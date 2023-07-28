from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class Events(BaseModel):
    action: Optional[str] = None
    target_type: Optional[str] = None
    before: Optional[datetime] = Field(None, description='Include only events created before a certain date.')
    after: Optional[datetime] = Field(None, description='Include only events created after a particular date.')
    target_id: Optional[int] = None
    author_id: Optional[int] = None
    search: Optional[str] = None
class AuthenticatedUserEvents(Events):
    scope: Optional[str] = None
    sort: Optional[str] = None
class UserContributionEvents(Events):
    id: int
    sort: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
class ProjectVisibleEvents(Events):
    project_id: int
    sort: Optional[str] = None