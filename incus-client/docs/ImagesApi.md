# \ImagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**image_delete**](ImagesApi.md#image_delete) | **DELETE** /1.0/images/{fingerprint} | Delete the image
[**image_get**](ImagesApi.md#image_get) | **GET** /1.0/images/{fingerprint} | Get the image
[**image_patch**](ImagesApi.md#image_patch) | **PATCH** /1.0/images/{fingerprint} | Partially update the image
[**image_put**](ImagesApi.md#image_put) | **PUT** /1.0/images/{fingerprint} | Update the image
[**images_get**](ImagesApi.md#images_get) | **GET** /1.0/images | Get the images



## image_delete

> models::InstancesPut202Response image_delete(fingerprint, project)
Delete the image

Removes the image from the image store.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**fingerprint** | **String** | Fingerprint | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## image_get

> models::ImageGet200Response image_get(fingerprint, project)
Get the image

Gets a specific image.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**fingerprint** | **String** | Fingerprint | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::ImageGet200Response**](image_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## image_patch

> models::InstancePatch200Response image_patch(fingerprint, image, project)
Partially update the image

Updates a subset of the image definition.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**fingerprint** | **String** | Fingerprint | [required] |
**image** | [**ImagePut**](ImagePut.md) | Image configuration | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## image_put

> models::InstancePatch200Response image_put(fingerprint, image, project)
Update the image

Updates the entire image definition.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**fingerprint** | **String** | Fingerprint | [required] |
**image** | [**ImagePut**](ImagePut.md) | Image configuration | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## images_get

> models::ImagesGet200Response images_get(project, filter, all_projects)
Get the images

Returns a list of images (URLs).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**project** | Option<**String**> | Project name |  |
**filter** | Option<**String**> | Collection filter |  |
**all_projects** | Option<**bool**> | Retrieve images from all projects |  |

### Return type

[**models::ImagesGet200Response**](images_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

