from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class GroupAccessToken(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group.")

@action_store.kubiya_action()
def list_group_access_tokens(input: GroupAccessToken):
    return get_wrapper(endpoint=f"/groups/{input.id}/access_tokens")

class GroupAccessTokenByID(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group.")
    token_id: Union[int, str] = Field(description="ID of the group access token.")

@action_store.kubiya_action()
def get_group_access_token(input: GroupAccessTokenByID):
    return get_wrapper(endpoint=f"/groups/{input.id}/access_tokens/{input.token_id}")

class CreateGroupAccessToken(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group.")
    name: str = Field(description="Name of the group access token.")
    scopes: List[str] = Field(description="List of scopes.")
    access_level: Optional[int] = Field(None, description="Access level. Valid values are 10 (Guest), 20 (Reporter), 30 (Developer), 40 (Maintainer), and 50 (Owner).")
    expires_at: str = Field(description="Expiration date of the access token in ISO format (YYYY-MM-DD). The date cannot be set later than the maximum allowable lifetime of an access token.")

@action_store.kubiya_action()
def create_group_access_token(input: CreateGroupAccessToken):
    return post_wrapper(endpoint=f"/groups/{input.id}/access_tokens", args=input.dict(exclude_none=True))

class RotateGroupAccessToken(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group.")
    token_id: Union[int, str] = Field(description="ID of the group access token.")

@action_store.kubiya_action()
def rotate_group_access_token(input: RotateGroupAccessToken):
    return post_wrapper(endpoint=f"/groups/{input.id}/access_tokens/{input.token_id}/rotate")

class RevokeGroupAccessToken(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group.")
    token_id: Union[int, str] = Field(description="ID of the group access token.")

@action_store.kubiya_action()
def revoke_group_access_token(input: RevokeGroupAccessToken):
    return delete_wrapper(endpoint=f"/groups/{input.id}/access_tokens/{input.token_id}")
