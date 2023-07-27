from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class GroupsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class GroupsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesAdd(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class GroupsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class GroupsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str