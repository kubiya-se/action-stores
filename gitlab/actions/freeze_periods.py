from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.freeze_periods import *
@action_store.kubiya_action()
def list_freeze_periods(input: ListFreezePeriods):
    return get_wrapper(endpoint=f'/projects/{input.id}/freeze_periods')
@action_store.kubiya_action()
def get_freeze_period_by_a_freeze_period_id(input: GetFreezePeriod):
    return get_wrapper(endpoint=f'/projects/{input.id}/freeze_periods/{input.freeze_period_id}')
@action_store.kubiya_action()
def create_a_freeze_period(input: CreateFreezePeriod):
    return post_wrapper(endpoint=f'/projects/{input.id}/freeze_periods', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_a_freeze_period(input: UpdateFreezePeriod):
    return put_wrapper(endpoint=f'/projects/{input.id}/freeze_periods/{input.freeze_period_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_freeze_period(input: DeleteFreezePeriod):
    return delete_wrapper(endpoint=f'/projects/{input.id}/freeze_periods/{input.freeze_period_id}')