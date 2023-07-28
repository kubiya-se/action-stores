from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ListProjectTriggerTokensInput(BaseModel):
    id: Union[int, str] = Field(..., description='ID or URL-encoded path of the project.')
class GetTriggerTokenDetailsInput(BaseModel):
    id: Union[int, str] = Field(..., description='ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class CreateTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description='ID or URL-encoded path of the project.')
    description: str = Field(..., description='The trigger name.')
class UpdateProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description='ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
    description: Optional[str] = Field(None, description='The trigger name.')
class RemoveProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description='ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class TriggerPipelineWithTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description='ID or URL-encoded path of the project.')
    ref: str = Field(..., description='The branch or tag to run the pipeline on.')
    token: str = Field(..., description='The trigger token or CI/CD job token.')
    variables: Optional[Dict[str, str]] = Field(None, description='A map of key-valued strings containing the pipeline variables.')