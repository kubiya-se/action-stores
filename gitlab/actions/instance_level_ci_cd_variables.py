from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.instance_level_ci_cd_variables import *
@action_store.kubiya_action()
def list_all_instance_variables():
    return get_wrapper(endpoint='/admin/ci/variables')
@action_store.kubiya_action()
def show_instance_variable(input: VariableKey):
    return get_wrapper(endpoint=f'/admin/ci/variables/{input.key}')
@action_store.kubiya_action()
def create_instance_variable(input: InstanceVariable):
    return post_wrapper(endpoint='/admin/ci/variables', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_instance_variable(input: InstanceVariable):
    return put_wrapper(endpoint=f'/admin/ci/variables/{input.key}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def remove_instance_variable(input: VariableKey):
    return delete_wrapper(endpoint=f'/admin/ci/variables/{input.key}')