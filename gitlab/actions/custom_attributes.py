from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class UsersIdCustomattributes(BaseModel):
    id: int  # The ID of a resource


@action_store.kubiya_action()
def list_custom_attributes_users(input: UsersIdCustomattributes):
    return get_wrapper(endpoint=f"/users/{input.id}/custom_attributes", args=input.dict(exclude_none=True))


class GroupsIdCustomattributes(BaseModel):
    id: int  # The ID of a resource


@action_store.kubiya_action()
def list_custom_attributes_groups(input: GroupsIdCustomattributes):
    return get_wrapper(endpoint=f"/groups/{input.id}/custom_attributes", args=input.dict(exclude_none=True))


class ProjectsIdCustomattributes(BaseModel):
    id: int  # The ID of a resource


@action_store.kubiya_action()
def list_custom_attributes_projects(input: ProjectsIdCustomattributes):
    return get_wrapper(endpoint=f"/projects/{input.id}/custom_attributes", args=input.dict(exclude_none=True))


class UsersIdCustomattributesKey(BaseModel):
    id: int  # The ID of a resource

    key: str  # The key of the custom attribute


@action_store.kubiya_action()
def single_custom_attribute_users(input: UsersIdCustomattributesKey):
    return get_wrapper(endpoint=f"/users/{input.id}/custom_attributes/{input.key}", args=input.dict(exclude_none=True))


class GroupsIdCustomattributesKey(BaseModel):
    id: int  # The ID of a resource

    key: str  # The key of the custom attribute


@action_store.kubiya_action()
def single_custom_attribute_groups(input: GroupsIdCustomattributesKey):
    return get_wrapper(endpoint=f"/groups/{input.id}/custom_attributes/{input.key}", args=input.dict(exclude_none=True))


class ProjectsIdCustomattributesKey(BaseModel):
    id: int  # The ID of a resource

    key: str  # The key of the custom attribute


@action_store.kubiya_action()
def single_custom_attribute_projects(input: ProjectsIdCustomattributesKey):
    return get_wrapper(endpoint=f"/projects/{input.id}/custom_attributes/{input.key}",
                       args=input.dict(exclude_none=True))


class UsersIdCustomattributesKeySet(BaseModel):
    id: int  # The ID of a resource

    key: str  # The key of the custom attribute

    value: str  # The value of the custom attribute


@action_store.kubiya_action()
def set_custom_attribute_users(input: UsersIdCustomattributesKeySet):
    return put_wrapper(endpoint=f"/users/{input.id}/custom_attributes/{input.key}", args=input.dict(exclude_none=True))


class GroupsIdCustomattributesKeySet(BaseModel):
    id: int  # The ID of a resource

    key: str  # The key of the custom attribute

    value: str  # The value of the custom attribute


@action_store.kubiya_action()
def set_custom_attribute_groups(input: GroupsIdCustomattributesKeySet):
    return put_wrapper(endpoint=f"/groups/{input.id}/custom_attributes/{input.key}", args=input.dict(exclude_none=True))


class ProjectsIdCustomattributesKeySet(BaseModel):
    id: int  # The ID of a resource

    key: str  # The key of the custom attribute

    value: str  # The value of the custom attribute


@action_store.kubiya_action()
def set_custom_attribute_projects(input: ProjectsIdCustomattributesKeySet):
    return put_wrapper(endpoint=f"/projects/{input.id}/custom_attributes/{input.key}",
                       args=input.dict(exclude_none=True))


class UsersIdCustomattributesKeyDelete(BaseModel):
    id: int  # The ID of a resource

    key: str  # The key of the custom attribute


@action_store.kubiya_action()
def delete_custom_attribute_users(input: UsersIdCustomattributesKeyDelete):
    return delete_wrapper(endpoint=f"/users/{input.id}/custom_attributes/{input.key}",
                          args=input.dict(exclude_none=True))


class GroupsIdCustomattributesKeyDelete(BaseModel):
    id: int  # The ID of a resource

    key: str  # The key of the custom attribute


@action_store.kubiya_action()
def delete_custom_attribute_groups(input: GroupsIdCustomattributesKeyDelete):
    return delete_wrapper(endpoint=f"/groups/{input.id}/custom_attributes/{input.key}",
                          args=input.dict(exclude_none=True))


class ProjectsIdCustomattributesKeyDelete(BaseModel):
    id: int  # The ID of a resource

    key: str  # The key of the custom attribute


@action_store.kubiya_action()
def delete_custom_attribute_projects(input: ProjectsIdCustomattributesKeyDelete):
    return delete_wrapper(endpoint=f"/projects/{input.id}/custom_attributes/{input.key}",
                          args=input.dict(exclude_none=True))
