from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ListFreezePeriods(BaseModel):
    id: Union[int, str]
class GetFreezePeriod(BaseModel):
    id: Union[int, str]
    freeze_period_id: int
class CreateFreezePeriod(BaseModel):
    id: Union[int, str]
    freeze_start: str
    freeze_end: str
    cron_timezone: Optional[str] = None
class UpdateFreezePeriod(BaseModel):
    id: Union[int, str]
    freeze_period_id: int
    freeze_start: Optional[str] = None
    freeze_end: Optional[str] = None
    cron_timezone: Optional[str] = None
class DeleteFreezePeriod(BaseModel):
    id: Union[int, str]
    freeze_period_id: int