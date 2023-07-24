
from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class RunnerFilter(BaseModel):
    scope: Optional[str] = Field(None, description="Deprecated: Use type or status instead.")
    type: Optional[str] = Field(None, description="The type of runners to return.")
    status: Optional[str] = Field(None, description="The status of runners to return.")
    paused: Optional[bool] = Field(None, description="Whether to include only runners that are accepting or ignoring new jobs.")
    tag_list: Optional[List[str]] = Field(None, description="A list of runner tags.")

@action_store.kubiya_action()
def list_owned_runners(input: RunnerFilter):
    return get_wrapper(endpoint="/runners", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def list_all_runners(input: RunnerFilter):
    return get_wrapper(endpoint="/runners/all", args=input.dict(exclude_none=True))

class RunnerId(BaseModel):
    id: int = Field(description="The ID of a runner.")

@action_store.kubiya_action()
def get_runner_details(input: RunnerId):
    return get_wrapper(endpoint=f"/runners/{input.id}")

class RunnerUpdate(BaseModel):
    id: int = Field(description="The ID of a runner.")
    description: Optional[str] = Field(None, description="The description of the runner.")
    active: Optional[bool] = Field(None, description="Deprecated: Use paused instead.")
    paused: Optional[bool] = Field(None, description="Specifies if the runner should ignore new jobs.")
    tag_list: Optional[List[str]] = Field(None, description="The list of tags for the runner.")
    run_untagged: Optional[bool] = Field(None, description="Specifies if the runner can execute untagged jobs.")
    locked: Optional[bool] = Field(None, description="Specifies if the runner is locked.")
    access_level: Optional[str] = Field(None, description="The access level of the runner.")
    maximum_timeout: Optional[int] = Field(None, description="Maximum timeout that limits the amount of time (in seconds) that runners can run jobs.")

@action_store.kubiya_action()
def update_runner_details(input: RunnerUpdate):
    return put_wrapper(endpoint=f"/runners/{input.id}", args=input.dict(exclude_none=True))

class RunnerPause(BaseModel):
    runner_id: int = Field(description="The ID of a runner.")
    paused: bool = Field(description="Specifies if the runner should ignore new jobs.")

@action_store.kubiya_action()
def pause_runner(input: RunnerPause):
    return put_wrapper(endpoint=f"/runners/{input.runner_id}", args=input.dict(exclude_none=True))

class RunnerJobsFilter(BaseModel):
    id: int = Field(description="The ID of a runner.")
    status: Optional[str] = Field(None, description="Status of the job.")
    order_by: Optional[str] = Field(None, description="Order jobs by id.")
    sort: Optional[str] = Field(None, description="Sort jobs in asc or desc order (default: desc).")

@action_store.kubiya_action()
def list_runner_jobs(input: RunnerJobsFilter):
    return get_wrapper(endpoint=f"/runners/{input.id}/jobs", args=input.dict(exclude_none=True))

class ProjectRunnersFilter(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user.")
    scope: Optional[str] = Field(None, description="Deprecated: Use type or status instead.")
    type: Optional[str] = Field(None, description="The type of runners to return.")
    status: Optional[str] = Field(None, description="The status of runners to return.")
    paused: Optional[bool] = Field(None, description="Whether to include only runners that are accepting or ignoring new jobs.")
    tag_list: Optional[List[str]] = Field(None, description="A list of runner tags.")

@action_store.kubiya_action()
def list_project_runners(input: ProjectRunnersFilter):
    return get_wrapper(endpoint=f"/projects/{input.id}/runners", args=input.dict(exclude_none=True))

class EnableRunnerInProject(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user.")
    runner_id: int = Field(description="The ID of a runner.")

@action_store.kubiya_action()
def enable_runner_in_project(input: EnableRunnerInProject):
    return post_wrapper(endpoint=f"/projects/{input.id}/runners", args=input.dict(exclude_none=True))
class DisableRunnerFromProject(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user.")
    runner_id: int = Field(description="The ID of a runner.")

@action_store.kubiya_action()
def disable_runner_from_project(input: DisableRunnerFromProject):
    return delete_wrapper(endpoint=f"/projects/{input.id}/runners/{input.runner_id}")

class GroupRunnersFilter(BaseModel):
    id: int = Field(description="The ID of the group owned by the authenticated user.")
    type: Optional[str] = Field(None, description="The type of runners to return.")
    status: Optional[str] = Field(None, description="The status of runners to return.")
    paused: Optional[bool] = Field(None, description="Whether to include only runners that are accepting or ignoring new jobs.")
    tag_list: Optional[List[str]] = Field(None, description="A list of runner tags.")

@action_store.kubiya_action()
def list_group_runners(input: GroupRunnersFilter):
    return get_wrapper(endpoint=f"/groups/{input.id}/runners", args=input.dict(exclude_none=True))

class RegisterRunner(BaseModel):
    token: str = Field(description="Registration token.")
    description: Optional[str] = Field(None, description="Description of the runner.")
    info: Optional[dict] = Field(None, description="Runner’s metadata.")
    active: Optional[bool] = Field(None, description="Deprecated: Use paused instead.")
    paused: Optional[bool] = Field(None, description="Specifies if the runner should ignore new jobs.")
    locked: Optional[bool] = Field(None, description="Specifies if the runner should be locked for the current project.")
    run_untagged: Optional[bool] = Field(None, description="Specifies if the runner should handle untagged jobs.")
    tag_list: Optional[List[str]] = Field(None, description="A list of runner tags.")
    access_level: Optional[str] = Field(None, description="The access level of the runner.")
    maximum_timeout: Optional[int] = Field(None, description="Maximum timeout that limits the amount of time (in seconds) that runners can run jobs.")
    maintainer_note: Optional[str] = Field(None, description="Deprecated, see maintenance_note.")
    maintenance_note: Optional[str] = Field(None, description="Free-form maintenance notes for the runner (1024 characters).")

@action_store.kubiya_action()
def register_new_runner(input: RegisterRunner):
    return post_wrapper(endpoint="/runners", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def delete_runner_by_id(input: RunnerId):
    return delete_wrapper(endpoint=f"/runners/{input.id}")

class RunnerToken(BaseModel):
    token: str = Field(description="The runner’s authentication token.")

@action_store.kubiya_action()
def delete_runner_by_token(input: RunnerToken):
    return delete_wrapper(endpoint="/runners", args=input.dict(exclude_none=True))

class VerifyRunnerAuthentication(BaseModel):
    token: str = Field(description="The runner’s authentication token.")
    system_id: Optional[str] = Field(None, description="The runner’s system identifier.")

@action_store.kubiya_action()
def verify_runner_authentication(input: VerifyRunnerAuthentication):
    return post_wrapper(endpoint="/runners/verify", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def reset_instance_runner_registration_token():
    return post_wrapper(endpoint="/runners/reset_registration_token")

class ProjectId(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user.")

@action_store.kubiya_action()
def reset_project_runner_registration_token(input: ProjectId):
    return post_wrapper(endpoint=f"/projects/{input.id}/runners/reset_registration_token")

@action_store.kubiya_action()
def reset_group_runner_registration_token(input: ProjectId):
    return post_wrapper(endpoint=f"/groups/{input.id}/runners/reset_registration_token")

@action_store.kubiya_action()
def reset_runner_authentication_token_by_id(input: RunnerId):
    return post_wrapper(endpoint=f"/runners/{input.id}/reset_authentication_token")

@action_store.kubiya_action()
def reset_runner_authentication_token_by_token(input: RunnerToken):
    return post_wrapper(endpoint="/runners/reset_authentication_token", args=input.dict(exclude_none=True))
