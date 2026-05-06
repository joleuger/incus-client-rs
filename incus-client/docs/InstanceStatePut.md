# InstanceStatePut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | Option<**String**> | State change action (start, stop, restart, freeze, unfreeze) | [optional]
**force** | Option<**bool**> | Whether to force the action (for stop and restart) | [optional]
**stateful** | Option<**bool**> | Whether to store the runtime state (for stop) | [optional]
**timeout** | Option<**i64**> | How long to wait (in s) before giving up (when force isn't set) | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


