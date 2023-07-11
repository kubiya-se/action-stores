from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class ListAllFeatureFlagUserListsForProject(BaseModel):
    id: Union[int, str]
    search: Optional[str] = None


class CreateFeatureFlagUserList(BaseModel):
    id: Union[int, str]
    name: str
    user_xids: str #A comma-separated list of external user IDs.


class GetFeatureFlagUserList(BaseModel):
    id: Union[int, str]
    iid: Union[int, str] #The internal ID of the project’s feature flag user list.


class UpdateFeatureFlagUserList(BaseModel):
    id: Union[int, str]
    iid: Union[int, str]
    name: Optional[str] = None #The name of the list.
    user_xids: Optional[str] = None #A comma-separated list of external user IDs.


class DeleteFeatureFlagUserList(BaseModel):
    id: Union[int, str]
    iid: Union[int, str] #The internal ID of the project’s feature flag user list

@action_store.kubiya_action()
def list_all_feature_flag_user_lists_for_project(input: ListAllFeatureFlagUserListsForProject):
    return get_wrapper(endpoint=f"/projects/{input.id}/feature_flags_user_lists", args=input.dict(exclude_none=True))


@action_store.kubiya_action()
def create_feature_flag_user_list(input: CreateFeatureFlagUserList):
    return post_wrapper(endpoint=f"/projects/{input.id}/feature_flags_user_lists", args=input.dict())


@action_store.kubiya_action()
def get_feature_flag_user_list(input: GetFeatureFlagUserList):
    return get_wrapper(endpoint=f"/projects/{input.id}/feature_flags_user_lists/{input.iid}", args=input.dict())


@action_store.kubiya_action()
def update_feature_flag_user_list(input: UpdateFeatureFlagUserList):
    return put_wrapper(endpoint=f"/projects/{input.id}/feature_flags_user_lists/{input.iid}", args=input.dict(exclude_none=True))


@action_store.kubiya_action()
def delete_feature_flag_user_list(input: DeleteFeatureFlagUserList):
    return delete_wrapper(endpoint=f"/projects/{input.id}/feature_flags_user_lists/{input.iid}", args=input.dict())
