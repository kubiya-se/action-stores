from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ProjectsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None
class GroupsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None