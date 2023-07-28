from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.feature_flags import *
@action_store.kubiya_action()
def list_feature_flags(input: ListFeatureFlags):
    return get_wrapper(endpoint=f'/projects/{input.id}/feature_flags', params=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_feature_flag(input: GetFeatureFlag):
    return get_wrapper(endpoint=f'/projects/{input.id}/feature_flags/{input.feature_flag_name}')
@action_store.kubiya_action()
def create_feature_flag(input: CreateFeatureFlag):
    return post_wrapper(endpoint=f'/projects/{input.id}/feature_flags', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_feature_flag(input: UpdateFeatureFlag):
    return put_wrapper(endpoint=f'/projects/{input.id}/feature_flags/{input.feature_flag_name}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_feature_flag(input: DeleteAFeatureFlag):
    return delete_wrapper(endpoint=f'/projects/{input.id}/feature_flags/{input.feature_flag_name}', args=input.dict(exclude_none=True))