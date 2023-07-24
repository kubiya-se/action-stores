from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class GetAllPipelineSchedulesInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    scope: Optional[str] = Field(None, description="The scope of pipeline schedules, must be one of: active, inactive.")

@action_store.kubiya_action()
def get_all_pipeline_schedules(input: GetAllPipelineSchedulesInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/pipeline_schedules", args=input.dict(exclude_none=True))

class GetSinglePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_schedule_id: int = Field(..., description="The pipeline schedule ID.")

@action_store.kubiya_action()
def get_single_pipeline_schedule(input: GetSinglePipelineScheduleInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}")

class GetPipelinesTriggeredByScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_schedule_id: int = Field(..., description="The pipeline schedule ID.")

@action_store.kubiya_action()
def get_pipelines_triggered_by_schedule(input: GetPipelinesTriggeredByScheduleInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}/pipelines")

class CreateNewPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    description: str = Field(..., description="The description of the pipeline schedule.")
    ref: str = Field(..., description="The branch or tag name that is triggered.")
    cron: str = Field(..., description="The cron schedule, for example: 0 1 * * *.")
    cron_timezone: Optional[str] = Field(None, description="The time zone supported by ActiveSupport::TimeZone, for example: Pacific Time (US & Canada) (default: UTC).")
    active: Optional[bool] = Field(None, description="The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated (default: true).")

@action_store.kubiya_action()
def create_new_pipeline_schedule(input: CreateNewPipelineScheduleInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/pipeline_schedules", args=input.dict(exclude_none=True))

class EditPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_schedule_id: int = Field(..., description="The pipeline schedule ID.")
    description: Optional[str] = Field(None, description="The description of the pipeline schedule.")
    ref: Optional[str] = Field(None, description="The branch or tag name that is triggered.")
    cron: Optional[str] = Field(None, description="The cron schedule, for example: 0 1 * * *.")
    cron_timezone: Optional[str] = Field(None, description="The time zone supported by ActiveSupport::TimeZone (for example Pacific Time (US & Canada)), or TZInfo::Timezone (for example America/Los_Angeles).")
    active: Optional[bool] = Field(None, description="The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated.")

@action_store.kubiya_action()
def edit_pipeline_schedule(input: EditPipelineScheduleInput):
    return put_wrapper(endpoint=f"/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}", args=input.dict(exclude_none=True))

class TakeOwnershipOfPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_schedule_id: int = Field(..., description="The pipeline schedule ID.")

@action_store.kubiya_action()
def take_ownership_of_pipeline_schedule(input: TakeOwnershipOfPipelineScheduleInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}/take_ownership")

class DeletePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_schedule_id: int = Field(..., description="The pipeline schedule ID.")

@action_store.kubiya_action()
def delete_pipeline_schedule(input: DeletePipelineScheduleInput):
    return delete_wrapper(endpoint=f"/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}")

class RunScheduledPipelineImmediatelyInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_schedule_id: int = Field(..., description="The pipeline schedule ID.")

@action_store.kubiya_action()
def run_scheduled_pipeline_immediately(input: RunScheduledPipelineImmediatelyInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}/play")

class CreatePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_schedule_id: int = Field(..., description="The pipeline schedule ID.")
    key: str = Field(..., description="The key of a variable; must have no more than 255 characters; only A-Z, a-z, 0-9, and _ are allowed.")
    value: str = Field(..., description="The value of a variable.")
    variable_type: Optional[str] = Field(None, description="The type of a variable. Available types are: env_var (default) and file.")

@action_store.kubiya_action()
def create_pipeline_schedule_variable(input: CreatePipelineScheduleVariableInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}/variables", args=input.dict(exclude_none=True))

class EditPipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_schedule_id: int = Field(..., description="The pipeline schedule ID.")
    key: str = Field(..., description="The key of a variable.")
    value: str = Field(..., description="The value of a variable.")
    variable_type: Optional[str] = Field(None, description="The type of a variable. Available types are: env_var (default) and file.")

@action_store.kubiya_action()
def edit_pipeline_schedule_variable(input: EditPipelineScheduleVariableInput):
    return put_wrapper(endpoint=f"/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}/variables/{input.key}", args=input.dict(exclude_none=True))

class DeletePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_schedule_id: int = Field(..., description="The pipeline schedule ID.")
    key: str = Field(..., description="The key of a variable.")

@action_store.kubiya_action()
def delete_pipeline_schedule_variable(input: DeletePipelineScheduleVariableInput):
    return delete_wrapper(endpoint=f"/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}/variables/{input.key}")
