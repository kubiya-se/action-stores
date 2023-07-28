from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class RunnerFilter(BaseModel):
    scope: Optional[str] = Field(None, description='Deprecated: Use type or status instead.')
    type: Optional[str] = Field(None, description='The type of runners to return.')
    status: Optional[str] = Field(None, description='The status of runners to return.')
    paused: Optional[bool] = Field(None, description='Whether to include only runners that are accepting or ignoring new jobs.')
    tag_list: Optional[List[str]] = Field(None, description='A list of runner tags.')
class RunnerId(BaseModel):
    id: int = Field(description='The ID of a runner.')
class RunnerUpdate(BaseModel):
    id: int = Field(description='The ID of a runner.')
    description: Optional[str] = Field(None, description='The description of the runner.')
    active: Optional[bool] = Field(None, description='Deprecated: Use paused instead.')
    paused: Optional[bool] = Field(None, description='Specifies if the runner should ignore new jobs.')
    tag_list: Optional[List[str]] = Field(None, description='The list of tags for the runner.')
    run_untagged: Optional[bool] = Field(None, description='Specifies if the runner can execute untagged jobs.')
    locked: Optional[bool] = Field(None, description='Specifies if the runner is locked.')
    access_level: Optional[str] = Field(None, description='The access level of the runner.')
    maximum_timeout: Optional[int] = Field(None, description='Maximum timeout that limits the amount of time (in seconds) that runners can run jobs.')
class RunnerPause(BaseModel):
    runner_id: int = Field(description='The ID of a runner.')
    paused: bool = Field(description='Specifies if the runner should ignore new jobs.')
class RunnerJobsFilter(BaseModel):
    id: int = Field(description='The ID of a runner.')
    status: Optional[str] = Field(None, description='Status of the job.')
    order_by: Optional[str] = Field(None, description='Order jobs by id.')
    sort: Optional[str] = Field(None, description='Sort jobs in asc or desc order (default: desc).')
class ProjectRunnersFilter(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    scope: Optional[str] = Field(None, description='Deprecated: Use type or status instead.')
    type: Optional[str] = Field(None, description='The type of runners to return.')
    status: Optional[str] = Field(None, description='The status of runners to return.')
    paused: Optional[bool] = Field(None, description='Whether to include only runners that are accepting or ignoring new jobs.')
    tag_list: Optional[List[str]] = Field(None, description='A list of runner tags.')
class EnableRunnerInProject(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    runner_id: int = Field(description='The ID of a runner.')
class DisableRunnerFromProject(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    runner_id: int = Field(description='The ID of a runner.')
class GroupRunnersFilter(BaseModel):
    id: int = Field(description='The ID of the group owned by the authenticated user.')
    type: Optional[str] = Field(None, description='The type of runners to return.')
    status: Optional[str] = Field(None, description='The status of runners to return.')
    paused: Optional[bool] = Field(None, description='Whether to include only runners that are accepting or ignoring new jobs.')
    tag_list: Optional[List[str]] = Field(None, description='A list of runner tags.')
class RegisterRunner(BaseModel):
    token: str = Field(description='Registration token.')
    description: Optional[str] = Field(None, description='Description of the runner.')
    info: Optional[dict] = Field(None, description='Runner’s metadata.')
    active: Optional[bool] = Field(None, description='Deprecated: Use paused instead.')
    paused: Optional[bool] = Field(None, description='Specifies if the runner should ignore new jobs.')
    locked: Optional[bool] = Field(None, description='Specifies if the runner should be locked for the current project.')
    run_untagged: Optional[bool] = Field(None, description='Specifies if the runner should handle untagged jobs.')
    tag_list: Optional[List[str]] = Field(None, description='A list of runner tags.')
    access_level: Optional[str] = Field(None, description='The access level of the runner.')
    maximum_timeout: Optional[int] = Field(None, description='Maximum timeout that limits the amount of time (in seconds) that runners can run jobs.')
    maintainer_note: Optional[str] = Field(None, description='Deprecated, see maintenance_note.')
    maintenance_note: Optional[str] = Field(None, description='Free-form maintenance notes for the runner (1024 characters).')
class RunnerToken(BaseModel):
    token: str = Field(description='The runner’s authentication token.')
class VerifyRunnerAuthentication(BaseModel):
    token: str = Field(description='The runner’s authentication token.')
    system_id: Optional[str] = Field(None, description='The runner’s system identifier.')
class ProjectId(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')