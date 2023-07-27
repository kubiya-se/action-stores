from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ProjectResourceGroups(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
class SingleResourceGroup(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    key: str = Field(description='The key of the resource group.')
class ResourceGroupUpcomingJobs(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    key: str = Field(description='The key of the resource group.')
class UpdateResourceGroup(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    key: str = Field(description='The key of the resource group.')
    process_mode: Optional[str] = Field(None, description='The process mode of the resource group. One of unordered, oldest_first or newest_first.')