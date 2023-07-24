from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime


@action_store.kubiya_action()
def get_all_broadcast_messages_():
    return get_wrapper(endpoint=f"/broadcast_messages", args=input.dict(exclude_none=True))


class GetASpecificBroadcastMessage(BaseModel):
    id: int  # The ID of the broadcast message


@action_store.kubiya_action()
def get_a_specific_broadcast_message_(input: GetASpecificBroadcastMessage):
    return get_wrapper(endpoint=f"/broadcast_messages/{input.id}", args=input.dict(exclude_none=True))


class CreateABroadcastMessage(BaseModel):
    message: str  # Message to display.
    starts_at: Optional[datetime]  # Starting time. Expected in ISO 8601 format.
    ends_at: Optional[datetime]  # Ending time. Expected in ISO 8601 format.
    font: Optional[str]  # Foreground color hex code.
    target_access_levels: Optional[List[int]]  # Target access levels (roles) of the broadcast message.
    target_path: Optional[str]  # Target path of the broadcast message.
    broadcast_type: Optional[str]  # Appearance type (defaults to banner)
    dismissable: Optional[bool]  # Can the user dismiss the message?

@action_store.kubiya_action()
def create_a_broadcast_message(input: CreateABroadcastMessage):
    return post_wrapper(endpoint=f"/broadcast_messages", args=input.dict(exclude_none=True))


class UpdateABroadcastMessage(BaseModel):
    id: int  # ID of broadcast message to update.
    message: Optional[str]  # Message to display.
    starts_at: Optional[datetime]  # Starting time. Expected in ISO 8601 format.
    ends_at: Optional[datetime]  # Ending time. Expected in ISO 8601 format.
    font: Optional[str]  # Foreground color hex code.
    target_access_levels: Optional[List[int]]  # Target access levels (roles) of the broadcast message.
    target_path: Optional[str]  # Target path of the broadcast message.
    broadcast_type: Optional[str]  # Appearance type (defaults to banner)
    dismissable: Optional[bool]  # Can the user dismiss the message?


@action_store.kubiya_action()
def update_a_broadcast_message(input: UpdateABroadcastMessage):
    return put_wrapper(endpoint=f"/broadcast_messages/{input.id}", args=input.dict(exclude_none=True))


class DeleteABroadcastMessage(BaseModel):
    id: int #ID of the broadcast message to delete

@action_store.kubiya_action()
def delete_a_broadcast_message(input: DeleteABroadcastMessage):
    return delete_wrapper(endpoint=f"/broadcast_messages/{input.id}", args=input.dict(exclude_none=True))