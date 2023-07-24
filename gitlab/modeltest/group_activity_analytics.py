from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class GroupActivityIssuesCount(BaseModel):
    group_path: str = Field(description='Group path')
class GroupActivityMergeRequestsCount(BaseModel):
    group_path: str = Field(description='Group path')
class GroupActivityNewMembersCount(BaseModel):
    group_path: str = Field(description='Group path')