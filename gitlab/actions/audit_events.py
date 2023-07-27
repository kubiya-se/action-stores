from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.audit_events import *
@action_store.kubiya_action()
def retrieve_all_instance_audit_events(input: Auditevents):
    return get_wrapper(endpoint=f'/audit_events', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def retrieve_single_instance_audit_event(input: AuditeventsId):
    return get_wrapper(endpoint=f'/audit_events/{input.id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def retrieve_all_group_audit_events(input: GroupsIdAuditevents):
    return get_wrapper(endpoint=f'/groups/{input.id}/audit_events', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def retrieve_all_group_audit_events(input: GroupsIdAuditeventsAuditeventid):
    return get_wrapper(endpoint=f'/groups/{input.id}/audit_events/{input.audit_event_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def retrieve_all_project_audit_events(input: ProjectsIdAuditevents):
    return get_wrapper(endpoint=f'/projects/{input.id}/audit_events', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def retrieve_a_specific_project_audit_event(input: ProjectsIdAuditeventsAuditeventid):
    return get_wrapper(endpoint=f'/projects/{input.id}/audit_events/{input.audit_event_id}', args=input.dict(exclude_none=True))