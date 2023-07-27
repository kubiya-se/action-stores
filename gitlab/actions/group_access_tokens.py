from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.group_access_tokens import *
@action_store.kubiya_action()
def list_group_access_tokens(input: GroupAccessToken):
    return get_wrapper(endpoint=f'/groups/{input.id}/access_tokens')
@action_store.kubiya_action()
def get_group_access_token(input: GroupAccessTokenByID):
    return get_wrapper(endpoint=f'/groups/{input.id}/access_tokens/{input.token_id}')
@action_store.kubiya_action()
def create_group_access_token(input: CreateGroupAccessToken):
    return post_wrapper(endpoint=f'/groups/{input.id}/access_tokens', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def rotate_group_access_token(input: RotateGroupAccessToken):
    return post_wrapper(endpoint=f'/groups/{input.id}/access_tokens/{input.token_id}/rotate')
@action_store.kubiya_action()
def revoke_group_access_token(input: RevokeGroupAccessToken):
    return delete_wrapper(endpoint=f'/groups/{input.id}/access_tokens/{input.token_id}')