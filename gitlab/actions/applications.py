from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.applications import *
@action_store.kubiya_action()
def create_an_application(input: Applications):
    return post_wrapper(endpoint=f'/applications', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_all_applications(input=None):
    return get_wrapper(endpoint=f'/applications', args=input)
@action_store.kubiya_action()
def delete_an_application(input: ApplicationsId):
    return delete_wrapper(endpoint=f'/applications/{input.id}', args=input.dict(exclude_none=True))