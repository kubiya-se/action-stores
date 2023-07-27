from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.variables_group import *
@action_store.kubiya_action()
def list_group_variables(input: ListGroupVariables):
    return get_wrapper(endpoint=f'/groups/{input.id}/variables', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def show_group_variable_details(input: ShowGroupVariableDetails):
    return get_wrapper(endpoint=f'/groups/{input.id}/variables/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_group_variable(input: CreateGroupVariable):
    return post_wrapper(endpoint=f'/groups/{input.id}/variables', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_group_variable(input: UpdateGroupVariable):
    return put_wrapper(endpoint=f'/groups/{input.id}/variables/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def remove_group_variable(input: RemoveGroupVariable):
    return delete_wrapper(endpoint=f'/groups/{input.id}/variables/{input.key}', args=input.dict(exclude_none=True))