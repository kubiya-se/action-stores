from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.custom_attributes import *
@action_store.kubiya_action()
def list_custom_attributes_users(input: UsersIdCustomattributes):
    return get_wrapper(endpoint=f'/users/{input.id}/custom_attributes', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_custom_attributes_groups(input: GroupsIdCustomattributes):
    return get_wrapper(endpoint=f'/groups/{input.id}/custom_attributes', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_custom_attributes_projects(input: ProjectsIdCustomattributes):
    return get_wrapper(endpoint=f'/projects/{input.id}/custom_attributes', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def single_custom_attribute_users(input: UsersIdCustomattributesKey):
    return get_wrapper(endpoint=f'/users/{input.id}/custom_attributes/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def single_custom_attribute_groups(input: GroupsIdCustomattributesKey):
    return get_wrapper(endpoint=f'/groups/{input.id}/custom_attributes/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def single_custom_attribute_projects(input: ProjectsIdCustomattributesKey):
    return get_wrapper(endpoint=f'/projects/{input.id}/custom_attributes/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def set_custom_attribute_users(input: UsersIdCustomattributesKeySet):
    return put_wrapper(endpoint=f'/users/{input.id}/custom_attributes/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def set_custom_attribute_groups(input: GroupsIdCustomattributesKeySet):
    return put_wrapper(endpoint=f'/groups/{input.id}/custom_attributes/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def set_custom_attribute_projects(input: ProjectsIdCustomattributesKeySet):
    return put_wrapper(endpoint=f'/projects/{input.id}/custom_attributes/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_custom_attribute_users(input: UsersIdCustomattributesKeyDelete):
    return delete_wrapper(endpoint=f'/users/{input.id}/custom_attributes/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_custom_attribute_groups(input: GroupsIdCustomattributesKeyDelete):
    return delete_wrapper(endpoint=f'/groups/{input.id}/custom_attributes/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_custom_attribute_projects(input: ProjectsIdCustomattributesKeyDelete):
    return delete_wrapper(endpoint=f'/projects/{input.id}/custom_attributes/{input.key}', args=input.dict(exclude_none=True))