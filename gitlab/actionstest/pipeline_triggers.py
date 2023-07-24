from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.pipeline_triggers import *
@action_store.kubiya_action()
def list_project_trigger_tokens(input: ListProjectTriggerTokensInput):
    return get_wrapper(endpoint=f'/projects/{input.id}/triggers')
@action_store.kubiya_action()
def get_trigger_token_details(input: GetTriggerTokenDetailsInput):
    return get_wrapper(endpoint=f'/projects/{input.id}/triggers/{input.trigger_id}')
@action_store.kubiya_action()
def create_a_trigger_token(input: CreateTriggerTokenInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/triggers', args=input.dict())
@action_store.kubiya_action()
def update_project_trigger_token(input: UpdateProjectTriggerTokenInput):
    return put_wrapper(endpoint=f'/projects/{input.id}/triggers/{input.trigger_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def remove_project_trigger_token(input: RemoveProjectTriggerTokenInput):
    return delete_wrapper(endpoint=f'/projects/{input.id}/triggers/{input.trigger_id}')
@action_store.kubiya_action()
def trigger_pipeline_with_token(input: TriggerPipelineWithTokenInput):
    return post_wrapper(endpoint=f'/projects/{input.id}/trigger/pipeline', args=input.dict(exclude_none=True))