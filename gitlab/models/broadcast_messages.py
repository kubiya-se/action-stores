from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class GetASpecificBroadcastMessage(BaseModel):
    id: int
class CreateABroadcastMessage(BaseModel):
    message: str
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class UpdateABroadcastMessage(BaseModel):
    id: int
    message: Optional[str]
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class DeleteABroadcastMessage(BaseModel):
    id: int