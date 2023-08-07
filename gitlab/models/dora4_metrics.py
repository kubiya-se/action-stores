from typing import List, Any, Optional, Union, Dict, Union
from pydantic import BaseModel, Field
from datetime import datetime


class ListDict(BaseModel):
    response: List[dict]

class SingleDict(BaseModel):
    response: dict

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