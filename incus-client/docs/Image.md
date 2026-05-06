# Image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | Option<[**Vec<models::ImageAlias>**](ImageAlias.md)> | List of aliases | [optional]
**architecture** | Option<**String**> | Architecture | [optional]
**auto_update** | Option<**bool**> | Whether the image should auto-update when a new build is available | [optional]
**cached** | Option<**bool**> | Whether the image is an automatically cached remote image | [optional]
**created_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | When the image was originally created | [optional]
**expires_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | When the image becomes obsolete | [optional]
**filename** | Option<**String**> | Original filename | [optional]
**fingerprint** | Option<**String**> | Full SHA-256 fingerprint | [optional]
**last_used_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | Last time the image was used | [optional]
**profiles** | Option<**Vec<String>**> | List of profiles to use when creating from this image (if none provided by user) | [optional]
**project** | Option<**String**> | Project name | [optional]
**properties** | Option<**std::collections::HashMap<String, String>**> | Descriptive properties | [optional]
**public** | Option<**bool**> | Whether the image is available to unauthenticated users | [optional]
**size** | Option<**i64**> | Size of the image in bytes | [optional]
**r#type** | Option<**String**> | Type of image (container or virtual-machine) | [optional]
**update_source** | Option<[**models::ImageSource**](ImageSource.md)> |  | [optional]
**uploaded_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | When the image was added to this server | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


