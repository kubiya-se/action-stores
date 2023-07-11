from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from enum import Enum
from datetime import datetime

class Scope(str, Enum):
    running = "running"
    pending = "pending"
    finished = "finished"
    branches = "branches"
    tags = "tags"

class Status(str, Enum):
    created = "created"
    waiting_for_resource = "waiting_for_resource"
    preparing = "preparing"
    pending = "pending"
    running = "running"
    success = "success"
    failed = "failed"
    canceled = "canceled"
    skipped = "skipped"
    manual = "manual"
    scheduled = "scheduled"

class Source(str, Enum):
    push = "push"
    web = "web"
    trigger = "trigger"
    schedule = "schedule"
    api = "api"
    external = "external"
    pipeline = "pipeline"
    chat = "chat"
    webide = "webide"
    merge_request_event = "merge_request_event"
    external_pull_request_event = "external_pull_request_event"
    parent_pipeline = "parent_pipeline"
    ondemand_dast_scan = "ondemand_dast_scan"
    ondemand_dast_validation = "ondemand_dast_validation"

class OrderBy(str, Enum):
    id = "id"
    status = "status"
    ref = "ref"
    updated_at = "updated_at"
    user_id = "user_id"

class Sort(str, Enum):
    asc = "asc"
    desc = "desc"

class ListProjectPipelinesInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
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

@action_store.kubiya_action()
def list_project_pipelines(input: ListProjectPipelinesInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/pipelines", args=input.dict(exclude_none=True))

class GetPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_id: int = Field(..., description="The ID of a pipeline.")

@action_store.kubiya_action()
def get_pipeline(input: GetPipelineInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/pipelines/{input.pipeline_id}")

class GetPipelineVariablesInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_id: int = Field(..., description="The ID of a pipeline.")

@action_store.kubiya_action()
def get_pipeline_variables(input: GetPipelineVariablesInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/pipelines/{input.pipeline_id}/variables")

class GetPipelineTestReportInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_id: int = Field(..., description="The ID of a pipeline.")

@action_store.kubiya_action()
def get_pipeline_test_report(input: GetPipelineTestReportInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/pipelines/{input.pipeline_id}/test_report")

class GetPipelineTestReportSummaryInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_id: int = Field(..., description="The ID of a pipeline.")

@action_store.kubiya_action()
def get_pipeline_test_report_summary(input: GetPipelineTestReportSummaryInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/pipelines/{input.pipeline_id}/test_report_summary")

class GetLatestPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    ref: Optional[str] = Field(None, description="The branch or tag to check for the latest pipeline. Defaults to the default branch when not specified.")

@action_store.kubiya_action()
def get_latest_pipeline(input: GetLatestPipelineInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/pipelines/latest", args=input.dict(exclude_none=True))

class CreatePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    ref: str = Field(..., description="The branch or tag to run the pipeline on.")
    variables: Optional[List[Dict[str, Union[str, Dict[str, str]]]]] = Field(None, description="An array of hashes containing the variables available in the pipeline.")

@action_store.kubiya_action()
def create_pipeline(input: CreatePipelineInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/pipeline", args=input.dict(exclude_none=True))

class RetryJobsInPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_id: int = Field(..., description="The ID of a pipeline.")

@action_store.kubiya_action()
def retry_jobs_in_pipeline(input: RetryJobsInPipelineInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/pipelines/{input.pipeline_id}/retry")

class CancelPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_id: int = Field(..., description="The ID of a pipeline.")

@action_store.kubiya_action()
def cancel_pipeline_jobs(input: CancelPipelineJobsInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/pipelines/{input.pipeline_id}/cancel")

class DeletePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    pipeline_id: int = Field(..., description="The ID of a pipeline.")

@action_store.kubiya_action()
def delete_pipeline(input: DeletePipelineInput):
    return delete_wrapper(endpoint=f"/projects/{input.id}/pipelines/{input.pipeline_id}")
