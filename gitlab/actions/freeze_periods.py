from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime


class ListFreezePeriods(BaseModel):
    id: Union[int, str]  # The ID or URL-encoded path of the project.

@action_store.kubiya_action()
def list_freeze_periods(input: ListFreezePeriods):
    return get_wrapper(endpoint=f"/projects/{input.id}/freeze_periods")

class GetFreezePeriod(BaseModel):
    id: Union[int, str]  # The ID or URL-encoded path of the project.
    freeze_period_id: int  # The ID of the freeze period.

@action_store.kubiya_action()
def get_freeze_period_by_a_freeze_period_id(input: GetFreezePeriod):
    return get_wrapper(endpoint=f"/projects/{input.id}/freeze_periods/{input.freeze_period_id}")

class CreateFreezePeriod(BaseModel):
    id: Union[int, str]  # The ID or URL-encoded path of the project.
    freeze_start: str  # Start of the freeze period in cron format.
    freeze_end: str  # End of the freeze period in cron format.
    cron_timezone: Optional[str] = None  # The time zone for the cron fields, defaults to UTC if not provided.

@action_store.kubiya_action()
def create_a_freeze_period(input: CreateFreezePeriod):
    return post_wrapper(endpoint=f"/projects/{input.id}/freeze_periods", args=input.dict(exclude_none=True))

class UpdateFreezePeriod(BaseModel):
    id: Union[int, str]  # The ID or URL-encoded path of the project.
    freeze_period_id: int  # The ID of the freeze period.
    freeze_start: Optional[str] = None  # Start of the freeze period in cron format.
    freeze_end: Optional[str] = None  # End of the freeze period in cron format.
    cron_timezone: Optional[str] = None  # The time zone for the cron fields.

@action_store.kubiya_action()
def update_a_freeze_period(input: UpdateFreezePeriod):
    return put_wrapper(endpoint=f"/projects/{input.id}/freeze_periods/{input.freeze_period_id}", args=input.dict(exclude_none=True))

class DeleteFreezePeriod(BaseModel):
    id: Union[int, str]  # The ID or URL-encoded path of the project.
    freeze_period_id: int  # The ID of the freeze period.

@action_store.kubiya_action()
def delete_a_freeze_period(input: DeleteFreezePeriod):
    return delete_wrapper(endpoint=f"/projects/{input.id}/freeze_periods/{input.freeze_period_id}")
