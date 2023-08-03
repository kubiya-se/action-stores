from typing import List, Any, Optional, Union
from pydantic import BaseModel
from datetime import datetime
from ..models.pipelines import *

from .. import action_store as action_store
from ..http_wrapper import *


@action_store.kubiya_action()
def list_project_pipelines(input: ListProjectPipelinesInput):
    response =  get_wrapper(endpoint=f'/projects/{input.id}/pipelines', args=input.dict(exclude_none=True))
    return Pipelines(pipe=response)

@action_store.kubiya_action()
def get_pipeline(input: GetPipelineInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}')
    return SinglePipeline(pipe=response)

@action_store.kubiya_action()
def get_pipeline_variables(input: GetPipelineVariablesInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/variables')
    return Pipelines(pipe=response)

@action_store.kubiya_action()
def get_pipeline_test_report(input: GetPipelineTestReportInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/test_report')
    return SinglePipeline(pipe=response)

@action_store.kubiya_action()
def get_pipeline_test_report_summary(input: GetPipelineTestReportSummaryInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/test_report_summary')
    return SinglePipeline(pipe=response)

@action_store.kubiya_action()
def get_latest_pipeline(input: GetLatestPipelineInput):
    response = get_wrapper(endpoint=f'/projects/{input.id}/pipelines/latest', args=input.dict(exclude_none=True))
    return SinglePipeline(pipe=response)    

@action_store.kubiya_action()
def create_pipeline(input: CreatePipelineInput):
    response = post_wrapper(endpoint=f'/projects/{input.id}/pipeline', args=input.dict(exclude_none=True))
    return SinglePipeline(pipe=response)

@action_store.kubiya_action()
def retry_jobs_in_pipeline(input: RetryJobsInPipelineInput):
    response = post_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/retry')
    return SinglePipeline(pipe=response)

@action_store.kubiya_action()
def cancel_pipeline_jobs(input: CancelPipelineJobsInput):
    response = post_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/cancel')
    return SinglePipeline(pipe=response)

@action_store.kubiya_action()
def delete_pipeline(input: DeletePipelineInput):
    response = delete_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}')
    return SinglePipeline(pipe=response)