# InstancePost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | Option<**serde_json::Value**> | Instance configuration file. | [optional]
**devices** | Option<**serde_json::Value**> | Instance devices. | [optional]
**profiles** | Option<**Vec<String>**> | List of profiles applied to the instance. | [optional]
**allow_inconsistent** | Option<**bool**> | AllowInconsistent allow inconsistent copies when migrating. | [optional]
**instance_only** | Option<**bool**> | Whether snapshots should be discarded (migration only) | [optional]
**live** | Option<**bool**> | Whether to perform a live migration (migration only) | [optional]
**migration** | Option<**bool**> | Whether the instance is being migrated to another server | [optional]
**name** | Option<**String**> | New name for the instance | [optional]
**pool** | Option<**String**> | Target pool for local cross-pool move | [optional]
**project** | Option<**String**> | Target project for local cross-project move | [optional]
**target** | Option<[**models::InstancePostTarget**](InstancePostTarget.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


