# InstanceState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | Option<[**models::InstanceStateCpu**](InstanceStateCPU.md)> |  | [optional]
**disk** | Option<[**std::collections::HashMap<String, models::InstanceStateDisk>**](InstanceStateDisk.md)> | Disk usage key/value pairs | [optional]
**memory** | Option<[**models::InstanceStateMemory**](InstanceStateMemory.md)> |  | [optional]
**network** | Option<[**std::collections::HashMap<String, models::InstanceStateNetwork>**](InstanceStateNetwork.md)> | Network usage key/value pairs | [optional]
**os_info** | Option<[**models::InstanceStateOsInfo**](InstanceStateOSInfo.md)> |  | [optional]
**pid** | Option<**i64**> | PID of the runtime | [optional]
**processes** | Option<**i64**> | Number of processes in the instance | [optional]
**started_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | The time that the instance started at  API extension: instance_state_started_at. | [optional]
**status** | Option<**String**> | Current status (Running, Stopped, Frozen or Error) | [optional]
**status_code** | Option<**i64**> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


