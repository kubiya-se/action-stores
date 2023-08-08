from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime
from ..models.variables_group import *

from .. import action_store as action_store
from ..http_wrapper import *


@action_store.kubiya_action()
def list_group_variables(input: ListGroupVariables):
    response = get_wrapper(endpoint=f'/groups/{input.id}/variables', args=input.dict(exclude_none=True))
    return ListDict(response=response)

@action_store.kubiya_action()
def show_group_variable_details(input: ShowGroupVariableDetails):
    response = get_wrapper(endpoint=f'/groups/{input.id}/variables/{input.key}', args=input.dict(exclude_none=True))
    return SingleDict(response=response)

@action_store.kubiya_action()
def create_group_variable(input: CreateGroupVariable):
    response = post_wrapper(endpoint=f'/groups/{input.id}/variables', args=input.dict(exclude_none=True))
    return SingleDict(response=response)

@action_store.kubiya_action()
def update_group_variable(input: UpdateGroupVariable):
    response = put_wrapper(endpoint=f'/groups/{input.id}/variables/{input.key}', args=input.dict(exclude_none=True))
    return SingleDict(response=response)

@action_store.kubiya_action()
def remove_group_variable(input: RemoveGroupVariable):
    return delete_wrapper(endpoint=f'/groups/{input.id}/variables/{input.key}', args=input.dict(exclude_none=True))