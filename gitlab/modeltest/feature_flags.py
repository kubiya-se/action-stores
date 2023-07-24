from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
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
class GetFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
class CreateFeatureFlag(BaseModel):
    id: Union[int, str]
    name: str
    version: str
    description: Optional[str] = None
    active: Optional[bool] = None
    strategies: Optional[List[Strategy]] = None
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
    id: Union[int, str]
    feature_flag_name: str
    description: Optional[str] = None
    active: Optional[bool] = None
    name: Optional[str] = None
    strategies: Optional[List[StrategyUpdate]] = None
class DeleteAFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str