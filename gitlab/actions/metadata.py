from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.metadata import *
@action_store.kubiya_action()
def get_metadata():
    return get_wrapper(endpoint='/metadata')