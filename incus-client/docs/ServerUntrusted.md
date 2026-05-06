# ServerUntrusted

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_extensions** | Option<**Vec<String>**> | List of supported API extensions | [optional][readonly]
**api_status** | Option<**String**> | Support status of the current API (one of \"devel\", \"stable\" or \"deprecated\") | [optional][readonly]
**api_version** | Option<**String**> | API version number | [optional][readonly]
**auth** | Option<**String**> | Whether the client is trusted (one of \"trusted\" or \"untrusted\") | [optional][readonly]
**auth_methods** | Option<**Vec<String>**> | List of supported authentication methods | [optional][readonly]
**config** | Option<**serde_json::Value**> | Server configuration map (refer to doc/server.md) | [optional]
**public** | Option<**bool**> | Whether the server is public-only (only public endpoints are implemented) | [optional][readonly]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


