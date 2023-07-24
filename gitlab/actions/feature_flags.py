from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field, Json
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class StrategyScope(BaseModel):
    id: Optional[Json]
    environment_scope: Optional[str]

class Strategy(BaseModel):
    id: Optional[Json]
    name: Optional[Json]
    parameters: Optional[Json]
    scopes: Optional[List[StrategyScope]]

class FeatureFlag(BaseModel):
    name: str
    description: Optional[str]
    active: bool
    version: str
    created_at: datetime
    updated_at: datetime
    scopes: Optional[List[Any]]
    strategies: Optional[List[Strategy]]

class ListFeatureFlags(BaseModel):
    id: Union[int, str]
    scope: Optional[str]

@action_store.kubiya_action()
def list_feature_flags(input: ListFeatureFlags):
    return get_wrapper(endpoint=f"/projects/{input.id}/feature_flags", params=input.dict(exclude_none=True))

class GetFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str

@action_store.kubiya_action()
def get_feature_flag(input: GetFeatureFlag):
    return get_wrapper(endpoint=f"/projects/{input.id}/feature_flags/{input.feature_flag_name}")

class CreateFeatureFlag(BaseModel):
    id: Union[int, str]
    name: str
    version: str
    description: Optional[str] = None
    active: Optional[bool] = None
    strategies: Optional[List[Strategy]] = None

@action_store.kubiya_action()
def create_feature_flag(input: CreateFeatureFlag):
    return post_wrapper(endpoint=f"/projects/{input.id}/feature_flags", args=input.dict(exclude_none=True))


class StrategyScopeUpdate(BaseModel):
    id: Optional[Json] = None
    environment_scope: Optional[str] = None
    _destroy: Optional[bool] = None

class StrategyUpdate(BaseModel):
    id: Optional[Json] = None
    name: Optional[Json] = None
    _destroy: Optional[bool] = None
    parameters: Optional[Json] = None
    scopes: Optional[List[StrategyScopeUpdate]] = None

class UpdateFeatureFlag(BaseModel):
    id: Union[int, str]  # The ID or URL-encoded path of the project.
    feature_flag_name: str  # The current name of the feature flag.
    description: Optional[str] = None  # The description of the feature flag.
    active: Optional[bool] = None  # The active state of the flag. Supported in GitLab 13.3 and later.
    name: Optional[str] = None  # The new name of the feature flag. Supported in GitLab 13.3 and later.
    strategies: Optional[List[StrategyUpdate]] = None

@action_store.kubiya_action()
def update_feature_flag(input: UpdateFeatureFlag):
    return put_wrapper(endpoint=f"/projects/{input.id}/feature_flags/{input.feature_flag_name}", args=input.dict(exclude_none=True))

class DeleteAFeatureFlag(BaseModel):
    id: Union[int,str]
    feature_flag_name: str

@action_store.kubiya_action()
def delete_a_feature_flag(input: DeleteAFeatureFlag):
    return delete_wrapper(endpoint = f"/projects/{input.id}/feature_flags/{input.feature_flag_name}", args = input.dict(exclude_none=True))