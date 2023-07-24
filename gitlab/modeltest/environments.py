from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class ProjectsIdEnvironments(BaseModel):
    id: int
    name: Optional[str] = None
    search: Optional[str] = None
    states: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentid(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsCreate(BaseModel):
    id: int
    name: str
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentsid(BaseModel):
    id: int
    environment_id: int
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentidDelete(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsReviewapps(BaseModel):
    id: int
    before: Optional[datetime] = None
    limit: Optional[int] = None
    dry_run: Optional[bool] = None
class ProjectsIdEnvironmentsEnvironmentidStop(BaseModel):
    id: int
    environment_id: int
    force: Optional[bool] = None
class ProjectsIdEnvironmentsStopstale(BaseModel):
    id: int
    before: datetime