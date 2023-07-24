from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.broadcast_messages import *
@action_store.kubiya_action()
def get_all_broadcast_messages_():
    return get_wrapper(endpoint=f'/broadcast_messages', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_specific_broadcast_message_(input: GetASpecificBroadcastMessage):
    return get_wrapper(endpoint=f'/broadcast_messages/{input.id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_broadcast_message(input: CreateABroadcastMessage):
    return post_wrapper(endpoint=f'/broadcast_messages', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_a_broadcast_message(input: UpdateABroadcastMessage):
    return put_wrapper(endpoint=f'/broadcast_messages/{input.id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_broadcast_message(input: DeleteABroadcastMessage):
    return delete_wrapper(endpoint=f'/broadcast_messages/{input.id}', args=input.dict(exclude_none=True))