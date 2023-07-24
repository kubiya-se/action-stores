from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class ListIssuesForAnEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class AssignIssueToEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
    issue_id: Union[int, str]
class RemoveIssueFromEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
    epic_issue_id: Union[int, str]
class UpdateEpicIssueAssociation(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
    epic_issue_id: Union[int, str]
    move_before_id: Optional[Union[int, str]] = None
    move_after_id: Optional[Union[int, str]] = None