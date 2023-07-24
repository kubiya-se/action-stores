from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class Auditevents(BaseModel):
    created_after: Optional[str] = None
    created_before: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[int] = None
class AuditeventsId(BaseModel):
    id: int
class GroupsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class GroupsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int
class ProjectsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class ProjectsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int