# ServerEnvironment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | Option<**Vec<String>**> | List of addresses the server is listening on | [optional]
**architectures** | Option<**Vec<String>**> | List of architectures supported by the server | [optional]
**certificate** | Option<**String**> | Server certificate as PEM encoded X509 | [optional]
**certificate_fingerprint** | Option<**String**> | Server certificate fingerprint as SHA256 | [optional]
**driver** | Option<**String**> | List of supported instance drivers (separate by \" | \") | [optional]
**driver_version** | Option<**String**> | List of supported instance driver versions (separate by \" | \") | [optional]
**firewall** | Option<**String**> | Current firewall driver | [optional]
**kernel** | Option<**String**> | OS kernel name | [optional]
**kernel_architecture** | Option<**String**> | OS kernel architecture | [optional]
**kernel_features** | Option<**std::collections::HashMap<String, String>**> | Map of kernel features that were tested on startup | [optional]
**kernel_version** | Option<**String**> | Kernel version | [optional]
**lxc_features** | Option<**std::collections::HashMap<String, String>**> | Map of LXC features that were tested on startup | [optional]
**os_name** | Option<**String**> | Name of the operating system (Linux distribution) | [optional]
**os_version** | Option<**String**> | Version of the operating system (Linux distribution) | [optional]
**project** | Option<**String**> | Current project name | [optional]
**server** | Option<**String**> | Server implementation name | [optional]
**server_clustered** | Option<**bool**> | Whether the server is part of a cluster | [optional]
**server_event_mode** | Option<**String**> | Mode that the event distribution subsystem is operating in on this server. Either \"full-mesh\", \"hub-server\" or \"hub-client\". | [optional]
**server_name** | Option<**String**> | Server hostname | [optional]
**server_pid** | Option<**i64**> | PID of the daemon | [optional]
**server_version** | Option<**String**> | Server version | [optional]
**storage** | Option<**String**> | List of active storage drivers (separate by \" | \") | [optional]
**storage_supported_drivers** | Option<[**Vec<models::ServerStorageDriverInfo>**](ServerStorageDriverInfo.md)> | List of supported storage drivers | [optional]
**storage_version** | Option<**String**> | List of active storage driver versions (separate by \" | \") | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


