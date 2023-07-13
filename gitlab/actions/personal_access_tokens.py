from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
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

@action_store.kubiya_action()
def list_personal_access_tokens(input: PersonalAccessTokensList):
    return get_wrapper(endpoint="/personal_access_tokens", args=input.dict(exclude_none=True))

class SinglePersonalAccessToken(BaseModel):
    id: Union[int, str] = Field(description="ID of personal access token")

@action_store.kubiya_action()
def get_single_personal_access_token_using_a_personal_access_token_ID(input: SinglePersonalAccessToken):
    return get_wrapper(endpoint=f"/personal_access_tokens/{input.id}", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def get_personal_access_token_using_a_request_header():
    return get_wrapper(endpoint="/personal_access_tokens/self")

class RotatePersonalAccessToken(BaseModel):
    id: Union[int, str] = Field(description="ID of personal access token")

@action_store.kubiya_action()
def rotate_personal_access_token(input: RotatePersonalAccessToken):
    return post_wrapper(endpoint=f"/personal_access_tokens/{input.id}/rotate", args=input.dict(exclude_none=True))

class RevokePersonalAccessToken(BaseModel):
    id: Union[int, str] = Field(description="ID of personal access token")

@action_store.kubiya_action()
def revoke_personal_access_token_using_a_personal_access_token_ID(input: RevokePersonalAccessToken):
    return delete_wrapper(endpoint=f"/personal_access_tokens/{input.id}", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def revoke_personal_access_token_using_a_request_header():
    return delete_wrapper(endpoint="/personal_access_tokens/self")
