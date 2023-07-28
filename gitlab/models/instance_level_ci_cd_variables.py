from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class InstanceVariable(BaseModel):
    key: str = Field(description='The key of a variable.')
    value: str = Field(description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description='The type of a variable.')
    protected: Optional[bool] = Field(None, description='Whether the variable is protected.')
    masked: Optional[bool] = Field(None, description='Whether the variable is masked.')
    raw: Optional[bool] = Field(None, description='Whether the variable is expandable.')
class VariableKey(BaseModel):
    key: str = Field(description='The key of a variable.')