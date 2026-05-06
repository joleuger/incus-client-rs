# ImagePut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_update** | Option<**bool**> | Whether the image should auto-update when a new build is available | [optional]
**expires_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | When the image becomes obsolete | [optional]
**profiles** | Option<**Vec<String>**> | List of profiles to use when creating from this image (if none provided by user) | [optional]
**properties** | Option<**std::collections::HashMap<String, String>**> | Descriptive properties | [optional]
**public** | Option<**bool**> | Whether the image is available to unauthenticated users | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


