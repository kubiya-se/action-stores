from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.pipelines import *
@action_store.kubiya_action()
def list_project_pipelines(input: ListProjectPipelinesInput):
    return get_wrapper(endpoint=f'/projects/{input.id}/pipelines', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_pipeline(input: GetPipelineInput):
    return get_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}')
@action_store.kubiya_action()
def get_pipeline_variables(input: GetPipelineVariablesInput):
    return get_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/variables')
@action_store.kubiya_action()
def get_pipeline_test_report(input: GetPipelineTestReportInput):
    return get_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/test_report')
@action_store.kubiya_action()
def get_pipeline_test_report_summary(input: GetPipelineTestReportSummaryInput):
    return get_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/test_report_summary')
@action_store.kubiya_action()
def get_latest_pipeline(input: GetLatestPipelineInput):
    return get_wrapper(endpoint=f'/projects/{input.id}/pipelines/latest', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_pipeline(input: CreatePipelineInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/pipeline', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def retry_jobs_in_pipeline(input: RetryJobsInPipelineInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/retry')
@action_store.kubiya_action()
def cancel_pipeline_jobs(input: CancelPipelineJobsInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}/cancel')
@action_store.kubiya_action()
def delete_pipeline(input: DeletePipelineInput):
    return delete_wrapper(endpoint=f'/projects/{input.id}/pipelines/{input.pipeline_id}')