# InstanceBackupsPost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compression_algorithm** | Option<**String**> | What compression algorithm to use | [optional]
**expires_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | When the backup expires (gets auto-deleted) | [optional]
**instance_only** | Option<**bool**> | Whether to ignore snapshots | [optional]
**name** | Option<**String**> | Backup name | [optional]
**optimized_storage** | Option<**bool**> | Whether to use a pool-optimized binary format (instead of plain tarball) | [optional]
**root_only** | Option<**bool**> | Whether to ignore dependent volumes | [optional]
**target** | Option<[**models::BackupTarget**](BackupTarget.md)> |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


