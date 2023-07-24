from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.pipelines_schedules import *
@action_store.kubiya_action()
def get_all_pipeline_schedules(input: GetAllPipelineSchedulesInput):
    return get_wrapper(endpoint=f'/projects/{input.id}/pipeline_schedules', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_single_pipeline_schedule(input: GetSinglePipelineScheduleInput):
    return get_wrapper(endpoint=f'/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}')
@action_store.kubiya_action()
def get_pipelines_triggered_by_schedule(input: GetPipelinesTriggeredByScheduleInput):
    return get_wrapper(endpoint=f'/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}/pipelines')
@action_store.kubiya_action()
def create_new_pipeline_schedule(input: CreateNewPipelineScheduleInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/pipeline_schedules', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def edit_pipeline_schedule(input: EditPipelineScheduleInput):
    return put_wrapper(endpoint=f'/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def take_ownership_of_pipeline_schedule(input: TakeOwnershipOfPipelineScheduleInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}/take_ownership')
@action_store.kubiya_action()
def delete_pipeline_schedule(input: DeletePipelineScheduleInput):
    return delete_wrapper(endpoint=f'/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}')
@action_store.kubiya_action()
def run_scheduled_pipeline_immediately(input: RunScheduledPipelineImmediatelyInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}/play')
@action_store.kubiya_action()
def create_pipeline_schedule_variable(input: CreatePipelineScheduleVariableInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}/variables', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def edit_pipeline_schedule_variable(input: EditPipelineScheduleVariableInput):
    return put_wrapper(endpoint=f'/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}/variables/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_pipeline_schedule_variable(input: DeletePipelineScheduleVariableInput):
    return delete_wrapper(endpoint=f'/projects/{input.id}/pipeline_schedules/{input.pipeline_schedule_id}/variables/{input.key}')