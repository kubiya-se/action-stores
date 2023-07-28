from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class PersonalAccessTokensList(BaseModel):
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    last_used_after: Optional[datetime] = None
    last_used_before: Optional[datetime] = None
    revoked: Optional[bool] = None
    search: Optional[str] = None
    state: Optional[str] = None
    user_id: Optional[Union[int, str]] = None
class SinglePersonalAccessToken(BaseModel):
    id: Union[int, str] = Field(description='ID of personal access token')
class RotatePersonalAccessToken(BaseModel):
    id: Union[int, str] = Field(description='ID of personal access token')
class RevokePersonalAccessToken(BaseModel):
    id: Union[int, str] = Field(description='ID of personal access token')