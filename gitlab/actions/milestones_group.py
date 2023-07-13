from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field, validator
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from enum import Enum

class MilestoneStates(str, Enum):
    active = "active"
    closed = "closed"

class GroupMilestonesGet(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group owned by the authenticated user")
    iids: Optional[List[int]] = None
    state: Optional[str] = None
    title: Optional[str] = None
    search: Optional[str] = None
    include_parent_milestones: Optional[bool] = None
    updated_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None

@action_store.kubiya_action()
def list_group_milestones(input: GroupMilestonesGet):
    return get_wrapper(endpoint=f"/groups/{input.id}/milestones", args=input.dict(exclude_none=True))

class SingleGroupMilestoneGet(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group owned by the authenticated user")
    milestone_id: int = Field(description="The ID of a group milestone")

@action_store.kubiya_action()
def get_single_group_milestone(input: SingleGroupMilestoneGet):
    return get_wrapper(endpoint=f"/groups/{input.id}/milestones/{input.milestone_id}")

class GroupMilestoneCreate(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group owned by the authenticated user")
    title: str = Field(description="The title of a milestone")
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    start_date: Optional[datetime] = None

@action_store.kubiya_action()
def create_new_group_milestone(input: GroupMilestoneCreate):
    return post_wrapper(endpoint=f"/groups/{input.id}/milestones", args=input.dict(exclude_none=True))

class GroupMilestoneUpdate(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group owned by the authenticated user")
    milestone_id: int = Field(description="The ID of a group milestone")
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
    state_event: Optional[str] = None

@action_store.kubiya_action()
def edit_group_milestone(input: GroupMilestoneUpdate):
    return put_wrapper(endpoint=f"/groups/{input.id}/milestones/{input.milestone_id}", args=input.dict(exclude_none=True))

class GroupMilestoneDelete(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group owned by the authenticated user")
    milestone_id: int = Field(description="The ID of the group’s milestone")

@action_store.kubiya_action()
def delete_group_milestone(input: GroupMilestoneDelete):
    return delete_wrapper(endpoint=f"/groups/{input.id}/milestones/{input.milestone_id}")


@action_store.kubiya_action()
def get_all_issues_assigned_to_a_single_group_milestone(input: SingleGroupMilestoneGet):
    return get_wrapper(endpoint=f"/groups/{input.id}/milestones/{input.milestone_id}/issues")

@action_store.kubiya_action()
def get_all_merge_requests_assigned_to_a_single_group_milestone(input: SingleGroupMilestoneGet):
    return get_wrapper(endpoint=f"/groups/{input.id}/milestones/{input.milestone_id}/merge_requests")

@action_store.kubiya_action()
def get_all_burndown_chart_events_for_a_single_group_milestone(input: SingleGroupMilestoneGet):
    return get_wrapper(endpoint=f"/groups/{input.id}/milestones/{input.milestone_id}/burndown_events")
