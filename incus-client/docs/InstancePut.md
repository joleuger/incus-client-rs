# InstancePut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | Option<**String**> | Architecture name | [optional]
**config** | Option<**serde_json::Value**> | Instance configuration (see doc/instances.md) | [optional]
**description** | Option<**String**> | Instance description | [optional]
**devices** | Option<**serde_json::Value**> | Instance devices (see doc/instances.md) | [optional]
**disk_only** | Option<**bool**> | Whether only the instances disk should be restored | [optional]
**ephemeral** | Option<**bool**> | Whether the instance is ephemeral (deleted on shutdown) | [optional]
**profiles** | Option<**Vec<String>**> | List of profiles applied to the instance | [optional]
**restore** | Option<**String**> | If set, instance will be restored to the provided snapshot name | [optional]
**stateful** | Option<**bool**> | Whether the instance currently has saved state on disk | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


