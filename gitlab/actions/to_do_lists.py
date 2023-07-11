from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class ListOfToDoItems(BaseModel):
    action: Optional[str] = None
    author_id: Optional[int] = None
    project_id: Optional[int] = None
    group_id: Optional[int] = None
    state: Optional[str] = None
    type: Optional[str] = None

@action_store.kubiya_action()
def get_a_list_of_todo_items(input: ListOfToDoItems):
    return get_wrapper(endpoint="/todos", args=input.dict(exclude_none=True))


class MarkAToDoItemAsDone(BaseModel):
    id: int

@action_store.kubiya_action()
def mark_a_todo_item_as_done(input: MarkAToDoItemAsDone):
    return post_wrapper(endpoint=f"/todos/{input.id}/mark_as_done")


@action_store.kubiya_action()
def mark_all_todo_items_as_done():
    return post_wrapper(endpoint="/todos/mark_as_done")