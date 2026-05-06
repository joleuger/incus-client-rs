# ImageMetadataTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_only** | Option<**bool**> | Whether to trigger only if the file is missing | [optional]
**gid** | Option<**String**> | The file owner gid. | [optional]
**mode** | Option<**String**> | The file permissions. | [optional]
**properties** | Option<**std::collections::HashMap<String, String>**> | Key/value properties to pass to the template | [optional]
**template** | Option<**String**> | The template itself as a valid pongo2 template | [optional]
**uid** | Option<**String**> | The file owner uid. | [optional]
**when** | Option<**Vec<String>**> | When to trigger the template (create, copy or start) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


