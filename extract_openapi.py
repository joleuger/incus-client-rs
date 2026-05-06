#!/usr/bin/env python3
"""
extract_openapi.py — Extract selected paths from an OpenAPI YAML spec.

Copies only the requested path entries plus all $ref-referenced schemas
(transitively) from components/schemas, components/parameters, etc.
Produces a valid, minimal OpenAPI YAML you can feed to openapi-generator.

Usage:
    python extract_openapi.py spec.yaml [options] PATH [PATH ...]

Examples:
    # Single path
    python extract_openapi.py rest-api.yaml /1.0/instances

    # Multiple paths (glob-style * supported)
    python extract_openapi.py rest-api.yaml '/1.0/instances' '/1.0/instances/{name}'

    # All instance-related paths
    python extract_openapi.py rest-api.yaml '/1.0/instances*'

    # Write to file instead of stdout
    python extract_openapi.py rest-api.yaml -o instances.yaml '/1.0/instances*'

    # Fetch spec directly from URL
    python extract_openapi.py https://raw.githubusercontent.com/lxc/incus/refs/heads/main/doc/rest-api.yaml -o out.yaml '/1.0/instances*'

SPDX-License-Identifier: MIT OR Apache-2.0

Copyright 2026 Johannes Leupolz <dev@leupolz.eu>

"""

import argparse
import fnmatch
import re
import sys
import urllib.request
from typing import Any

from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.default_flow_style = False
yaml.width = 120


# ---------------------------------------------------------------------------
# $ref resolution
# ---------------------------------------------------------------------------

REF_RE = re.compile(r"#/(.+)")


def collect_refs(node: Any, found: set[str]) -> None:
    """Recursively walk a YAML node and collect all local $ref targets."""
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "$ref" and isinstance(v, str):
                m = REF_RE.match(v)
                if m:
                    found.add(m.group(1))  # e.g. "components/schemas/Instance"
            else:
                collect_refs(v, found)
    elif isinstance(node, list):
        for item in node:
            collect_refs(item, found)


def resolve_path(spec: dict, ref_path: str) -> Any:
    """Follow a slash-separated path into the spec dict."""
    parts = ref_path.split("/")
    node = spec
    for part in parts:
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node


def collect_all_deps(spec: dict, initial_refs: set[str]) -> set[str]:
    """
    Given a set of initial $ref paths, keep resolving transitively until
    no new refs are found.
    """
    all_refs: set[str] = set()
    queue = set(initial_refs)
    while queue:
        ref = queue.pop()
        if ref in all_refs:
            continue
        all_refs.add(ref)
        node = resolve_path(spec, ref)
        if node is not None:
            new_refs: set[str] = set()
            collect_refs(node, new_refs)
            queue.update(new_refs - all_refs)
    return all_refs


# ---------------------------------------------------------------------------
# Building the output spec
# ---------------------------------------------------------------------------

def set_nested(target: dict, path: str, value: Any) -> None:
    """Set target[a][b][c] = value for a slash-separated path."""
    parts = path.split("/")
    node = target
    for part in parts[:-1]:
        node = node.setdefault(part, {})
    node[parts[-1]] = value



def deep_merge(base, overlay):
    """Recursively merge overlay into base. Overlay wins on conflicts."""
    if isinstance(base, dict) and isinstance(overlay, dict):
        merged = dict(base)
        for k, v in overlay.items():
            merged[k] = deep_merge(base[k], v) if k in base else v
        return merged
    return overlay


def build_output(spec: dict, selected_paths: dict, deps: set[str]) -> dict:
    out: dict = {}

    # Top-level metadata — covers both Swagger 2.0 and OpenAPI 3.x
    for key in ("swagger", "openapi", "info", "host", "basePath",
                "schemes", "consumes", "produces", "servers", "securityDefinitions"):
        if key in spec:
            out[key] = spec[key]

    # Selected paths
    out["paths"] = selected_paths

    # Resolved components
    for ref_path in sorted(deps):
        value = resolve_path(spec, ref_path)
        if value is not None:
            set_nested(out, ref_path, value)

    return out


# ---------------------------------------------------------------------------
# Path matching
# ---------------------------------------------------------------------------

def match_paths(all_paths: list[str], patterns: list[str]) -> list[str]:
    matched = []
    for path in all_paths:
        for pattern in patterns:
            if fnmatch.fnmatch(path, pattern):
                matched.append(path)
                break
    return matched


# ---------------------------------------------------------------------------
# Spec loading
# ---------------------------------------------------------------------------

def load_spec(source: str) -> dict:
    if source.startswith("http://") or source.startswith("https://"):
        print(f"Fetching {source} …", file=sys.stderr)
        with urllib.request.urlopen(source) as resp:
            return yaml.load(resp.read().decode())
    else:
        with open(source, encoding="utf-8") as f:
            return yaml.load(f)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract selected API paths (+ all $ref deps) from an OpenAPI YAML spec.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "spec",
        help="Path or URL to the OpenAPI YAML file",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        metavar="PATH",
        help="API path(s) to extract, supports * glob (e.g. '/1.0/instances*')",
    )
    parser.add_argument(
        "-o", "--output",
        default="-",
        help="Output file (default: stdout)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Just list all paths in the spec and exit",
    )
    args = parser.parse_args()

    spec = load_spec(args.spec)

    all_paths = list(spec.get("paths", {}).keys())

    if args.list:
        for p in sorted(all_paths):
            print(p)
        return

    if not args.paths:
        parser.error("PATH argument(s) required unless --list is used")

    matched = match_paths(all_paths, args.paths)

    if not matched:
        print(
            f"No paths matched {args.paths}.\n"
            f"Run with --list to see all available paths.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Selected {len(matched)} path(s):", file=sys.stderr)
    for p in matched:
        print(f"  {p}", file=sys.stderr)

    # Collect selected path nodes
    selected_paths = {p: spec["paths"][p] for p in matched}

    # Collect all $refs from selected paths (transitive)
    initial_refs: set[str] = set()
    collect_refs(selected_paths, initial_refs)
    all_deps = collect_all_deps(spec, initial_refs)

    print(f"Resolved {len(all_deps)} component reference(s).", file=sys.stderr)

    out = build_output(spec, selected_paths, all_deps)

    if args.output == "-":
        yaml.dump(out, sys.stdout)
    else:
        import os
        if os.path.exists(args.output):
            with open(args.output, encoding="utf-8") as f:
                existing = yaml.load(f)
            if existing:
                out = deep_merge(existing, out)
                print(f"Merged into existing {args.output}", file=sys.stderr)
        with open(args.output, "w", encoding="utf-8") as f:
            yaml.dump(out, f)
        print(f"Written to {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()