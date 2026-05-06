# InstanceStateNetwork

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | Option<[**Vec<models::InstanceStateNetworkAddress>**](InstanceStateNetworkAddress.md)> | List of IP addresses | [optional]
**counters** | Option<[**models::InstanceStateNetworkCounters**](InstanceStateNetworkCounters.md)> |  | [optional]
**host_name** | Option<**String**> | Name of the interface on the host | [optional]
**hwaddr** | Option<**String**> | MAC address | [optional]
**mtu** | Option<**i64**> | MTU (maximum transmit unit) for the interface | [optional]
**state** | Option<**String**> | Administrative state of the interface (up/down) | [optional]
**r#type** | Option<**String**> | Type of interface (broadcast, loopback, point-to-point, ...) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


