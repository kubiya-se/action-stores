from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field, parse_object_as
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.pipelines import *

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


@action_store.kubiya_action()
def list_project_pipelines(input: ListProjectPipelinesInput):
    response =  get_wrapper(endpoint=f'/projects/{input.id}/pipelines', args=input.dict(exclude_none=True))
    return parse_object_as(List[PipelineResponse], response)

class PipelineVariables(BaseModel):
    key: Optional[str]
    variable_type: Optional[str]
    value: Optional[str]

@action_store.kubiya_action()
def get_pipeline(input: GetPipelineInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}')
    return parse_object_as(PipelineResponse, response)

@action_store.kubiya_action()
def get_pipeline_variables(input: GetPipelineVariablesInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/variables')
    return parse_object_as(List[PipelineVariables], response)

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

@action_store.kubiya_action()
def get_pipeline_test_report(input: GetPipelineTestReportInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/test_report')
    return parse_object_as(TestResult, response)

@action_store.kubiya_action()
def get_pipeline_test_report_summary(input: GetPipelineTestReportSummaryInput):
    return get_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/test_report_summary')

@action_store.kubiya_action()
def get_latest_pipeline(input: GetLatestPipelineInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/pipelines/latest', args=input.dict(exclude_none=True))
    return parse_object_as(PipelineResponse, response)


@action_store.kubiya_action()
def create_pipeline(input: CreatePipelineInput):
    response = post_wrapper(endpoint=f'/projects/{input.id}/pipeline', args=input.dict(exclude_none=True))
    return parse_object_as(PipelineResponse, response)
@action_store.kubiya_action()
def retry_jobs_in_pipeline(input: RetryJobsInPipelineInput):
    response = post_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/retry')
    return parse_object_as(PipelineResponse, response)
@action_store.kubiya_action()
def cancel_pipeline_jobs(input: CancelPipelineJobsInput):
    response = post_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/cancel')
    return parse_object_as(PipelineResponse, response)
@action_store.kubiya_action()
def delete_pipeline(input: DeletePipelineInput):
    return delete_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}')