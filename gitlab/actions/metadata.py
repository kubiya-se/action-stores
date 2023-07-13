from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

@action_store.kubiya_action()
def get_metadata():
    return get_wrapper(endpoint="/metadata")
    