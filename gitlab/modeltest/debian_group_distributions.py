from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class ListAllDebianDistributionsInAGroup(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class GroupsIdDebiandistributionsCodenameKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int