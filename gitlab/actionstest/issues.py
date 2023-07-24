from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.issues import *
@action_store.kubiya_action()
def list_all_issues(input: ListAllIssues):
    return get_wrapper(endpoint='/issues', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_all_group_issues(input: ListAllGroupIssues):
    return get_wrapper(endpoint=f'/groups/{input.id}/issues', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def new_issue(input: CreateProjectIssue):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_project_issue(input: UpdateProjectIssue):
    return put_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_issue(input: DeleteIssue):
    return delete_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}')
@action_store.kubiya_action()
def reorder_issue(input: ReorderIssue):
    return put_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/reorder', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def move_issue(input: MoveIssue):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/move', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def move_issue(input: MoveIssueInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/move', data=input.dict())
@action_store.kubiya_action()
def clone_issue(input: CloneIssueInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/clone', data=input.dict())
@action_store.kubiya_action()
def subscribe_issue(input: SubscribeIssueInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/subscribe')
@action_store.kubiya_action()
def unsubscribe_issue(input: UnsubscribeIssueInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/unsubscribe')
@action_store.kubiya_action()
def create_todo_item(input: CreateTodoItemInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/todo')
@action_store.kubiya_action()
def promote_issue_to_epic(input: PromoteIssueToEpicInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/notes', data=input.dict())
@action_store.kubiya_action()
def upload_metric_image(input: UploadMetricImage):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/metric_images', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def set_time_estimate_for_an_issue(input: TimeEstimateForAnIssue):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/time_estimate', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def reset_time_estimate_for_an_issue(input: IssueIdentifier):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/reset_time_estimate')
@action_store.kubiya_action()
def add_spent_time_for_an_issue(input: AddSpentTimeForAnIssue):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/add_spent_time', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def reset_spent_time_for_an_issue(input: IssueIdentifier):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/reset_spent_time')
@action_store.kubiya_action()
def get_time_tracking_stats(input: IssueIdentifier):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/time_stats')
@action_store.kubiya_action()
def list_related_merge_requests(input: IssueIdentifier):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/related_merge_requests')
@action_store.kubiya_action()
def list_merge_requests_that_close_issue(input: IssueIdentifier):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/closed_by')
@action_store.kubiya_action()
def get_issue_participants(input: IssueIdentifier):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/participants')
@action_store.kubiya_action()
def get_user_agent_details(input: IssueIdentifier):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/user_agent_detail')
@action_store.kubiya_action()
def upload_metric_image(input: UploadMetricImage):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/metric_images', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_metric_images(input: ListMetricImages):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/metric_images')
@action_store.kubiya_action()
def update_metric_image(input: UpdateMetricImage):
    return put_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/metric_images/{input.image_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_metric_image(input: DeleteMetricImage):
    return delete_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/metric_images/{input.image_id}')