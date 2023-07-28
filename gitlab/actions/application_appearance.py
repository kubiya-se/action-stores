from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.application_appearance import *

@action_store.kubiya_action()
def get_current_appearance_configuration():
    return get_wrapper(endpoint=f'/application/appearance', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def change_appearance_configuration(input: ApplicationAppearance):
    return put_wrapper(endpoint=f'/application/appearance', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def change_logo(input: ChangeLogo):
    return put_wrapper(endpoint=f'/application/appearance', args=input.dict(exclude_none=True))