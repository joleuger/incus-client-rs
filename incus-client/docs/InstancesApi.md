# \InstancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_access**](InstancesApi.md#instance_access) | **GET** /1.0/instances/{name}/access | Get who has access to an instance
[**instance_backup_delete**](InstancesApi.md#instance_backup_delete) | **DELETE** /1.0/instances/{name}/backups/{backup} | Delete a backup
[**instance_backup_export**](InstancesApi.md#instance_backup_export) | **GET** /1.0/instances/{name}/backups/{backup}/export | Get the raw backup file(s)
[**instance_backup_get**](InstancesApi.md#instance_backup_get) | **GET** /1.0/instances/{name}/backups/{backup} | Get the backup
[**instance_backup_post**](InstancesApi.md#instance_backup_post) | **POST** /1.0/instances/{name}/backups/{backup} | Rename a backup
[**instance_backups_get**](InstancesApi.md#instance_backups_get) | **GET** /1.0/instances/{name}/backups | Get the backups
[**instance_backups_get_recursion1**](InstancesApi.md#instance_backups_get_recursion1) | **GET** /1.0/instances/{name}/backups?recursion=1 | Get the backups
[**instance_backups_post**](InstancesApi.md#instance_backups_post) | **POST** /1.0/instances/{name}/backups | Create a backup
[**instance_bitmaps_post**](InstancesApi.md#instance_bitmaps_post) | **POST** /1.0/instances/{name}/bitmaps | Create a bitmap
[**instance_console_delete**](InstancesApi.md#instance_console_delete) | **DELETE** /1.0/instances/{name}/console | Clear the console log
[**instance_console_get**](InstancesApi.md#instance_console_get) | **GET** /1.0/instances/{name}/console | Get console output
[**instance_console_post**](InstancesApi.md#instance_console_post) | **POST** /1.0/instances/{name}/console | Connect to console
[**instance_debug_memory_get**](InstancesApi.md#instance_debug_memory_get) | **GET** /1.0/instances/{name}/debug/memory | Get memory debug information of an instance
[**instance_debug_repair_post**](InstancesApi.md#instance_debug_repair_post) | **GET** /1.0/instances/{name}/debug/repair | Trigger a repair action on the instance.
[**instance_delete**](InstancesApi.md#instance_delete) | **DELETE** /1.0/instances/{name} | Delete an instance
[**instance_exec_output_delete**](InstancesApi.md#instance_exec_output_delete) | **DELETE** /1.0/instances/{name}/logs/exec-output/{filename} | Delete the exec record-output file
[**instance_exec_output_get**](InstancesApi.md#instance_exec_output_get) | **GET** /1.0/instances/{name}/logs/exec-output/{filename} | Get the exec-output log file
[**instance_exec_outputs_get**](InstancesApi.md#instance_exec_outputs_get) | **GET** /1.0/instances/{name}/logs/exec-output | Get the exec record-output files
[**instance_exec_post**](InstancesApi.md#instance_exec_post) | **POST** /1.0/instances/{name}/exec | Run a command
[**instance_files_delete**](InstancesApi.md#instance_files_delete) | **DELETE** /1.0/instances/{name}/files | Delete a file
[**instance_files_get**](InstancesApi.md#instance_files_get) | **GET** /1.0/instances/{name}/files | Get a file
[**instance_files_head**](InstancesApi.md#instance_files_head) | **HEAD** /1.0/instances/{name}/files | Get metadata for a file
[**instance_files_post**](InstancesApi.md#instance_files_post) | **POST** /1.0/instances/{name}/files | Create or replace a file
[**instance_get**](InstancesApi.md#instance_get) | **GET** /1.0/instances/{name} | Get the instance
[**instance_get_recursion1**](InstancesApi.md#instance_get_recursion1) | **GET** /1.0/instances/{name}?recursion=1 | Get the instance
[**instance_log_delete**](InstancesApi.md#instance_log_delete) | **DELETE** /1.0/instances/{name}/logs/{filename} | Delete the log file
[**instance_log_get**](InstancesApi.md#instance_log_get) | **GET** /1.0/instances/{name}/logs/{filename} | Get the log file
[**instance_logs_get**](InstancesApi.md#instance_logs_get) | **GET** /1.0/instances/{name}/logs | Get the log files
[**instance_metadata_get**](InstancesApi.md#instance_metadata_get) | **GET** /1.0/instances/{name}/metadata | Get the instance image metadata
[**instance_metadata_patch**](InstancesApi.md#instance_metadata_patch) | **PATCH** /1.0/instances/{name}/metadata | Partially update the image metadata
[**instance_metadata_put**](InstancesApi.md#instance_metadata_put) | **PUT** /1.0/instances/{name}/metadata | Update the image metadata
[**instance_metadata_templates_delete**](InstancesApi.md#instance_metadata_templates_delete) | **DELETE** /1.0/instances/{name}/metadata/templates | Delete a template file
[**instance_metadata_templates_get**](InstancesApi.md#instance_metadata_templates_get) | **GET** /1.0/instances/{name}/metadata/templates | Get the template file names or a specific
[**instance_metadata_templates_post**](InstancesApi.md#instance_metadata_templates_post) | **POST** /1.0/instances/{name}/metadata/templates | Create or replace a template file
[**instance_patch**](InstancesApi.md#instance_patch) | **PATCH** /1.0/instances/{name} | Partially update the instance
[**instance_post**](InstancesApi.md#instance_post) | **POST** /1.0/instances/{name} | Rename or move/migrate an instance
[**instance_put**](InstancesApi.md#instance_put) | **PUT** /1.0/instances/{name} | Update the instance
[**instance_rebuild_post**](InstancesApi.md#instance_rebuild_post) | **POST** /1.0/instances/{name}/rebuild | Rebuild an instance
[**instance_sftp**](InstancesApi.md#instance_sftp) | **GET** /1.0/instances/{name}/sftp | Get the instance SFTP connection
[**instance_snapshot_delete**](InstancesApi.md#instance_snapshot_delete) | **DELETE** /1.0/instances/{name}/snapshots/{snapshot} | Delete a snapshot
[**instance_snapshot_get**](InstancesApi.md#instance_snapshot_get) | **GET** /1.0/instances/{name}/snapshots/{snapshot} | Get the snapshot
[**instance_snapshot_patch**](InstancesApi.md#instance_snapshot_patch) | **PATCH** /1.0/instances/{name}/snapshots/{snapshot} | Partially update snapshot
[**instance_snapshot_post**](InstancesApi.md#instance_snapshot_post) | **POST** /1.0/instances/{name}/snapshots/{snapshot} | Rename or move/migrate a snapshot
[**instance_snapshot_put**](InstancesApi.md#instance_snapshot_put) | **PUT** /1.0/instances/{name}/snapshots/{snapshot} | Update snapshot
[**instance_snapshots_get**](InstancesApi.md#instance_snapshots_get) | **GET** /1.0/instances/{name}/snapshots | Get the snapshots
[**instance_snapshots_get_recursion1**](InstancesApi.md#instance_snapshots_get_recursion1) | **GET** /1.0/instances/{name}/snapshots?recursion=1 | Get the snapshots
[**instance_snapshots_post**](InstancesApi.md#instance_snapshots_post) | **POST** /1.0/instances/{name}/snapshots | Create a snapshot
[**instance_state_get**](InstancesApi.md#instance_state_get) | **GET** /1.0/instances/{name}/state | Get the runtime state
[**instance_state_put**](InstancesApi.md#instance_state_put) | **PUT** /1.0/instances/{name}/state | Change the state
[**instances_get**](InstancesApi.md#instances_get) | **GET** /1.0/instances | Get the instances
[**instances_post**](InstancesApi.md#instances_post) | **POST** /1.0/instances | Create a new instance
[**instances_put**](InstancesApi.md#instances_put) | **PUT** /1.0/instances | Bulk instance state update



## instance_access

> models::InstanceAccess200Response instance_access(name, project)
Get who has access to an instance

Gets the access information for the instance.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstanceAccess200Response**](instance_access_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_backup_delete

> models::InstancesPut202Response instance_backup_delete(name, backup, project)
Delete a backup

Deletes the instance backup.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**backup** | **String** | Backup name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_backup_export

> instance_backup_export(name, backup, project)
Get the raw backup file(s)

Download the raw backup file(s) from the server.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**backup** | **String** | Backup name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_backup_get

> models::InstanceBackupGet200Response instance_backup_get(name, backup, project)
Get the backup

Gets a specific instance backup.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**backup** | **String** | Backup name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstanceBackupGet200Response**](instance_backup_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_backup_post

> models::InstancesPut202Response instance_backup_post(name, backup, project, backup2)
Rename a backup

Renames an instance backup.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**backup** | **String** | Backup name | [required] |
**project** | Option<**String**> | Project name |  |
**backup2** | Option<[**InstanceBackupPost**](InstanceBackupPost.md)> | Backup rename |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_backups_get

> models::InstanceBackupsGet200Response instance_backups_get(name, project)
Get the backups

Returns a list of instance backups (URLs).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstanceBackupsGet200Response**](instance_backups_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_backups_get_recursion1

> models::InstanceBackupsGetRecursion1200Response instance_backups_get_recursion1(name, project)
Get the backups

Returns a list of instance backups (structs).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstanceBackupsGetRecursion1200Response**](instance_backups_get_recursion1_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_backups_post

> models::InstancesPut202Response instance_backups_post(name, project, backup)
Create a backup

Creates a new backup.  If the `Accept` header is set to `application/octet-stream`, this directly streams the backup tarball to the client without any intermediate operation.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |
**backup** | Option<[**InstanceBackupsPost**](InstanceBackupsPost.md)> | Backup request |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_bitmaps_post

> models::InstancesPut202Response instance_bitmaps_post(name, project, bitmap)
Create a bitmap

Creates a new bitmap.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |
**bitmap** | Option<[**StorageVolumeBitmapsPost**](StorageVolumeBitmapsPost.md)> | Bitmap request |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_console_delete

> models::InstancePatch200Response instance_console_delete(name, project)
Clear the console log

Clears the console log buffer.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_console_get

> instance_console_get(name, project, r#type)
Get console output

Gets the console output for the instance either as text log or as vga screendump.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |
**r#type** | Option<**String**> | Console type |  |[default to log]

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_console_post

> models::InstancesPut202Response instance_console_post(name, project, console)
Connect to console

Connects to the console of an instance.  The returned operation metadata will contain two websockets, one for data and one for control.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |
**console** | Option<[**InstanceConsolePost**](InstanceConsolePost.md)> | Console request |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_debug_memory_get

> instance_debug_memory_get(name, project, format)
Get memory debug information of an instance

Returns memory debug information of a running instance. Only supported for VMs.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |
**format** | Option<**String**> | Memory dump format |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_debug_repair_post

> models::InstancePatch200Response instance_debug_repair_post(name, project, state)
Trigger a repair action on the instance.

Runs an internal repair action on the instance.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |
**state** | Option<[**InstanceDebugRepairPost**](InstanceDebugRepairPost.md)> | State |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_delete

> models::InstancesPut202Response instance_delete(name, project)
Delete an instance

Deletes a specific instance.  This also deletes anything owned by the instance such as snapshots and backups.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_exec_output_delete

> models::InstancePatch200Response instance_exec_output_delete(name, filename, project)
Delete the exec record-output file

Removes the exec record-output file.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**filename** | **String** | Log file name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_exec_output_get

> instance_exec_output_get(name, filename, project)
Get the exec-output log file

Gets the exec-output file.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**filename** | **String** | Log file name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_exec_outputs_get

> models::InstanceExecOutputsGet200Response instance_exec_outputs_get(name, project)
Get the exec record-output files

Returns a list of exec record-output files (URLs).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstanceExecOutputsGet200Response**](instance_exec_outputs_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_exec_post

> models::InstancesPut202Response instance_exec_post(name, project, exec)
Run a command

Executes a command inside an instance.  The returned operation metadata will contain either 2 or 4 websockets. In non-interactive mode, you'll get one websocket for each of stdin, stdout and stderr. In interactive mode, a single bi-directional websocket is used for stdin and stdout/stderr.  An additional \"control\" socket is always added on top which can be used for out of band communications. This allows sending signals and window sizing information through.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |
**exec** | Option<[**InstanceExecPost**](InstanceExecPost.md)> | Exec request |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_files_delete

> models::InstancePatch200Response instance_files_delete(name, path, project, x_incus_force)
Delete a file

Removes the file.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**path** | Option<**String**> | Path to the file |  |
**project** | Option<**String**> | Project name |  |
**x_incus_force** | Option<**String**> | Perform recursive deletion |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_files_get

> instance_files_get(name, path, project)
Get a file

Gets the file content. If it's a directory, a json list of files will be returned instead.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**path** | Option<**String**> | Path to the file |  |
**project** | Option<**String**> | Project name |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_files_head

> instance_files_head(name, path, project)
Get metadata for a file

Gets the file or directory metadata.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**path** | Option<**String**> | Path to the file |  |
**project** | Option<**String**> | Project name |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_files_post

> models::InstancePatch200Response instance_files_post(name, path, project, x_incus_uid, x_incus_gid, x_incus_mode, x_incus_type, x_incus_write)
Create or replace a file

Creates a new file in the instance.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**path** | Option<**String**> | Path to the file |  |
**project** | Option<**String**> | Project name |  |
**x_incus_uid** | Option<**String**> | File owner UID |  |
**x_incus_gid** | Option<**String**> | File owner GID |  |
**x_incus_mode** | Option<**String**> | File mode |  |
**x_incus_type** | Option<**String**> | Type of file (file, symlink or directory) |  |
**x_incus_write** | Option<**String**> | Write mode (overwrite or append) |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_get

> models::InstanceGet200Response instance_get(name, project)
Get the instance

Gets a specific instance (basic struct).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstanceGet200Response**](instance_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_get_recursion1

> models::InstanceGetRecursion1200Response instance_get_recursion1(name, project)
Get the instance

Gets a specific instance (full struct).  recursion=1 also includes information about state, snapshots and backups.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstanceGetRecursion1200Response**](instance_get_recursion1_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_log_delete

> models::InstancePatch200Response instance_log_delete(name, filename, project)
Delete the log file

Removes the log file.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**filename** | **String** | Log file name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_log_get

> instance_log_get(name, filename, project)
Get the log file

Gets the log file.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**filename** | **String** | Log file name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_logs_get

> models::InstanceLogsGet200Response instance_logs_get(name, project)
Get the log files

Returns a list of log files (URLs).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstanceLogsGet200Response**](instance_logs_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_metadata_get

> models::InstanceMetadataGet200Response instance_metadata_get(name, project)
Get the instance image metadata

Gets the image metadata for the instance.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstanceMetadataGet200Response**](instance_metadata_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_metadata_patch

> models::InstancePatch200Response instance_metadata_patch(name, metadata, project)
Partially update the image metadata

Updates a subset of the instance image metadata.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**metadata** | [**ImageMetadata**](ImageMetadata.md) | Image metadata | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_metadata_put

> models::InstancePatch200Response instance_metadata_put(name, metadata, project)
Update the image metadata

Updates the instance image metadata.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**metadata** | [**ImageMetadata**](ImageMetadata.md) | Image metadata | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_metadata_templates_delete

> models::InstancePatch200Response instance_metadata_templates_delete(name, path, project)
Delete a template file

Removes the template file.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**path** | Option<**String**> | Template name |  |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_metadata_templates_get

> instance_metadata_templates_get(name, project, path)
Get the template file names or a specific

If no path specified, returns a list of template file names. If a path is specified, returns the file content.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |
**path** | Option<**String**> | Template name |  |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_metadata_templates_post

> models::InstancePatch200Response instance_metadata_templates_post(name, path, project)
Create or replace a template file

Creates a new image template file for the instance.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**path** | Option<**String**> | Template name |  |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_patch

> models::InstancePatch200Response instance_patch(name, project, instance)
Partially update the instance

Updates a subset of the instance configuration

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |
**instance** | Option<[**InstancePut**](InstancePut.md)> | Update request |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_post

> models::InstancesPut202Response instance_post(name, project, migration)
Rename or move/migrate an instance

Renames, moves an instance between pools or migrates an instance to another server.  The returned operation metadata will vary based on what's requested. For rename or move within the same server, this is a simple background operation with progress data. For migration, in the push case, this will similarly be a background operation with progress data, for the pull case, it will be a websocket operation with a number of secrets to be passed to the target server.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |
**migration** | Option<[**InstancePost**](InstancePost.md)> | Migration request |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_put

> models::InstancesPut202Response instance_put(name, project, instance)
Update the instance

Updates the instance configuration or trigger a snapshot restore.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |
**instance** | Option<[**InstancePut**](InstancePut.md)> | Update request |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_rebuild_post

> models::InstancePatch200Response instance_rebuild_post(name, instance, project)
Rebuild an instance

Rebuild an instance using an alternate image or as empty.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**instance** | [**InstanceRebuildPost**](InstanceRebuildPost.md) | InstanceRebuild request | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstancePatch200Response**](instance_patch_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_sftp

> instance_sftp(name)
Get the instance SFTP connection

Upgrades the request to an SFTP connection of the instance's filesystem.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_snapshot_delete

> models::InstancesPut202Response instance_snapshot_delete(name, snapshot, project)
Delete a snapshot

Deletes the instance snapshot.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**snapshot** | **String** | Snapshot name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_snapshot_get

> models::InstanceSnapshotGet200Response instance_snapshot_get(name, snapshot, project)
Get the snapshot

Gets a specific instance snapshot.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**snapshot** | **String** | Snapshot name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstanceSnapshotGet200Response**](instance_snapshot_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_snapshot_patch

> models::InstancesPut202Response instance_snapshot_patch(name, snapshot, project, snapshot2)
Partially update snapshot

Updates a subset of the snapshot config.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**snapshot** | **String** | Snapshot name | [required] |
**project** | Option<**String**> | Project name |  |
**snapshot2** | Option<[**InstanceSnapshotPut**](InstanceSnapshotPut.md)> | Snapshot update |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_snapshot_post

> models::InstancesPut202Response instance_snapshot_post(name, snapshot, project, snapshot2)
Rename or move/migrate a snapshot

Renames or migrates an instance snapshot to another server.  The returned operation metadata will vary based on what's requested. For rename or move within the same server, this is a simple background operation with progress data. For migration, in the push case, this will similarly be a background operation with progress data, for the pull case, it will be a websocket operation with a number of secrets to be passed to the target server.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**snapshot** | **String** | Snapshot name | [required] |
**project** | Option<**String**> | Project name |  |
**snapshot2** | Option<[**InstanceSnapshotPost**](InstanceSnapshotPost.md)> | Snapshot migration |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_snapshot_put

> models::InstancesPut202Response instance_snapshot_put(name, snapshot, project, snapshot2)
Update snapshot

Updates the snapshot config.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**snapshot** | **String** | Snapshot name | [required] |
**project** | Option<**String**> | Project name |  |
**snapshot2** | Option<[**InstanceSnapshotPut**](InstanceSnapshotPut.md)> | Snapshot update |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_snapshots_get

> models::InstanceSnapshotsGet200Response instance_snapshots_get(name, project)
Get the snapshots

Returns a list of instance snapshots (URLs).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstanceSnapshotsGet200Response**](instance_snapshots_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_snapshots_get_recursion1

> models::InstanceSnapshotsGetRecursion1200Response instance_snapshots_get_recursion1(name, project)
Get the snapshots

Returns a list of instance snapshots (structs).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstanceSnapshotsGetRecursion1200Response**](instance_snapshots_get_recursion1_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_snapshots_post

> models::InstancesPut202Response instance_snapshots_post(name, project, snapshot)
Create a snapshot

Creates a new snapshot.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |
**snapshot** | Option<[**InstanceSnapshotsPost**](InstanceSnapshotsPost.md)> | Snapshot request |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_state_get

> models::InstanceStateGet200Response instance_state_get(name, project)
Get the runtime state

Gets the runtime state of the instance.  This is a reasonably expensive call as it causes code to be run inside of the instance to retrieve the resource usage and network information.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |

### Return type

[**models::InstanceStateGet200Response**](instance_state_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instance_state_put

> models::InstancesPut202Response instance_state_put(name, project, state)
Change the state

Changes the running state of the instance.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**name** | **String** | Instance name | [required] |
**project** | Option<**String**> | Project name |  |
**state** | Option<[**InstanceStatePut**](InstanceStatePut.md)> | State |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instances_get

> models::InstancesGet200Response instances_get(project, filter, all_projects)
Get the instances

Returns a list of instances (URLs).

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**project** | Option<**String**> | Project name |  |
**filter** | Option<**String**> | Collection filter |  |
**all_projects** | Option<**bool**> | Retrieve instances from all projects |  |

### Return type

[**models::InstancesGet200Response**](instances_get_200_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instances_post

> models::InstancesPut202Response instances_post(project, target)
Create a new instance

Creates a new instance. Depending on the source, this can create an instance from an existing local image, remote image, existing local instance or snapshot, remote migration stream or backup file.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**project** | Option<**String**> | Project name |  |
**target** | Option<**String**> | Cluster member |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


## instances_put

> models::InstancesPut202Response instances_put(project, state)
Bulk instance state update

Changes the running state of all instances.

### Parameters


Name | Type | Description  | Required | Notes
------------- | ------------- | ------------- | ------------- | -------------
**project** | Option<**String**> | Project name |  |
**state** | Option<[**InstancesPut**](InstancesPut.md)> | State |  |

### Return type

[**models::InstancesPut202Response**](instances_put_202_response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

