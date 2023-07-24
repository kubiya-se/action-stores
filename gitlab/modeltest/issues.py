from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class ListAllIssues(BaseModel):
    assignee_id: Optional[int] = None
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
    in_: Optional[str] = Field(None, alias='in')
    issue_type: Optional[str] = None
    iteration_id: Optional[int] = None
    iteration_title: Optional[str] = None
    labels: Optional[str] = None
    milestone: Optional[str] = None
    milestone_id: Optional[str] = None
    my_reaction_emoji: Optional[str] = None
    non_archived: Optional[bool] = None
    not_: Optional[Dict[str, Any]] = Field(None, alias='not')
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
    id: Union[int, str]
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
class DeleteIssue(BaseModel):
    id: Union[int, str]
    issue_iid: int
class ReorderIssue(BaseModel):
    id: Union[int, str]
    issue_iid: int
    move_after_id: Optional[int] = None
    move_before_id: Optional[int] = None
class MoveIssue(BaseModel):
    id: Union[int, str]
    issue_iid: int
    to_project_id: int
class MoveIssueInput(BaseModel):
    id: Union[int, str]
    issue_iid: int
    to_project_id: int
class CloneIssueInput(BaseModel):
    id: Union[int, str]
    issue_iid: int
    to_project_id: int
    with_notes: Optional[bool] = False
class SubscribeIssueInput(BaseModel):
    id: Union[int, str]
    issue_iid: int
class UnsubscribeIssueInput(BaseModel):
    id: Union[int, str]
    issue_iid: int
class CreateTodoItemInput(BaseModel):
    id: Union[int, str]
    issue_iid: int
class PromoteIssueToEpicInput(BaseModel):
    id: Union[int, str]
    issue_iid: int
    body: str
class UploadMetricImage(BaseModel):
    id: Union[int, str]
    issue_iid: int
    file: str
    url: Optional[str] = Field(None, alias='url')
    url_text: Optional[str] = Field(None, alias='url_text')
class TimeEstimateForAnIssue(BaseModel):
    id: Union[int, str]
    issue_iid: int
    duration: str
class AddSpentTimeForAnIssue(BaseModel):
    id: Union[int, str]
    issue_iid: int
    duration: str
    summary: Optional[str] = None
class IssueIdentifier(BaseModel):
    id: Union[int, str]
    issue_iid: int
class ListMetricImages(BaseModel):
    id: Union[int, str]
    issue_iid: int
class UpdateMetricImage(BaseModel):
    id: Union[int, str]
    issue_iid: int
    image_id: int
    url: Optional[str] = None
    url_text: Optional[str] = None
class DeleteMetricImage(BaseModel):
    id: Union[int, str]
    issue_iid: int
    image_id: int