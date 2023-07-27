from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class NotMatch(BaseModel):
    author_id: Optional[int] = Field(None, description='Can exclude by author ID')
    author_username: Optional[str] = Field(None, description='Can exclude by author username (GitLab 14.7 and later)')
    labels: Optional[str] = Field(None, description='Can exclude by labels')
class GroupsIdEpics(BaseModel):
    id: Union[int, str]
    author_id: Optional[int] = None
    author_username: Optional[str] = None
    labels: Optional[str] = None
    with_labels_details: Optional[bool] = None
    order_by: Optional[str] = None
    sort: Optional[str] = None
    search: Optional[str] = None
    state: Optional[str] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    include_ancestor_groups: Optional[bool] = None
    include_descendant_groups: Optional[bool] = None
    my_reaction_emoji: Optional[str] = None
    not_: Optional[NotMatch] = Field(None, alias='not', description='Return epics that do not match the parameters supplied')
class SingleEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class NewEpicInput(BaseModel):
    id: Union[int, str]
    title: str
    labels: Optional[str]
    description: Optional[str]
    color: Optional[str]
    confidential: Optional[bool]
    created_at: Optional[datetime]
    start_date_is_fixed: Optional[bool]
    start_date_fixed: Optional[str]
    due_date_is_fixed: Optional[bool]
    due_date_fixed: Optional[str]
    parent_id: Optional[Union[int, str]]
class UpdateEpic(BaseModel):
    id: int
    epic_iid: int
    add_labels: Optional[str] = None
    confidential: Optional[bool] = None
    description: Optional[str] = None
    due_date_fixed: Optional[str] = None
    due_date_is_fixed: Optional[bool] = None
    labels: Optional[str] = None
    parent_id: Optional[int] = None
    remove_labels: Optional[str] = None
    start_date_fixed: Optional[str] = None
    start_date_is_fixed: Optional[bool] = None
    state_event: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
class DeleteEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class CreateAToDoItem(BaseModel):
    id: Union[int, str]
    epic_iid: int