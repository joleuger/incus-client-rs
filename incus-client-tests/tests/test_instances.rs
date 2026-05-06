// SPDX-License-Identifier: MIT OR Apache-2.0
//
// Author: Johannes Leupolz <dev@leupolz.eu>

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
