from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.personal_access_tokens import *
@action_store.kubiya_action()
def list_personal_access_tokens(input: PersonalAccessTokensList):
    return get_wrapper(endpoint='/personal_access_tokens', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_single_personal_access_token_using_a_personal_access_token_ID(input: SinglePersonalAccessToken):
    return get_wrapper(endpoint=f'/personal_access_tokens/{input.id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_personal_access_token_using_a_request_header():
    return get_wrapper(endpoint='/personal_access_tokens/self')
@action_store.kubiya_action()
def rotate_personal_access_token(input: RotatePersonalAccessToken):
    return post_wrapper(endpoint=f'/personal_access_tokens/{input.id}/rotate', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def revoke_personal_access_token_using_a_personal_access_token_ID(input: RevokePersonalAccessToken):
    return delete_wrapper(endpoint=f'/personal_access_tokens/{input.id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def revoke_personal_access_token_using_a_request_header():
    return delete_wrapper(endpoint='/personal_access_tokens/self')