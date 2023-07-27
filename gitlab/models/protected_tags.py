from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ProtectedTagsList(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
class SingleProtectedTag(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    name: str = Field(description='The name of the tag or wildcard.')
class CreateAccess(BaseModel):
    user_id: Optional[int] = None
    access_level: Optional[int] = None
class ProtectRepositoryTags(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    name: str = Field(description='The name of the tag or wildcard.')
    allowed_to_create: Optional[List[CreateAccess]] = None
    create_access_level: Optional[int] = Field(None, description='Access levels allowed to create. Default: 40, for Maintainer role.')
class UnprotectRepositoryTags(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    name: str = Field(description='The name of the tag.')