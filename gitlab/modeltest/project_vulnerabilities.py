from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class ListProjectVulnerabilities(BaseModel):
    id: Union[int, str]
class NewVulnerability(BaseModel):
    id: Union[int, str]
    finding_id: Union[int, str]