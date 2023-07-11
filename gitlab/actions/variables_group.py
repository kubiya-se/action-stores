from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from enum import Enum

class ListGroupVariables(BaseModel):
    id: Union[int, str] #The ID of a group or URL-encoded path of the group

@action_store.kubiya_action()
def list_group_variables(input: ListGroupVariables):
    return get_wrapper(endpoint=f"/groups/{input.id}/variables", args=input.dict(exclude_none=True))

class VariableType(str, Enum):
    env_var = "env_var"
    file = "file"

class ShowGroupVariableDetails(BaseModel):
    id: Union[int, str] #The ID of a group or URL-encoded path of the group
    key: str = Field(..., max_length=255, regex="^[A-Za-z0-9_]+$")

@action_store.kubiya_action()
def show_group_variable_details(input: ShowGroupVariableDetails):
    return get_wrapper(endpoint=f"/groups/{input.id}/variables/{input.key}", args=input.dict(exclude_none=True))


class CreateGroupVariable(BaseModel):
    id: Union[int, str] #The ID of a group or URL-encoded path of the group
    key: str = Field(..., max_length=255, regex="^[A-Za-z0-9_]+$")
    value: str
    variable_type: Optional[VariableType] = None #The type of a variable. Available types are: env_var (default) and file
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None #Whether the variable is treated as a raw string. Default: false. When true, variables in the value are not expanded.
    environment_scope: Optional[str] = None 
    description: Optional[str] = None #The description of the variable. Default: null


@action_store.kubiya_action()
def create_group_variable(input: CreateGroupVariable):
    return post_wrapper(endpoint=f"/groups/{input.id}/variables", args=input.dict(exclude_none=True))


class UpdateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex="^[A-Za-z0-9_]+$")
    value: str
    variable_type: Optional[VariableType] = None #The type of a variable. Available types are: env_var (default) and file
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None #Whether the variable is treated as a raw string. Default: false. When true, variables in the value are not expanded.
    environment_scope: Optional[str] = None
    description: Optional[str] = None #The description of the variable. Default: null. Introduced in GitLab 16.2.


@action_store.kubiya_action()
def update_group_variable(input: UpdateGroupVariable):
    return put_wrapper(endpoint=f"/groups/{input.id}/variables/{input.key}", args=input.dict(exclude_none=True))


class RemoveGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex="^[A-Za-z0-9_]+$")

@action_store.kubiya_action()
def remove_group_variable(input: RemoveGroupVariable):
    return delete_wrapper(endpoint=f"/groups/{input.id}/variables/{input.key}", args=input.dict(exclude_none=True))