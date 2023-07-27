from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class GroupAccessToken(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group.')
class GroupAccessTokenByID(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group.')
    token_id: Union[int, str] = Field(description='ID of the group access token.')
class CreateGroupAccessToken(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group.')
    name: str = Field(description='Name of the group access token.')
    scopes: List[str] = Field(description='List of scopes.')
    access_level: Optional[int] = Field(None, description='Access level. Valid values are 10 (Guest), 20 (Reporter), 30 (Developer), 40 (Maintainer), and 50 (Owner).')
    expires_at: str = Field(description='Expiration date of the access token in ISO format (YYYY-MM-DD). The date cannot be set later than the maximum allowable lifetime of an access token.')
class RotateGroupAccessToken(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group.')
    token_id: Union[int, str] = Field(description='ID of the group access token.')
class RevokeGroupAccessToken(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group.')
    token_id: Union[int, str] = Field(description='ID of the group access token.')