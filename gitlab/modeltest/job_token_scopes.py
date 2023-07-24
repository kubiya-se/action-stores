from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class GetProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
class PatchProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
    enabled: bool
class GetProjectCICDJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
class CreateNewProjectToJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int
class RemoveProjectFromJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int