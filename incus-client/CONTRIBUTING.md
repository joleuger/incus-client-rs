# Contributing to incus-client

Thank you for your interest in contributing! The most common contribution is adding
support for a new Incus API endpoint. This document explains how to do that and how
the project is structured.

---

## Repository structure

```
.
├── Cargo.toml                  # Workspace root
├── extract_openapi.py          # Helper script (see below)
├── incus-client/               # The published crate
│   ├── Cargo.toml
│   ├── README.md
│   ├── README_API.md           # Auto-generated API reference
│   ├── src/
│   │   ├── lib.rs              # Modified to include unix_socket.rs
│   │   ├── unix_socket.rs      # Handwritten
│   │   └── ...                 # Generated
│   └── .openapi-ignore
└── incus-client-tests/         # Integration tests (not published on crates.io)
```

Files listed in `incus-client/.openapi-ignore` are handwritten and must not be
modified by the generator. Everything else inside `incus-client/` is generated.

---

## Finding the right endpoint

Not sure which API endpoint corresponds to the CLI command you want to replicate?
Run any `incus` command with the `--debug` flag — it prints every API call it makes,
including the full URL and request body:

```bash
incus list --debug
incus launch images:ubuntu/22.04 my-instance --debug
```

This makes it straightforward to map a CLI command to the endpoint you need to add.

---

## Adding a new endpoint

### 1. Prerequisites

You need Java (11+) to run OpenAPI Generator. The easiest way to install it:

```bash
# Via Homebrew (macOS / Linux)
brew install openapi-generator

# Or download the JAR directly (no install needed)
curl -Lo openapi-generator-cli.jar \
  https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.6.0/openapi-generator-cli-7.6.0.jar

# Then run it with:
java -jar openapi-generator-cli.jar <args>
```

You also need Python 3 with `ruamel.yaml` for the extraction script:

```bash
pip install ruamel.yaml
```

### 2. Download the upstream spec

```bash
curl -Lo rest-api.yaml \
  https://raw.githubusercontent.com/lxc/incus/refs/heads/main/doc/rest-api.yaml
```

### 3. Find the endpoint you want

```bash
python extract_openapi.py rest-api.yaml --list
```

### 4. Extract it into the existing subset

The extraction script is additive — it merges the new paths into the existing file
without touching what is already there:

```bash
# Example: add network endpoints
python extract_openapi.py rest-api.yaml '/1.0/networks*' -o my-subset.yaml

# Add more endpoints in additional calls if needed
python extract_openapi.py rest-api.yaml '/1.0/operations*' -o my-subset.yaml
```

The script automatically pulls in all `$ref` dependencies (schemas, parameters)
transitively, so you do not need to worry about missing types.

### 5. Regenerate the client

Run the generator from the repository root:

```bash
openapi-generator generate \
  -i my-subset.yaml \
  -g rust \
  -o incus-client/ \
  --library reqwest \
  --package-name incus-client \
  --skip-validate-spec \
  --ignore-file-override incus-client/.openapi-ignore \
  --additional-properties=supportAsync=true
```

> `--skip-validate-spec` is required because the upstream Incus spec has minor
> OpenAPI conformance issues (extra `example` fields, missing parameter declarations)
> that do not affect the generated code.

The `.openapi-ignore` file protects handwritten files from being overwritten:

```
Cargo.toml
src/lib.rs
src/unix_socket.rs
```

After generation, move the generated `README.md` to `README_API.md` and replace
`README.md` with the one from the workspace root:

```bash
mv incus-client/README.md incus-client/README_API.md
cp README.md incus-client/README.md
```

### 6. Verify

```bash
cargo test

cd incus-client
cargo build
cargo clippy
```

Fix any compilation errors. The generator occasionally emits code that needs minor
manual adjustments.

### 7. Add a test

Add an integration test in `incus-client-tests/` that covers the new endpoint.
Tests require a running Incus daemon and are not run in CI by default:

```bash
cd incus-client-tests
cargo test -- --nocapture
```

### 8. Update the README

Add your endpoint to the covered endpoints table in `incus-client/README.md`:

```markdown
| `/1.0/networks` | `GET`, `POST` | Incus 6.7 |
```

### 9. Open a PR

Submit your pull request with:
- The regenerated files in `incus-client/`
- Your test in `incus-client-tests/`
- The updated endpoints table in `README.md`

---

## Changing handwritten code

The following files are maintained by hand and are not touched by the generator:

| File | Purpose |
|------|---------|
| `incus-client/src/unix_socket.rs` | Unix socket transport and path resolution |
| `incus-client/src/lib.rs` | Crate root and module re-exports |
| `incus-client/Cargo.toml` | Dependencies and feature flags |
| `incus-client/README.md` | This crate's documentation |

For changes to these files, please open an issue first to discuss the approach before
submitting a PR.

---

## Requesting an endpoint

If you need an endpoint but do not want to implement it yourself, open an issue with:

- The endpoint path (e.g. `/1.0/networks`)
- A brief description of your use case

---

## Questions

Feel free to open an issue for any questions about the project or the contribution process.