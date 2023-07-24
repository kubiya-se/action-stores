from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.error_tracking import *
@action_store.kubiya_action()
def get_error_tracking_settings(input: GetErrorTrackingSettings):
    return get_wrapper(endpoint=f'/projects/{input.id}/error_tracking/settings', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_error_tracking_settings(input: CreateErrorTrackingSettings):
    return put_wrapper(endpoint=f'/projects/{input.id}/error_tracking/settings', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def enable_or_disable_the_error_tracking_project_settings(input: EnableOrDisableTheErrorTrackingProjectSettings):
    return patch_wrapper(endpoint=f'/projects/{input.id}/error_tracking/settings', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_project_client_keys(input: ListProjectClientKeys):
    return get_wrapper(endpoint=f'/projects/{input.id}/error_tracking/client_keys', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_client_key(input: CreateAClientKey):
    return post_wrapper(endpoint=f'/projects/{input.id}/error_tracking/client_keys', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_client_key(input: DeleteAClientKey):
    return delete_wrapper(endpoint=f'/projects/{input.id}/error_tracking/client_keys/{input.key_id}', args=input.dict(exclude_none=True))