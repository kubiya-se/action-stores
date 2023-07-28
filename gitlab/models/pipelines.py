from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class Scope(str, Enum):
    running = 'running'
    pending = 'pending'
    finished = 'finished'
    branches = 'branches'
    tags = 'tags'
class Status(str, Enum):
    created = 'created'
    waiting_for_resource = 'waiting_for_resource'
    preparing = 'preparing'
    pending = 'pending'
    running = 'running'
    success = 'success'
    failed = 'failed'
    canceled = 'canceled'
    skipped = 'skipped'
    manual = 'manual'
    scheduled = 'scheduled'
class Source(str, Enum):
    push = 'push'
    web = 'web'
    trigger = 'trigger'
    schedule = 'schedule'
    api = 'api'
    external = 'external'
    pipeline = 'pipeline'
    chat = 'chat'
    webide = 'webide'
    merge_request_event = 'merge_request_event'
    external_pull_request_event = 'external_pull_request_event'
    parent_pipeline = 'parent_pipeline'
    ondemand_dast_scan = 'ondemand_dast_scan'
    ondemand_dast_validation = 'ondemand_dast_validation'
class OrderBy(str, Enum):
    id = 'id'
    status = 'status'
    ref = 'ref'
    updated_at = 'updated_at'
    user_id = 'user_id'
class Sort(str, Enum):
    asc = 'asc'
    desc = 'desc'
class ListProjectPipelinesInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    scope: Optional[Scope]
    status: Optional[Status]
    source: Optional[Source]
    ref: Optional[str]
    sha: Optional[str]
    yaml_errors: Optional[bool]
    username: Optional[str]
    updated_after: Optional[datetime]
    updated_before: Optional[datetime]
    name: Optional[str]
    order_by: Optional[OrderBy]
    sort: Optional[Sort]
class GetPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineVariablesInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportSummaryInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetLatestPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    ref: Optional[str] = Field(None, description='The branch or tag to check for the latest pipeline. Defaults to the default branch when not specified.')
class CreatePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    ref: str = Field(..., description='The branch or tag to run the pipeline on.')
    variables: Optional[List[Dict[str, Union[str, Dict[str, str]]]]] = Field(None, description='An array of hashes containing the variables available in the pipeline.')
class RetryJobsInPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class CancelPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class DeletePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')