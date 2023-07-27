from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.avatar import *

@action_store.kubiya_action()
def get_a_single_avatar_url(input: Avatar):
    return get_wrapper(endpoint=f'/avatar?email={input.email}', args=input.dict(exclude_none=True))