from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.version import *
@action_store.kubiya_action()
def retrieve_gitlab_instance_version_information(input=None):
    return get_wrapper(endpoint=f'/version', args=input)