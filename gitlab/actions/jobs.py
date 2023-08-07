from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime
from ..models.jobs import *

from .. import action_store as action_store
from ..http_wrapper import *


@action_store.kubiya_action()
def list_project_jobs(input: ListProjectJobsInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/jobs', args=input.dict())
    return ListDict(response = response)

@action_store.kubiya_action()
def list_pipeline_jobs(input: ListPipelineJobsInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/jobs', args=input.dict())
    return ListDict(response = response)

@action_store.kubiya_action()
def list_pipeline_trigger_jobs(input: ListPipelineTriggerJobsInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/bridges', args=input.dict())
    return ListDict(response = response)

@action_store.kubiya_action()
def get_allowed_agents(input: GetAllowedAgentsInput):
    response = get_wrapper(endpoint='/job/allowed_agents', args=input.dict())
    return SingleDict(response = response)
@action_store.kubiya_action()
def get_a_single_job(input: GetSingleJobInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/jobs/{input.job_id}')
    return SingleDict(response = response)
@action_store.kubiya_action()
def get_a_job_log(input: JobInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/jobs/{input.job_id}/trace')
    return SingleDict(response = response)

@action_store.kubiya_action()
def cancel_a_job(input: JobInput):
    response = post_wrapper(endpoint=f'/projects/{input.id}/jobs/{input.job_id}/cancel')
    return SingleDict(response = response)

@action_store.kubiya_action()
def retry_job(input: JobInput):
    response = post_wrapper(endpoint=f'/projects/{input.id}/jobs/{input.job_id}/retry')
    return SingleDict(response = response)

@action_store.kubiya_action()
def erase_a_job(input: JobInput):
    response = post_wrapper(endpoint=f'/projects/{input.id}/jobs/{input.job_id}/erase')
    return SingleDict(response = response)

@action_store.kubiya_action()
def run_a_job(input: RunJobInput):
    response = post_wrapper(endpoint=f'/projects/{input.id}/jobs/{input.job_id}/play', args=input.dict())
    return SingleDict(response = response)
