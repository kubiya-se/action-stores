from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

@action_store.kubiya_action()
def get_global_notification_settings():
    return get_wrapper(endpoint="/notification_settings")

class GlobalNotificationSettingsUpdate(BaseModel):
    level: Optional[str] = None
    notification_email: Optional[str] = None
    new_note: Optional[bool] = None
    new_issue: Optional[bool] = None
    reopen_issue: Optional[bool] = None
    close_issue: Optional[bool] = None
    reassign_issue: Optional[bool] = None
    issue_due: Optional[bool] = None
    new_merge_request: Optional[bool] = None
    push_to_merge_request: Optional[bool] = None
    reopen_merge_request: Optional[bool] = None
    close_merge_request: Optional[bool] = None
    reassign_merge_request: Optional[bool] = None
    merge_merge_request: Optional[bool] = None
    failed_pipeline: Optional[bool] = None
    fixed_pipeline: Optional[bool] = None
    success_pipeline: Optional[bool] = None
    moved_project: Optional[bool] = None
    merge_when_pipeline_succeeds: Optional[bool] = None
    new_epic: Optional[bool] = None

@action_store.kubiya_action()
def update_global_notification_settings(input: GlobalNotificationSettingsUpdate):
    return put_wrapper(endpoint="/notification_settings", args=input.dict(exclude_none=True))

class GroupOrProjectNotificationSettingsGet(BaseModel):
    id: Union[int, str] = Field(description="The ID, or URL-encoded path, of the group or project")

@action_store.kubiya_action()
def get_group_notification_settings(input: GroupOrProjectNotificationSettingsGet):
    return get_wrapper(endpoint=f"/groups/{input.id}/notification_settings", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def get_project_notification_settings(input: GroupOrProjectNotificationSettingsGet):
    return get_wrapper(endpoint=f"/projects/{input.id}/notification_settings", args=input.dict(exclude_none=True))

class GroupOrProjectNotificationSettingsUpdate(BaseModel):
    id: Union[int, str] = Field(description="The ID, or URL-encoded path, of the group or project")
    level: Optional[str] = None
    new_note: Optional[bool] = None
    new_issue: Optional[bool] = None
    reopen_issue: Optional[bool] = None
    close_issue: Optional[bool] = None
    reassign_issue: Optional[bool] = None
    issue_due: Optional[bool] = None
    new_merge_request: Optional[bool] = None
    push_to_merge_request: Optional[bool] = None
    reopen_merge_request: Optional[bool] = None
    close_merge_request: Optional[bool] = None
    reassign_merge_request: Optional[bool] = None
    merge_merge_request: Optional[bool] = None
    failed_pipeline: Optional[bool] = None
    fixed_pipeline: Optional[bool] = None
    success_pipeline: Optional[bool] = None
    moved_project: Optional[bool] = None
    merge_when_pipeline_succeeds: Optional[bool] = None
    new_epic: Optional[bool] = None

@action_store.kubiya_action()
def update_group_notification_settings(input: GroupOrProjectNotificationSettingsUpdate):
    return put_wrapper(endpoint=f"/groups/{input.id}/notification_settings", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def update_project_notification_settings(input: GroupOrProjectNotificationSettingsUpdate):
    return put_wrapper(endpoint=f"/projects/{input.id}/notification_settings", args=input.dict(exclude_none=True))
