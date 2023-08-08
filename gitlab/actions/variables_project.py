from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime
from ..models.variables_project import *

from .. import action_store as action_store
from ..http_wrapper import *


@action_store.kubiya_action()
def list_project_variables(input: GetProjectVariables):
    response = get_wrapper(endpoint=f'/projects/{input.id}/variables', args=input.dict(exclude_none=True))
    return ListDict(response=response)

@action_store.kubiya_action()
def get_a_single_variable(input: GetVariable):
    response = get_wrapper(endpoint=f'/projects/{input.id}/variables/{input.key}', args=input.dict(exclude_none=True))
    return SingleDict(response=response)

@action_store.kubiya_action()
def create_a_variable(input: CreateVariable):
    response = post_wrapper(endpoint=f'/projects/{input.id}/variables', args=input.dict(exclude_none=True))
    return SingleDict(response=response)

@action_store.kubiya_action()
def update_a_variable(input: UpdateVariable):
    response = put_wrapper(endpoint=f'/projects/{input.id}/variables/{input.key}', args=input.dict(exclude_none=True))
    return SingleDict(response=response)

@action_store.kubiya_action()
def delete_a_variable(input: DeleteVariable):
    return delete_wrapper(endpoint=f'/projects/{input.id}/variables/{input.key}', args=input.dict(exclude_none=True))