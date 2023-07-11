from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class Avatar(BaseModel):
    email: str # Public email address of the user.
    size: Optional[int] = None # Single pixel dimension (because images are squares). Only used for avatar lookups at Gravatar or at the configured Libravatar server.

@action_store.kubiya_action()
def get_a_single_avatar_url(input: Avatar):
    return get_wrapper(endpoint=f"/avatar?email={input.email}", args=input.dict(exclude_none=True))