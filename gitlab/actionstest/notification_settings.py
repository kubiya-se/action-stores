from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.notification_settings import *
@action_store.kubiya_action()
def get_global_notification_settings():
    return get_wrapper(endpoint='/notification_settings')
@action_store.kubiya_action()
def update_global_notification_settings(input: GlobalNotificationSettingsUpdate):
    return put_wrapper(endpoint='/notification_settings', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_group_notification_settings(input: GroupOrProjectNotificationSettingsGet):
    return get_wrapper(endpoint=f'/groups/{input.id}/notification_settings', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_project_notification_settings(input: GroupOrProjectNotificationSettingsGet):
    return get_wrapper(endpoint=f'/projects/{input.id}/notification_settings', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_group_notification_settings(input: GroupOrProjectNotificationSettingsUpdate):
    return put_wrapper(endpoint=f'/groups/{input.id}/notification_settings', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_project_notification_settings(input: GroupOrProjectNotificationSettingsUpdate):
    return put_wrapper(endpoint=f'/projects/{input.id}/notification_settings', args=input.dict(exclude_none=True))