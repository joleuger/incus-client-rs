# \OperationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operation_wait_get**](OperationsApi.md#operation_wait_get) | **GET** /1.0/operations/{id}/wait | Wait for the operation
[**operations_get**](OperationsApi.md#operations_get) | **GET** /1.0/operations | Get the operations



## operation_wait_get

> models::OperationWaitGet200Response operation_wait_get(id, timeout)
Wait for the operation

Waits for the operation to reach a final state (or timeout) and retrieve its final state.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**id** | **String** | Operation ID | [required] |
**timeout** | Option<**i32**> | Timeout in seconds (-1 means never) |  |

### Return type

[**models::OperationWaitGet200Response**](operation_wait_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## operations_get

> models::OperationsGet200Response operations_get(project, all_projects)
Get the operations

Returns a JSON object of operation type to operation list (URLs).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**project** | Option<**String**> | Project name |  |
**all_projects** | Option<**bool**> | Retrieve operations from all projects |  |

### Return type

[**models::OperationsGet200Response**](operations_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

