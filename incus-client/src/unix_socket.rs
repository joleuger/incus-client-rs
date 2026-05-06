// SPDX-License-Identifier: MIT OR Apache-2.0
//
// Author: Johannes Leupolz <dev@leupolz.eu>
//! Unix domain socket transport for the Incus client.
//!
//! Enabled via the `unix-socket` Cargo feature.
//!
//! # Quick start
//!
//! ```rust,no_run
//! # #[cfg(feature = "unix-socket")]
//! use incus_client::unix_socket::{resolve_socket_path, unix_socket_client, UNIX_BASE_PATH};
//! use incus_client::apis::configuration::Configuration;
//!
//! # #[cfg(feature = "unix-socket")]
//! # {
//! let (socket_path, _project) = resolve_socket_path(None);
//! let client = unix_socket_client(&socket_path).expect("failed to build Unix socket client");
//!
//! let config = Configuration {
//!     base_path: UNIX_BASE_PATH.to_string(),
//!     client,
//!     ..Default::default()
//! };
//! # }
//! ```

use std::env;
use std::path::{Path, PathBuf};

use crate::apis::configuration::Configuration;
use reqwest::ClientBuilder;

use nix::unistd::access;
use nix::unistd::geteuid;
use nix::unistd::AccessFlags;

/// The base URL to use with a Unix socket client.
/// reqwest uses this sentinel value to route requests through the socket.
pub const UNIX_BASE_PATH: &str = "http://unix.socket";

/// Builds a reqwest configuration that connects via the given Unix domain socket.
pub fn unix_socket_configuration() -> reqwest::Result<Configuration> {
    let (unix_socket_path,_) = resolve_socket_path(None);

    let unix_socket = ClientBuilder::new()
        .unix_socket(unix_socket_path)
        .connection_verbose(true)
        .build()?;

    let configuration = Configuration {
        base_path: "http://unix.socket".to_string(),
        user_agent: None,
        client: unix_socket,
        basic_auth: None,
        oauth_access_token: None,
        bearer_access_token: None,
        api_key: None,
    };
    Ok(configuration)
}

/// Resolves the Incus Unix socket path and an optional default project name.
///
/// Priority:
///   1. Explicit `path` argument
///   2. `INCUS_SOCKET` environment variable
///   3. `INCUS_DIR` environment variable + `/unix.socket`
///   4. `/run/incus/unix.socket` (if it exists)
///   5. `/var/lib/incus/unix.socket` (fallback)
///
/// If the main socket is not writable but a sibling `unix.socket.user` is
/// (i.e. you are using `incus-user`), the user socket is selected instead
/// and a project name `user-<uid>` is returned to restrict access appropriately.
pub fn resolve_socket_path(path: Option<&str>) -> (PathBuf, Option<String>) {
    // 1. Explicit argument
    if let Some(p) = path.filter(|p| !p.is_empty()) {
        return (PathBuf::from(p), None);
    }

    // 2. INCUS_SOCKET environment variable
    if let Ok(p) = env::var("INCUS_SOCKET") {
        if !p.is_empty() {
            return (PathBuf::from(p), None);
        }
    }

    // 3. INCUS_DIR environment variable
    let incus_dir_from_env = env::var("INCUS_DIR");
    let incus_dir = if incus_dir_from_env.as_ref().is_ok_and(|d| !d.is_empty()){
        PathBuf::from(incus_dir_from_env.unwrap())
    // 4. /run/incus (modern systemd-managed path)
    } else if Path::new("/run/incus/unix.socket").exists() {
        PathBuf::from("/run/incus")
    // 5. /var/lib/incus (traditional fallback)
    } else {
        PathBuf::from("/var/lib/incus")
    };

    let socket = incus_dir.join("unix.socket");
    let user_socket = incus_dir.join("unix.socket.user");

    // If the main socket is not writable but the user socket is, switch to it.
    // incus-user typically restricts the visible project list to the current user.
    if !is_writable(&socket) && is_writable(&user_socket) {
        return (user_socket, Some(format!("user-{}", geteuid())));
    }

    (socket, None)
}

fn is_writable(path: &Path) -> bool {
    access(path, AccessFlags::W_OK).is_ok()
}
