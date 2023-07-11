from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class Auditevents(BaseModel):

    created_after: Optional[str] = None # Return audit events created on or after the given time. Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)

    created_before: Optional[str] = None # Return audit events created on or before the given time. Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)

    entity_type: Optional[str] = None # Return audit events for the given entity type. Valid values are: User, Group, or Project.

    entity_id: Optional[int] = None # Return audit events for the given entity ID. Requires entity_type attribute to be present.


@action_store.kubiya_action()
def retrieve_all_instance_audit_events(input: Auditevents):
    return get_wrapper(endpoint=f"/audit_events", args=input.dict(exclude_none=True))


class AuditeventsId(BaseModel):

    id: int # The ID of the audit event


@action_store.kubiya_action()
def retrieve_single_instance_audit_event(input: AuditeventsId):
    return get_wrapper(endpoint=f"/audit_events/{input.id}", args=input.dict(exclude_none=True))


class GroupsIdAuditevents(BaseModel):

    id: int # The ID or URL-encoded path of the group

    created_after: Optional[str] = None # Return group audit events created on or after the given time. Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)

    created_before: Optional[str] = None # Return group audit events created on or before the given time. Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)


@action_store.kubiya_action()
def retrieve_all_group_audit_events(input: GroupsIdAuditevents):
    return get_wrapper(endpoint=f"/groups/{input.id}/audit_events", args=input.dict(exclude_none=True))


class GroupsIdAuditeventsAuditeventid(BaseModel):

    id: int # The ID or URL-encoded path of the group

    audit_event_id: int # The ID of the audit event


@action_store.kubiya_action()
def retrieve_all_group_audit_events(input: GroupsIdAuditeventsAuditeventid):
    return get_wrapper(endpoint=f"/groups/{input.id}/audit_events/{input.audit_event_id}", args=input.dict(exclude_none=True))


class ProjectsIdAuditevents(BaseModel):

    id: int # The ID or URL-encoded path of the project

    created_after: Optional[str] = None # Return project audit events created on or after the given time. Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)

    created_before: Optional[str] = None # Return project audit events created on or before the given time. Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ)


@action_store.kubiya_action()
def retrieve_all_project_audit_events(input: ProjectsIdAuditevents):
    return get_wrapper(endpoint=f"/projects/{input.id}/audit_events", args=input.dict(exclude_none=True))


class ProjectsIdAuditeventsAuditeventid(BaseModel):

    id: int # The ID or URL-encoded path of the project

    audit_event_id: int # The ID of the audit event


@action_store.kubiya_action()
def retrieve_a_specific_project_audit_event(input: ProjectsIdAuditeventsAuditeventid):
    return get_wrapper(endpoint=f"/projects/{input.id}/audit_events/{input.audit_event_id}", args=input.dict(exclude_none=True))
