from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class GetAllPipelineSchedulesInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    scope: Optional[str] = Field(None, description='The scope of pipeline schedules, must be one of: active, inactive.')
class GetSinglePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description='The pipeline schedule ID.')
class GetPipelinesTriggeredByScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description='The pipeline schedule ID.')
class CreateNewPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    description: str = Field(..., description='The description of the pipeline schedule.')
    ref: str = Field(..., description='The branch or tag name that is triggered.')
    cron: str = Field(..., description='The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description='The time zone supported by ActiveSupport::TimeZone, for example: Pacific Time (US & Canada) (default: UTC).')
    active: Optional[bool] = Field(None, description='The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated (default: true).')
class EditPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description='The pipeline schedule ID.')
    description: Optional[str] = Field(None, description='The description of the pipeline schedule.')
    ref: Optional[str] = Field(None, description='The branch or tag name that is triggered.')
    cron: Optional[str] = Field(None, description='The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description='The time zone supported by ActiveSupport::TimeZone (for example Pacific Time (US & Canada)), or TZInfo::Timezone (for example America/Los_Angeles).')
    active: Optional[bool] = Field(None, description='The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated.')
class TakeOwnershipOfPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description='The pipeline schedule ID.')
class DeletePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description='The pipeline schedule ID.')
class RunScheduledPipelineImmediatelyInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description='The pipeline schedule ID.')
class CreatePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description='The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable; must have no more than 255 characters; only A-Z, a-z, 0-9, and _ are allowed.')
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description='The type of a variable. Available types are: env_var (default) and file.')
class EditPipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description='The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description='The type of a variable. Available types are: env_var (default) and file.')
class DeletePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description='The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')