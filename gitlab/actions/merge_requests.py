from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.merge_requests import *

@action_store.kubiya_action()
def list_merge_requests(input: ListMergeRequests):
    return get_wrapper(endpoint='/merge_requests', args=input.dict(exclude_none=True, by_alias=True))
@action_store.kubiya_action()
def list_project_merge_requests(input: ListProjectMergeRequests):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests', args=input.dict(exclude_none=True, by_alias=True))
@action_store.kubiya_action()
def list_group_merge_requests(input: ListGroupMergeRequests):
    return get_wrapper(endpoint=f'/groups/{input.id}/merge_requests', args=input.dict(exclude_none=True, by_alias=True))
@action_store.kubiya_action()
def get_single_mr(input: GetSingleMR):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_merge_request_participants(input: GetMergeRequestParticipants):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/participants')
@action_store.kubiya_action()
def get_merge_request_commits(input: GetMergeRequestCommits):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/commits')
@action_store.kubiya_action()
def get_merge_request_changes(input: GetMergeRequestChanges):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/changes', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_merge_request_diffs(input: ListMergeRequestDiffs):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/diffs', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_merge_request_pipelines(input: ListMergeRequestPipelines):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/pipelines')
@action_store.kubiya_action()
def create_merge_request_pipeline(input: CreateMergeRequestPipeline):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/pipelines', args=input.dict())
@action_store.kubiya_action()
def create_new_merge_request(input: ProjectsMergeRequestCreate):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_merge_request(input: UpdateMergeRequest):
    return put_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_merge_request(input: DeleteMergeRequest):
    return delete_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def merge_merge_request(input: MergeMergeRequest):
    return put_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/merge', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def merge_to_default_merge_ref_path(input: MergeToDefaultMergeRefPath):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/merge_ref', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def cancel_merge_when_pipeline_succeeds(input: CancelMergeWhenPipelineSucceeds):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/cancel_merge_when_pipeline_succeeds', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def rebase_merge_request(input: RebaseMergeRequest):
    return put_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/rebase', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_issues_that_close_on_merge(input: ListIssuesThatCloseOnMerge):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/closes_issues', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def subscribe_merge_request(input: SubscribeMergeRequest):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/subscribe', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def unsubscribe_merge_request(input: UnsubscribeMergeRequest):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/unsubscribe', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_todo_item(input: CreateTodoItem):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/todo', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_merge_request_diff_versions(input: GetMergeRequestDiffVersions):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/versions', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_single_merge_request_diff_version(input: GetSingleMergeRequestDiffVersion):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/versions/{input.version_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def set_time_estimate_for_merge_request(input: SetTimeEstimateMergeRequest):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/time_estimate', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def reset_time_estimate_for_merge_request(input: ResetTimeEstimateMergeRequest):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/reset_time_estimate', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def add_spent_time_for_merge_request(input: AddSpentTimeMergeRequest):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/add_spent_time', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def reset_spent_time_for_merge_request(input: ResetSpentTimeMergeRequest):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/reset_spent_time', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_time_tracking_stats_merge_request(input: GetTimeTrackingStatsMergeRequest):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/time_stats', args=input.dict(exclude_none=True))