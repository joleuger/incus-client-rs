# InstanceFull

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | Option<**String**> | Architecture name | [optional]
**backups** | Option<[**Vec<models::InstanceBackup>**](InstanceBackup.md)> | List of backups. | [optional]
**config** | Option<**serde_json::Value**> | Instance configuration (see doc/instances.md) | [optional]
**created_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | Instance creation timestamp | [optional]
**description** | Option<**String**> | Instance description | [optional]
**devices** | Option<**serde_json::Value**> | Instance devices (see doc/instances.md) | [optional]
**disk_only** | Option<**bool**> | Whether only the instances disk should be restored | [optional]
**ephemeral** | Option<**bool**> | Whether the instance is ephemeral (deleted on shutdown) | [optional]
**expanded_config** | Option<**serde_json::Value**> | Expanded configuration (all profiles and local config merged) | [optional]
**expanded_devices** | Option<**serde_json::Value**> | Expanded devices (all profiles and local devices merged) | [optional]
**last_used_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | Last start timestamp | [optional]
**location** | Option<**String**> | What cluster member this instance is located on | [optional]
**name** | Option<**String**> | Instance name | [optional]
**profiles** | Option<**Vec<String>**> | List of profiles applied to the instance | [optional]
**project** | Option<**String**> | Instance project name | [optional]
**restore** | Option<**String**> | If set, instance will be restored to the provided snapshot name | [optional]
**snapshots** | Option<[**Vec<models::InstanceSnapshot>**](InstanceSnapshot.md)> | List of snapshots. | [optional]
**state** | Option<[**models::InstanceState**](InstanceState.md)> |  | [optional]
**stateful** | Option<**bool**> | Whether the instance currently has saved state on disk | [optional]
**status** | Option<**String**> | Instance status (see instance_state) | [optional]
**status_code** | Option<**i64**> |  | [optional]
**r#type** | Option<**String**> | The type of instance (container or virtual-machine) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


