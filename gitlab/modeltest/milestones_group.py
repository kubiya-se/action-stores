from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class MilestoneStates(str, Enum):
    active = 'active'
    closed = 'closed'
class GroupMilestonesGet(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group owned by the authenticated user')
    iids: Optional[List[int]] = None
    state: Optional[str] = None
    title: Optional[str] = None
    search: Optional[str] = None
    include_parent_milestones: Optional[bool] = None
    updated_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None
class SingleGroupMilestoneGet(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group owned by the authenticated user')
    milestone_id: int = Field(description='The ID of a group milestone')
class GroupMilestoneCreate(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group owned by the authenticated user')
    title: str = Field(description='The title of a milestone')
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
class GroupMilestoneUpdate(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group owned by the authenticated user')
    milestone_id: int = Field(description='The ID of a group milestone')
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    start_date: Optional[datetime] = None
    state_event: Optional[str] = None
class GroupMilestoneDelete(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group owned by the authenticated user')
    milestone_id: int = Field(description='The ID of the group’s milestone')