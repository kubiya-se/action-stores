from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class Strategies(str, Enum):
    name = 'name'
    id = 'id'
    _destroy = '_destroy'
    parameters = 'parameters'
    scopes = 'scopes'
    scopes_id = 'scopes:d'
class UpdateAFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
    description: Optional[str]
    active: Optional[bool]
    name: Optional[str]
    strategies: List[Strategies]