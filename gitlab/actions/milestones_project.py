from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class ProjectMilestonesGet(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user")
    iids: Optional[List[int]] = None
    state: Optional[str] = None
    title: Optional[str] = None
    search: Optional[str] = None
    include_parent_milestones: Optional[bool] = None
    updated_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None

@action_store.kubiya_action()
def list_project_milestones(input: ProjectMilestonesGet):
    return get_wrapper(endpoint=f"/projects/{input.id}/milestones", args=input.dict(exclude_none=True))

class SingleProjectMilestoneGet(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user")
    milestone_id: int = Field(description="The ID of the project’s milestone")

@action_store.kubiya_action()
def get_single_project_milestone(input: SingleProjectMilestoneGet):
    return get_wrapper(endpoint=f"/projects/{input.id}/milestones/{input.milestone_id}")

class ProjectMilestoneCreate(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user")
    title: str = Field(description="The title of a milestone")
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    start_date: Optional[datetime] = None

@action_store.kubiya_action()
def create_new_project_milestone(input: ProjectMilestoneCreate):
    return post_wrapper(endpoint=f"/projects/{input.id}/milestones", args=input.dict(exclude_none=True))

class ProjectMilestoneUpdate(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user")
    milestone_id: int = Field(description="The ID of the project’s milestone")
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
    state_event: Optional[str] = None

@action_store.kubiya_action()
def edit_project_milestone(input: ProjectMilestoneUpdate):
    return put_wrapper(endpoint=f"/projects/{input.id}/milestones/{input.milestone_id}", args=input.dict(exclude_none=True))

class ProjectMilestoneDelete(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user")
    milestone_id: int = Field(description="The ID of the project’s milestone")

@action_store.kubiya_action()
def delete_project_milestone(input: ProjectMilestoneDelete):
    return delete_wrapper(endpoint=f"/projects/{input.id}/milestones/{input.milestone_id}")

@action_store.kubiya_action()
def get_all_issues_assigned_to_a_single_project_milestone(input: SingleProjectMilestoneGet):
    return get_wrapper(endpoint=f"/projects/{input.id}/milestones/{input.milestone_id}/issues")

@action_store.kubiya_action()
def get_all_merge_requests_assigned_to_a_single_project_milestone(input: SingleProjectMilestoneGet):
    return get_wrapper(endpoint=f"/projects/{input.id}/milestones/{input.milestone_id}/merge_requests")

@action_store.kubiya_action()
def promote_project_milestone_to_a_group_milestone(input: SingleProjectMilestoneGet):
    return post_wrapper(endpoint=f"/projects/{input.id}/milestones/{input.milestone_id}/promote")

@action_store.kubiya_action()
def get_all_burndown_chart_events_for_a_single_milestone(input: SingleProjectMilestoneGet):
    return get_wrapper(endpoint=f"/projects/{input.id}/milestones/{input.milestone_id}/burndown_events")
