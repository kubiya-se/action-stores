
from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class ListAllIssues(BaseModel):
    assignee_id: Optional[int] = None #
    assignee_username: Optional[List[str]] = None
    author_id: Optional[int] = None
    author_username: Optional[str] = None
    confidential: Optional[bool] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    due_date: Optional[str] = None
    epic_id: Optional[int] = None
    health_status: Optional[str] = None
    iids: Optional[List[int]] = None
    in_: Optional[str] = Field(None, alias="in")
    issue_type: Optional[str] = None
    iteration_id: Optional[int] = None
    iteration_title: Optional[str] = None
    labels: Optional[str] = None
    milestone: Optional[str] = None
    milestone_id: Optional[str] = None
    my_reaction_emoji: Optional[str] = None
    non_archived: Optional[bool] = None
    not_: Optional[Dict[str, Any]] = Field(None, alias="not")
    order_by: Optional[str] = None
    scope: Optional[str] = None
    search: Optional[str] = None
    sort: Optional[str] = None
    state: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    weight: Optional[int] = None
    with_labels_details: Optional[bool] = None


class ListAllGroupIssues(ListAllIssues):
    id: Union[int, str]  # The global ID or URL-encoded path of the group owned by the authenticated user

@action_store.kubiya_action()
def list_all_issues(input: ListAllIssues):
    return get_wrapper(endpoint="/issues", args=input.dict(exclude_none=True))


@action_store.kubiya_action()
def list_all_group_issues(input: ListAllGroupIssues):
    return get_wrapper(endpoint=f"/groups/{input.id}/issues", args=input.dict(exclude_none=True))

class CreateProjectIssue(BaseModel):
    id: Union[int, str]
    assignee_id: Optional[int] = None
    assignee_ids: Optional[List[int]] = None
    confidential: Optional[bool] = None
    created_at: Optional[str] = None
    description: Optional[str] = None
    discussion_to_resolve: Optional[str] = None
    due_date: Optional[str] = None
    epic_id: Optional[int] = None
    title: str
    weight: Optional[int] = None

@action_store.kubiya_action()
def new_issue(input: CreateProjectIssue):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues", args=input.dict(exclude_none=True))

class UpdateProjectIssue(BaseModel):
    id: Union[int, str]
    issue_iid: int
    add_labels: Optional[str] = None
    assignee_ids: Optional[List[int]] = None
    confidential: Optional[bool] = None
    description: Optional[str] = None
    discussion_locked: Optional[bool] = None
    due_date: Optional[str] = None
    epic_id: Optional[int] = None

@action_store.kubiya_action()
def update_project_issue(input: UpdateProjectIssue):
    return put_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}", args=input.dict(exclude_none=True))

class DeleteIssue(BaseModel):
    id: Union[int, str]
    issue_iid: int

@action_store.kubiya_action()
def delete_issue(input: DeleteIssue):
    return delete_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}")

class ReorderIssue(BaseModel):
    id: Union[int, str]
    issue_iid: int
    move_after_id: Optional[int] = None
    move_before_id: Optional[int] = None

@action_store.kubiya_action()
def reorder_issue(input: ReorderIssue):
    return put_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/reorder", args=input.dict(exclude_none=True))

class MoveIssue(BaseModel):
    id: Union[int, str]
    issue_iid: int
    to_project_id: int

@action_store.kubiya_action()
def move_issue(input: MoveIssue):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/move", args=input.dict(exclude_none=True))


class MoveIssueInput(BaseModel):
    id: Union[int, str]
    issue_iid: int
    to_project_id: int


@action_store.kubiya_action()
def move_issue(input: MoveIssueInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/move", data=input.dict())


class CloneIssueInput(BaseModel):
    id: Union[int, str]
    issue_iid: int
    to_project_id: int
    with_notes: Optional[bool] = False


@action_store.kubiya_action()
def clone_issue(input: CloneIssueInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/clone", data=input.dict())


class SubscribeIssueInput(BaseModel):
    id: Union[int, str]
    issue_iid: int


@action_store.kubiya_action()
def subscribe_issue(input: SubscribeIssueInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/subscribe")


class UnsubscribeIssueInput(BaseModel):
    id: Union[int, str]
    issue_iid: int


@action_store.kubiya_action()
def unsubscribe_issue(input: UnsubscribeIssueInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/unsubscribe")


class CreateTodoItemInput(BaseModel):
    id: Union[int, str]
    issue_iid: int


@action_store.kubiya_action()
def create_todo_item(input: CreateTodoItemInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/todo")


class PromoteIssueToEpicInput(BaseModel):
    id: Union[int, str]
    issue_iid: int
    body: str


@action_store.kubiya_action()
def promote_issue_to_epic(input: PromoteIssueToEpicInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/notes", data=input.dict())


class UploadMetricImage(BaseModel):
    id: Union[int,str]
    issue_iid: int
    file: str
    url: Optional[str] = Field(None, alias='url')
    url_text: Optional[str] = Field(None, alias='url_text')

class TimeEstimateForAnIssue(BaseModel):
    id: Union[int,str]
    issue_iid: int
    duration: str

class AddSpentTimeForAnIssue(BaseModel):
    id: Union[int,str]
    issue_iid: int
    duration: str
    summary: Optional[str] = None

class IssueIdentifier(BaseModel):
    id: Union[int,str]
    issue_iid: int


@action_store.kubiya_action()
def upload_metric_image(input: UploadMetricImage):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/metric_images", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def set_time_estimate_for_an_issue(input: TimeEstimateForAnIssue):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/time_estimate", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def reset_time_estimate_for_an_issue(input: IssueIdentifier):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/reset_time_estimate")

@action_store.kubiya_action()
def add_spent_time_for_an_issue(input: AddSpentTimeForAnIssue):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/add_spent_time", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def reset_spent_time_for_an_issue(input: IssueIdentifier):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/reset_spent_time")

@action_store.kubiya_action()
def get_time_tracking_stats(input: IssueIdentifier):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/time_stats")

@action_store.kubiya_action()
def list_related_merge_requests(input: IssueIdentifier):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/related_merge_requests")

@action_store.kubiya_action()
def list_merge_requests_that_close_issue(input: IssueIdentifier):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/closed_by")

@action_store.kubiya_action()
def get_issue_participants(input: IssueIdentifier):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/participants")

@action_store.kubiya_action()
def get_user_agent_details(input: IssueIdentifier):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/user_agent_detail")

@action_store.kubiya_action()
def upload_metric_image(input: UploadMetricImage):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/metric_images", args=input.dict(exclude_none=True))


class ListMetricImages(BaseModel):
    id: Union[int,str]
    issue_iid: int

@action_store.kubiya_action()
def list_metric_images(input: ListMetricImages):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/metric_images")

class UpdateMetricImage(BaseModel):
    id: Union[int,str]
    issue_iid: int
    image_id: int
    url: Optional[str] = None
    url_text: Optional[str] = None

@action_store.kubiya_action()
def update_metric_image(input: UpdateMetricImage):
    return put_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/metric_images/{input.image_id}", args=input.dict(exclude_none=True))


class DeleteMetricImage(BaseModel):
    id: Union[int,str]
    issue_iid: int
    image_id: int

@action_store.kubiya_action()
def delete_metric_image(input: DeleteMetricImage):
    return delete_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/metric_images/{input.image_id}")