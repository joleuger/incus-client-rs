# InstanceSnapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | Option<**String**> | Architecture name | [optional]
**config** | Option<**serde_json::Value**> | Instance configuration (see doc/instances.md) | [optional]
**created_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | Instance creation timestamp | [optional]
**description** | Option<**String**> | Instance description | [optional]
**devices** | Option<**serde_json::Value**> | Instance devices (see doc/instances.md) | [optional]
**ephemeral** | Option<**bool**> | Whether the instance is ephemeral (deleted on shutdown) | [optional]
**expanded_config** | Option<**serde_json::Value**> | Expanded configuration (all profiles and local config merged) | [optional]
**expanded_devices** | Option<**serde_json::Value**> | Expanded devices (all profiles and local devices merged) | [optional]
**expires_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | When the snapshot expires (gets auto-deleted) | [optional]
**last_used_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | Last start timestamp | [optional]
**name** | Option<**String**> | Snapshot name | [optional]
**profiles** | Option<**Vec<String>**> | List of profiles applied to the instance | [optional]
**size** | Option<**i64**> | Size of the snapshot in bytes | [optional]
**stateful** | Option<**bool**> | Whether the instance currently has saved state on disk | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


