from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class ProjectsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class ProjectsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesCreate(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str