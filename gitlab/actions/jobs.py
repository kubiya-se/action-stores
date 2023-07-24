from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from enum import Enum
from datetime import datetime

class JobScope(str, Enum):
    created = "created"
    pending = "pending"
    running = "running"
    failed = "failed"
    success = "success"
    canceled = "canceled"
    skipped = "skipped"
    waiting_for_resource = "waiting_for_resource"
    manual = "manual"


class ListProjectJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description="ID or URL-encoded path of the project.")
    scope: Union[List[JobScope], JobScope, None] = Field(None, description="Scope of jobs to show.")
    
@action_store.kubiya_action()
def list_project_jobs(input: ListProjectJobsInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/jobs", args=input.dict())


class ListPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description="ID or URL-encoded path of the project.")
    pipeline_id: int = Field(..., description="ID of a pipeline.")
    scope: Union[List[JobScope], JobScope, None] = Field(None, description="Scope of jobs to show.")
    include_retried: Optional[bool] = Field(False, description="Include retried jobs in the response.")

@action_store.kubiya_action()
def list_pipeline_jobs(input: ListPipelineJobsInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/pipelines/{input.pipeline_id}/jobs", args=input.dict())


class ListPipelineTriggerJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description="ID or URL-encoded path of the project.")
    pipeline_id: int = Field(..., description="ID of a pipeline.")
    scope: Union[List[JobScope], JobScope, None] = Field(None, description="Scope of jobs to show.")

@action_store.kubiya_action()
def list_pipeline_trigger_jobs(input: ListPipelineTriggerJobsInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/pipelines/{input.pipeline_id}/bridges", args=input.dict())


# class GetJobInput(BaseModel):
#     CI_JOB_TOKEN: str = Field(..., description="Token value associated with the GitLab-provided CI_JOB_TOKEN variable.")

# @action_store.kubiya_action()
# def get_job_tokens_job(input: GetJobInput):
#     return get_wrapper(endpoint="/job", args=input.dict())


class GetAllowedAgentsInput(BaseModel):
    CI_JOB_TOKEN: str = Field(..., description="Token value associated with the GitLab-provided CI_JOB_TOKEN variable.")

@action_store.kubiya_action()
def get_allowed_agents(input: GetAllowedAgentsInput):
    return get_wrapper(endpoint="/job/allowed_agents", args=input.dict())


class GetSingleJobInput(BaseModel):
    id: Union[int, str] = Field(..., description="ID or URL-encoded path of the project.")
    job_id: int = Field(..., description="ID of a job.")

@action_store.kubiya_action()
def get_a_single_job(input: GetSingleJobInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/jobs/{input.job_id}")

class JobInput(BaseModel):
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    job_id: int = Field(..., description="The ID of a job.")

class JobVariable(BaseModel):
    key: str = Field(..., description="The key of the job variable.")
    value: str = Field(..., description="The value of the job variable.")

class RunJobInput(JobInput):
    job_variables_attributes: Optional[List[JobVariable]] = Field(None, description="An array containing the custom variables available to the job.")

@action_store.kubiya_action()
def get_a_job_log(input: JobInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/jobs/{input.job_id}/trace")

@action_store.kubiya_action()
def cancel_a_job(input: JobInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/jobs/{input.job_id}/cancel")

@action_store.kubiya_action()
def retry_job(input: JobInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/jobs/{input.job_id}/retry")

@action_store.kubiya_action()
def erase_a_job(input: JobInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/jobs/{input.job_id}/erase")

@action_store.kubiya_action()
def run_a_job(input: RunJobInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/jobs/{input.job_id}/play", args=input.dict())