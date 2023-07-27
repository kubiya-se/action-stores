from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.experiments import *
@action_store.kubiya_action()
def list_all_experiments(input: ListAllExperiments):
    return get_wrapper(endpoint=f'/experiments', args=input.dict(exclude_none=True))