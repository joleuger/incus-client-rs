# InstanceBackup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | When the backup was created | [optional]
**expires_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | When the backup expires (gets auto-deleted) | [optional]
**instance_only** | Option<**bool**> | Whether to ignore snapshots | [optional]
**name** | Option<**String**> | Backup name | [optional]
**optimized_storage** | Option<**bool**> | Whether to use a pool-optimized binary format (instead of plain tarball) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


