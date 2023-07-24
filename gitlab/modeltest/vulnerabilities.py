from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class VulnerabilitiesId(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdConfirm(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdResolve(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdDismiss(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdRevert(BaseModel):
    id: Union[int, str]