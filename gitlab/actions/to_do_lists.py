from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.to_do_lists import *
@action_store.kubiya_action()
def get_a_list_of_todo_items(input: ListOfToDoItems):
    return get_wrapper(endpoint='/todos', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def mark_a_todo_item_as_done(input: MarkAToDoItemAsDone):
    return post_wrapper(endpoint=f'/todos/{input.id}/mark_as_done')
@action_store.kubiya_action()
def mark_all_todo_items_as_done():
    return post_wrapper(endpoint='/todos/mark_as_done')