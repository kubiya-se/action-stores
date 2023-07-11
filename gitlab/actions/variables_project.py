from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class Variable(BaseModel):
    key: str
    value: str
    variable_type: Optional[str] = 'env_var'
    protected: Optional[bool] = False
    masked: Optional[bool] = False
    raw: Optional[bool] = False
    environment_scope: Optional[str] = '*'
    description: Optional[str] = None

class VariableFilter(BaseModel):
    environment_scope: Optional[str] = None

class GetProjectVariables(BaseModel):
    id: Union[int, str]  # The ID or URL-encoded path of the project.

@action_store.kubiya_action()
def list_project_variables(input: GetProjectVariables):
    return get_wrapper(endpoint=f"/projects/{input.id}/variables", args=input.dict(exclude_none=True))

class GetVariable(BaseModel):
    id: Union[int, str]
    key: str
    filter: Optional[VariableFilter] = None

@action_store.kubiya_action()
def get_a_single_variable(input: GetVariable):
    return get_wrapper(endpoint=f"/projects/{input.id}/variables/{input.key}", args=input.dict(exclude_none=True))

class CreateVariable(GetProjectVariables, Variable):
    pass

@action_store.kubiya_action()
def create_a_variable(input: CreateVariable):
    return post_wrapper(endpoint=f"/projects/{input.id}/variables", args=input.dict(exclude_none=True))

class UpdateVariable(GetVariable, Variable):
    pass

@action_store.kubiya_action()
def update_a_variable(input: UpdateVariable):
    return put_wrapper(endpoint=f"/projects/{input.id}/variables/{input.key}", args=input.dict(exclude_none=True))

class DeleteVariable(GetVariable):
    pass

@action_store.kubiya_action()
def delete_a_variable(input: DeleteVariable):
    return delete_wrapper(endpoint=f"/projects/{input.id}/variables/{input.key}", args=input.dict(exclude_none=True))
