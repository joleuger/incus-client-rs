# Operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class** | Option<**String**> | Type of operation (task, token or websocket) | [optional]
**created_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | Operation creation time | [optional]
**description** | Option<**String**> | Description of the operation | [optional]
**err** | Option<**String**> | Operation error message | [optional]
**id** | Option<**String**> | UUID of the operation | [optional]
**location** | Option<**String**> | What cluster member this record was found on | [optional]
**may_cancel** | Option<**bool**> | Whether the operation can be canceled | [optional]
**metadata** | Option<**std::collections::HashMap<String, serde_json::Value>**> | Operation specific metadata | [optional]
**resources** | Option<[**std::collections::HashMap<String, Vec<String>>**](Vec.md)> | Affected resources | [optional]
**status** | Option<**String**> | Status name | [optional]
**status_code** | Option<**i64**> |  | [optional]
**updated_at** | Option<**chrono::DateTime<chrono::FixedOffset>**> | Operation last change | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


