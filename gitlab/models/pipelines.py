from typing import List, Any, Optional, Union, Dict, Union
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class Pipelines(BaseModel):
    pipe: List[dict]

class SinglePipeline(BaseModel):
    pipe: dict

class Scope(str, Enum):
    running = 'running'
    pending = 'pending'
    finished = 'finished'
    branches = 'branches'
    tags = 'tags'

class PipelineVariables(BaseModel):
    key: Optional[str]
    variable_type: Optional[str]
    value: Optional[str]

class TestCase(BaseModel):
    status: Optional[str] = None
    name: Optional[str] = None
    classname: Optional[str] = None
    execution_time: Optional[int] = None
    system_output: Optional[str] = None
    stack_trace: Optional[str] = None

class TestSuite(BaseModel):
    name: Optional[str] = None
    total_time: Optional[int] = None
    total_count: Optional[int] = None
    success_count: Optional[int] = None
    failed_count: Optional[int] = None
    skipped_count: Optional[int] = None
    error_count: Optional[int] = None
    test_cases: Optional[List[TestCase]] = None

class TestResult(BaseModel):
    total_time: int
    total_count: Optional[int] = None
    success_count: Optional[int] = None
    failed_count: Optional[int] = None
    skipped_count: Optional[int] = None
    error_count: Optional[int] = None
    test_suites: Optional[List[TestSuite]] = None

class User(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    id: Optional[int] = None
    state: Optional[str] = None
    avatar_url: Optional[str] = None
    web_url: Optional[str] = None

class PipelineResponse(BaseModel):
    id: int
    iid: Optional[int] = None
    project_id: Optional[int] = None
    name: Optional[str] = None
    status: Optional[str] = None
    ref: Optional[str] = None
    sha: Optional[str] = None
    before_sha: Optional[str] = None
    tag: Optional[bool] = None
    yaml_errors: Optional[str] = None
    user: Optional[User] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    committed_at: Optional[datetime] = None
    duration: Optional[float] = None
    queued_duration: Optional[float] = None
    coverage: Optional[str] = None
    web_url: Optional[str] = None

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