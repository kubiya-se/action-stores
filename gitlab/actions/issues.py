from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime
from ..models.issues import *

from .. import action_store as action_store
from ..http_wrapper import *

@action_store.kubiya_action()
def list_all_issues(input: ListAllIssues):
    response =  get_wrapper(endpoint='/issues', args=input.dict(exclude_none=True))
    return Issues(issues=response)

@action_store.kubiya_action()
def get_single_issue(input: ListSingleIssue):
    response =  get_wrapper(endpoint='/issues/{id}', args=input.dict(exclude_none=True))
    return SingleIssue(issues=response)

@action_store.kubiya_action()
def list_all_group_issues(input: ListAllGroupIssues):
    response =  get_wrapper(endpoint=f'/groups/{input.id}/issues', args=input.dict(exclude_none=True))
    return Issues(issues=response)

@action_store.kubiya_action()
def edit_issue(input: EditIssue):
    response = put_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}', args=input.dict(exclude_none=True))
    return SingleIssue(issues=response)

@action_store.kubiya_action()
def new_issue(input: CreateProjectIssue):
    response =  post_wrapper(endpoint=f'/projects/{input.id}/issues', args=input.dict(exclude_none=True))
    return SingleIssue(issues=response)

@action_store.kubiya_action()
def update_project_issue(input: UpdateProjectIssue):
    response =  put_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}', args=input.dict(exclude_none=True))
    return Issues(issues=response)

@action_store.kubiya_action()
def delete_issue(input: DeleteIssue):
    response =  delete_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}')
    return Issues(issues=response)

@action_store.kubiya_action()
def reorder_issue(input: ReorderIssue):
    response =  put_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/reorder', args=input.dict(exclude_none=True))
    return Issues(issues=response)

@action_store.kubiya_action()
def move_issue(input: MoveIssueInput):
    response =  post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/move', data=input.dict())
    return Issues(issues=response)

@action_store.kubiya_action()
def clone_issue(input: CloneIssueInput):
    response =  post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/clone', data=input.dict())
    return Issues(issues=response)

@action_store.kubiya_action()
def subscribe_issue(input: SubscribeIssueInput):
    response =  post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/subscribe')
    return Issues(issues=response)

@action_store.kubiya_action()
def unsubscribe_issue(input: UnsubscribeIssueInput):
    response =  post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/unsubscribe')
    return Issues(issues=response)

@action_store.kubiya_action()
def create_todo_item(input: CreateTodoItemInput):
    response =  post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/todo')
    return Issues(issues=response)

@action_store.kubiya_action()
def promote_issue_to_epic(input: PromoteIssueToEpicInput):
    response =  post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/notes', data=input.dict())
    return Issues(issues=response)

# @action_store.kubiya_action()
# def upload_metric_image(input: UploadMetricImage):
#     response =  post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/metric_images', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def set_time_estimate_for_an_issue(input: TimeEstimateForAnIssue):
    response =  post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/time_estimate', args=input.dict(exclude_none=True))
    return Issues(issues=response)

@action_store.kubiya_action()
def reset_time_estimate_for_an_issue(input: IssueIdentifier):
    response =  post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/reset_time_estimate')
    return Issues(issues=response)

@action_store.kubiya_action()
def add_spent_time_for_an_issue(input: AddSpentTimeForAnIssue):
    response =  post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/add_spent_time', args=input.dict(exclude_none=True))
    return Issues(issues=response)

@action_store.kubiya_action()
def reset_spent_time_for_an_issue(input: IssueIdentifier):
    response =  post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/reset_spent_time')
    return Issues(issues=response)

@action_store.kubiya_action()
def get_time_tracking_stats(input: IssueIdentifier):
    response =  get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/time_stats')
    return Issues(issues=response)

@action_store.kubiya_action()
def list_related_merge_requests(input: IssueIdentifier):
    response =  get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/related_merge_requests')
    return Issues(issues=response)

@action_store.kubiya_action()
def list_merge_requests_that_close_issue(input: IssueIdentifier):
    response =  get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/closed_by')
    return Issues(issues=response)

@action_store.kubiya_action()
def get_issue_participants(input: IssueIdentifier):
    response =  get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/participants')
    return Issues(issues=response)

# @action_store.kubiya_action()
# def get_user_agent_details(input: IssueIdentifier):
#     response =  get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/user_agent_detail')
#     return Issues(issues=response)

# @action_store.kubiya_action()
# def upload_metric_image(input: UploadMetricImage):
#     response =  post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/metric_images', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def list_metric_images(input: ListMetricImages):
#     response =  get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/metric_images')
# @action_store.kubiya_action()
# def update_metric_image(input: UpdateMetricImage):
#     response =  put_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/metric_images/{input.image_id}', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def delete_metric_image(input: DeleteMetricImage):
#     response =  delete_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/metric_images/{input.image_id}')