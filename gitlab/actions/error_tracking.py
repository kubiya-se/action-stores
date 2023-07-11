from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class GetErrorTrackingSettings(BaseModel):
    id: Union[int,str]  # The ID or URL-encoded path of the project owned by the authenticated user


@action_store.kubiya_action()
def get_error_tracking_settings(input: GetErrorTrackingSettings):
    return get_wrapper(endpoint=f"/projects/{input.id}/error_tracking/settings", args=input.dict(exclude_none=True))


class CreateErrorTrackingSettings(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    active: bool  # Pass true to enable the error tracking setting configuration or false to disable it.
    integrated: bool  # Pass true to enable the integrated error tracking backend. Available in GitLab 14.2 and later.


@action_store.kubiya_action()
def create_error_tracking_settings(input: CreateErrorTrackingSettings):
    return put_wrapper(endpoint=f"/projects/{input.id}/error_tracking/settings", args=input.dict(exclude_none=True))

class EnableOrDisableTheErrorTrackingProjectSettings(BaseModel):
    id: int  # The ID or URL-encoded path of the project owned by the authenticated user
    active: bool  # Pass true to enable the error tracking setting configuration or false to disable it.
    integrated: Optional[bool] = None  # Pass true to enable the integrated error tracking backend. Available in GitLab 14.2 and later.


@action_store.kubiya_action()
def enable_or_disable_the_error_tracking_project_settings(input: EnableOrDisableTheErrorTrackingProjectSettings):
    return patch_wrapper(endpoint=f"/projects/{input.id}/error_tracking/settings", args=input.dict(exclude_none=True))


class ListProjectClientKeys(BaseModel):
    id: Union[int,str]  # The ID or URL-encoded path of the project owned by the authenticated user.


@action_store.kubiya_action()
def list_project_client_keys(input: ListProjectClientKeys):
    return get_wrapper(endpoint=f"/projects/{input.id}/error_tracking/client_keys", args=input.dict(exclude_none=True))


class CreateAClientKey(BaseModel):
    id: Union[int,str]  # The ID or URL-encoded path of the project owned by the authenticated user.


@action_store.kubiya_action()
def create_a_client_key(input: CreateAClientKey):
    return post_wrapper(endpoint=f"/projects/{input.id}/error_tracking/client_keys", args=input.dict(exclude_none=True))


class DeleteAClientKey(BaseModel):
    id: Union[int,str]  # The ID or URL-encoded path of the project owned by the authenticated user.

    key_id: int  # The ID of the client key.


@action_store.kubiya_action()
def delete_a_client_key(input: DeleteAClientKey):
    return delete_wrapper(endpoint=f"/projects/{input.id}/error_tracking/client_keys/{input.key_id}",
                          args=input.dict(exclude_none=True))
