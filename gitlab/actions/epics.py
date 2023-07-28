from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.epics import *
@action_store.kubiya_action()
def list_epics_for_a_group_0(input: GroupsIdEpics):
    return get_wrapper(endpoint=f'/groups/{input.id}/epics', args=input.dict(exclude_none=True, by_alias=True))
@action_store.kubiya_action()
def single_epic(input: SingleEpic):
    return get_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_iid}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def new_epic(input: NewEpicInput):
    return post_wrapper(endpoint=f'/groups/{input.id}/epics', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def update_epic(input: UpdateEpic):
    return put_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_iid}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_epic(input: DeleteEpic):
    return delete_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_iid}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_to_do_item(input: CreateAToDoItem):
    return post_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_iid}/todo', args=input.dict(exclude_none=True))