from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class ProjectResourceGroups(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")

@action_store.kubiya_action()
def get_all_resource_group_for_a_project(input: ProjectResourceGroups):
    return get_wrapper(endpoint=f"/projects/{input.id}/resource_groups")

class SingleResourceGroup(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    key: str = Field(description="The key of the resource group.")

@action_store.kubiya_action()
def get_a_specific_resource_group(input: SingleResourceGroup):
    return get_wrapper(endpoint=f"/projects/{input.id}/resource_groups/{input.key}")

class ResourceGroupUpcomingJobs(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    key: str = Field(description="The key of the resource group.")

@action_store.kubiya_action()
def list_upcoming_jobs_for_a_specific_resource_group(input: ResourceGroupUpcomingJobs):
    return get_wrapper(endpoint=f"/projects/{input.id}/resource_groups/{input.key}/upcoming_jobs")

class UpdateResourceGroup(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    key: str = Field(description="The key of the resource group.")
    process_mode: Optional[str] = Field(None, description="The process mode of the resource group. One of unordered, oldest_first or newest_first.")

@action_store.kubiya_action()
def edit_an_existing_resource_group(input: UpdateResourceGroup):
    return put_wrapper(endpoint=f"/projects/{input.id}/resource_groups/{input.key}", args=input.dict(exclude_none=True))
