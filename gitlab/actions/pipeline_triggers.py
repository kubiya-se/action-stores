from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class ListProjectTriggerTokensInput(BaseModel):
    id: Union[int, str] = Field(..., description="ID or URL-encoded path of the project.")

@action_store.kubiya_action()
def list_project_trigger_tokens(input: ListProjectTriggerTokensInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/triggers")

class GetTriggerTokenDetailsInput(BaseModel):
    id: Union[int, str] = Field(..., description="ID or URL-encoded path of the project.")
    trigger_id: int = Field(..., description="The trigger ID.")

@action_store.kubiya_action()
def get_trigger_token_details(input: GetTriggerTokenDetailsInput):
    return get_wrapper(endpoint=f"/projects/{input.id}/triggers/{input.trigger_id}")

class CreateTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description="ID or URL-encoded path of the project.")
    description: str = Field(..., description="The trigger name.")

@action_store.kubiya_action()
def create_a_trigger_token(input: CreateTriggerTokenInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/triggers", args=input.dict())

class UpdateProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description="ID or URL-encoded path of the project.")
    trigger_id: int = Field(..., description="The trigger ID.")
    description: Optional[str] = Field(None, description="The trigger name.")

@action_store.kubiya_action()
def update_project_trigger_token(input: UpdateProjectTriggerTokenInput):
    return put_wrapper(endpoint=f"/projects/{input.id}/triggers/{input.trigger_id}", args=input.dict(exclude_none=True))

class RemoveProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description="ID or URL-encoded path of the project.")
    trigger_id: int = Field(..., description="The trigger ID.")

@action_store.kubiya_action()
def remove_project_trigger_token(input: RemoveProjectTriggerTokenInput):
    return delete_wrapper(endpoint=f"/projects/{input.id}/triggers/{input.trigger_id}")

class TriggerPipelineWithTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description="ID or URL-encoded path of the project.")
    ref: str = Field(..., description="The branch or tag to run the pipeline on.")
    token: str = Field(..., description="The trigger token or CI/CD job token.")
    variables: Optional[Dict[str, str]] = Field(None, description="A map of key-valued strings containing the pipeline variables.")

@action_store.kubiya_action()
def trigger_pipeline_with_token(input: TriggerPipelineWithTokenInput):
    return post_wrapper(endpoint=f"/projects/{input.id}/trigger/pipeline", args=input.dict(exclude_none=True))
