# \ServerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**server_get**](ServerApi.md#server_get) | **GET** /1.0 | Get the server environment and configuration
[**server_get_untrusted**](ServerApi.md#server_get_untrusted) | **GET** /1.0?public | Get the server environment
[**server_patch**](ServerApi.md#server_patch) | **PATCH** /1.0 | Partially update the server configuration
[**server_put**](ServerApi.md#server_put) | **PUT** /1.0 | Update the server configuration



## server_get

> models::ServerGet200Response server_get(target, project)
Get the server environment and configuration

Shows the full server environment and configuration.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**target** | Option<**String**> | Cluster member name |  |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::ServerGet200Response**](server_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## server_get_untrusted

> models::ServerGetUntrusted200Response server_get_untrusted()
Get the server environment

Shows a small subset of the server environment and configuration which is required by untrusted clients to reach a server.  The `?public` part of the URL isn't required, it's simply used to separate the two behaviors of this endpoint.

### Parameters

This endpoint does not need any parameter.

### Return type

[**models::ServerGetUntrusted200Response**](server_get_untrusted_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## server_patch

> models::InstancePatch200Response server_patch(server, target)
Partially update the server configuration

Updates a subset of the server configuration.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**server** | [**ServerPut**](ServerPut.md) | Server configuration | [required] |
**target** | Option<**String**> | Cluster member name |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## server_put

> models::InstancePatch200Response server_put(server, target)
Update the server configuration

Updates the entire server configuration.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**server** | [**ServerPut**](ServerPut.md) | Server configuration | [required] |
**target** | Option<**String**> | Cluster member name |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

