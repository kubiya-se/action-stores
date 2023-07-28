from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class GetErrorTrackingSettings(BaseModel):
    id: Union[int, str]
class CreateErrorTrackingSettings(BaseModel):
    id: int
    active: bool
    integrated: bool
class EnableOrDisableTheErrorTrackingProjectSettings(BaseModel):
    id: int
    active: bool
    integrated: Optional[bool] = None
class ListProjectClientKeys(BaseModel):
    id: Union[int, str]
class CreateAClientKey(BaseModel):
    id: Union[int, str]
class DeleteAClientKey(BaseModel):
    id: Union[int, str]
    key_id: int