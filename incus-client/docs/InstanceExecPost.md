# InstanceExecPost

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | Option<**Vec<String>**> | Command and its arguments | [optional]
**cwd** | Option<**String**> | Current working directory for the command | [optional]
**environment** | Option<**std::collections::HashMap<String, String>**> | Additional environment to pass to the command | [optional]
**group** | Option<**i32**> | GID of the user to spawn the command as | [optional]
**height** | Option<**i64**> | Terminal height in rows (for interactive) | [optional]
**interactive** | Option<**bool**> | Whether the command is to be spawned in interactive mode (singled PTY instead of 3 PIPEs) | [optional]
**record_output** | Option<**bool**> | Whether to capture the output for later download (requires non-interactive) | [optional]
**user** | Option<**i32**> | UID of the user to spawn the command as | [optional]
**wait_for_websocket** | Option<**bool**> | Whether to wait for all websockets to be connected before spawning the command | [optional]
**width** | Option<**i64**> | Terminal width in characters (for interactive) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


