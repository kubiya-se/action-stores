from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.variables_project import *
@action_store.kubiya_action()
def list_project_variables(input: GetProjectVariables):
    return get_wrapper(endpoint=f'/projects/{input.id}/variables', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_single_variable(input: GetVariable):
    return get_wrapper(endpoint=f'/projects/{input.id}/variables/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_variable(input: CreateVariable):
    return post_wrapper(endpoint=f'/projects/{input.id}/variables', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_a_variable(input: UpdateVariable):
    return put_wrapper(endpoint=f'/projects/{input.id}/variables/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_variable(input: DeleteVariable):
    return delete_wrapper(endpoint=f'/projects/{input.id}/variables/{input.key}', args=input.dict(exclude_none=True))