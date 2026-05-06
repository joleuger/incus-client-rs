# InstanceSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | Option<**String**> | Image alias name (for image source) | [optional]
**allow_inconsistent** | Option<**bool**> | Whether to ignore errors when copying (e.g. for volatile files) | [optional]
**base_image** | Option<**String**> | Base image fingerprint (for faster migration) | [optional]
**certificate** | Option<**String**> | Certificate (for remote images or migration) | [optional]
**fingerprint** | Option<**String**> | Image fingerprint (for image source) | [optional]
**instance_only** | Option<**bool**> | Whether the copy should skip the snapshots (for copy) | [optional]
**live** | Option<**bool**> | Whether this is a live migration (for migration) | [optional]
**mode** | Option<**String**> | Whether to use pull or push mode (for migration) | [optional]
**operation** | Option<**String**> | Remote operation URL (for migration) | [optional]
**project** | Option<**String**> | Source project name (for copy and local image) | [optional]
**properties** | Option<**std::collections::HashMap<String, String>**> | Image filters (for image source) | [optional]
**protocol** | Option<**String**> | Protocol name (for remote image) | [optional]
**refresh** | Option<**bool**> | Whether this is refreshing an existing instance (for migration and copy) | [optional]
**refresh_exclude_older** | Option<**bool**> | Whether to exclude source snapshots earlier than latest target snapshot | [optional]
**secret** | Option<**String**> | Remote server secret (for remote private images) | [optional]
**secrets** | Option<**std::collections::HashMap<String, String>**> | Map of migration websockets (for migration) | [optional]
**server** | Option<**String**> | Remote server URL (for remote images) | [optional]
**source** | Option<**String**> | Existing instance name or snapshot (for copy) | [optional]
**r#type** | Option<**String**> | Source type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


