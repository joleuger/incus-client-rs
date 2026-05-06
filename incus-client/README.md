# incus-client

[![Crates.io](https://img.shields.io/crates/v/incus-client.svg)](https://crates.io/crates/incus-client)
[![Docs.rs](https://docs.rs/incus-client/badge.svg)](https://docs.rs/incus-client)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

A Rust client for the [Incus](https://linuxcontainers.org/incus/) REST API, built with
[reqwest](https://github.com/seanmonstar/reqwest).

The API bindings are generated from the official Incus OpenAPI specification using
[OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator). The generated
code is checked in so that users do not need Java or any other tooling — just `cargo add`.

📖 **Official Incus REST API reference:** https://linuxcontainers.org/incus/docs/main/rest-api/
📖 **Generated API docs:** [README_API.md](https://github.com/joleuger/incus-client-rs/incus-client/README_API.md)

> **Looking for a maintainer!**
> This crate is regenerated periodically from the upstream spec.
> If you are interested in taking over or co-maintaining this crate, feel free to open an issue
> or reach out directly. Maintainership can be transferred.

---

## Features

| Feature        | Description                                                             | Default |
|----------------|-------------------------------------------------------------------------|---------|
| `unix-socket`  | Connect to Incus via the local Unix domain socket instead of HTTPS/TCP | no      |

By default the client communicates with Incus over HTTPS (TCP).
Enable the `unix-socket` feature to talk to a local Incus daemon through the Unix socket
(auto-detected, see below) without any TLS setup.

---

## Installation

```toml
[dependencies]
# HTTPS / remote access (default)
incus-client = "0.1"

# Local Unix socket access
incus-client = { version = "0.1", features = ["unix-socket"] }
```

---

## Usage


### Local access via Unix socket (feature = `"unix-socket"`)

When running on the same machine as the Incus daemon, connect through the Unix socket.
No TLS certificates required — authentication is handled by file-system permissions.

The socket path is resolved automatically in the following priority order:

1. Path passed explicitly to `resolve_socket_path()`
2. `INCUS_SOCKET` environment variable
3. `INCUS_DIR` environment variable + `/unix.socket`
4. `/run/incus/unix.socket` (if it exists)
5. `/var/lib/incus/unix.socket` (fallback)

If the main socket is not writable but `unix.socket.user` is (i.e. you are using
`incus-user`), the user socket is selected automatically and the project is scoped
to `user-<uid>`.

```rust
use incus_client::apis::instances_api;
use incus_client::unix_socket::unix_socket_configuration;

/// this resembles the cli command`incus list`
#[tokio::test]
async fn test_incus_list() {
    let configuration = unix_socket_configuration().unwrap();

    let result = instances_api::instances_get(&configuration, None, None, None)
        .await
        .unwrap();
    // to show the output, remind calling "cargo test -- --no-capture"
    println!("output: {:?}", result);
}
```

> **Permissions:** The Incus socket is typically only accessible by `root` or members of the
> `incus-admin` group. Make sure your process has the required permissions.


### Remote access over HTTPS (untested)

```rust
use incus_client::apis::configuration::Configuration;
use incus_client::apis::instances_api;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = Configuration {
        base_path: "https://my-incus-host:8443".to_string(),
        // Add your TLS client certificate here as needed.
        ..Default::default()
    };

    let instances = instances_api::get_instances(&config, Some("default"), None).await?;
    println!("{:?}", instances);

    Ok(())
}
```

> **Authentication:** Incus uses mutual TLS for remote access. Pass your client certificate
> via `reqwest::ClientBuilder::identity()` and trust the server certificate via
> `add_root_certificate()`.

---

## API behaviour you should know about

The Incus REST API has a few conventions that are not obvious from the generated types alone.

### Sync vs. async responses

Every response has a `type` field: `"sync"` for immediate results (HTTP 200) and
`"async"` for background operations (HTTP 202). Async responses include an `operation`
URL (`/1.0/operations/<uuid>`) in the body and a `Location` header pointing to the same.
Poll `GET /1.0/operations/<uuid>/wait` to block until the operation finishes, or subscribe
to the WebSocket event stream first (see below).

### ETag / If-Match on PUT requests

Incus supports both `PUT` (full replace) and `PATCH` (partial update). When using `PUT`,
retrieve the current object with `GET` first, read the `ETag` response header, and send it
back as `If-Match`. Incus will reject the `PUT` if the object was modified in the meantime,
preventing race conditions.

### Recursion

Collection endpoints (`GET /1.0/instances`, etc.) return a list of URLs by default.
Pass `?recursion=1` to have Incus inline the full objects instead, saving round-trips.

### Filtering

Collections accept an OData-style `?filter=` parameter:

```
GET /1.0/instances?filter=status eq Running
GET /1.0/instances?filter=config.image.os eq ubuntu or devices.eth0.nictype eq bridged
```

---

## Versioning

This crate uses its own version scheme starting at `0.1.0`, independent of the Incus
release cycle. The [covered endpoints table](#covered-endpoints) lists which Incus version
each endpoint was exported from.

The Incus REST API is stable under `/1.0/` and does not break backwards compatibility.
New functionality is added exclusively via `api_extensions`.

---

## Covered endpoints

Not all Incus API endpoints are included — only those listed here have been generated
and are maintained. If you need an endpoint that is missing, feel free to open an issue
or submit a PR (see [CONTRIBUTING.md](CONTRIBUTING.md)).

| Endpoint | Methods | Exported from |
|----------|---------|---------------|
| `/1.0` | `*` | 40dd4f1 (Pre 7.0) |
| `/1.0?public` | `` | 40dd4f1 (Pre 7.0) |
| `/1.0/operations` | `` | 40dd4f1 (Pre 7.0) |
| `/1.0/operations/{id}/wait` | `` | 40dd4f1 (Pre 7.0) |
| `/1.0/instances` | `` | 40dd4f1 (Pre 7.0) |
| `/1.0/instances/{name}*` | `` | 40dd4f1 (Pre 7.0) |
| `/1.0/images` | `GET` | 40dd4f1 (Pre 7.0) |
| `/1.0/images/{fingerprint}` | `` | 40dd4f1 (Pre 7.0) |

---

## Contributing

Missing an endpoint? Open an issue or submit a PR — adding a new endpoint is straightforward
and does not require deep knowledge of the codebase. See [CONTRIBUTING.md](https://github.com/joleuger/incus-client-rs/incus-client/CONTRIBUTING.md)
for the step-by-step process.

---

## Maintainership

This crate is maintained on a best-effort basis.

**If you would like to take over or co-maintain this crate**, please open an issue —
maintainership (including crates.io ownership) can be transferred.

---

## License

Licensed under the [Apache License, Version 2.0](LICENSE).

The upstream Incus REST API specification is copyright the LXC project contributors
and is also licensed under Apache-2.0.