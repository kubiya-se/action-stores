from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class ProjectsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class ProjectsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class GroupsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int
class ProjectsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int