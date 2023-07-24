from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class ListAllDebianDistributionsInAProject(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class SingleDebianProjectDistributionKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianProjectDistribution(BaseModel):
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
class UpdateADebianProjectDistribution(BaseModel):
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
class DeleteADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int