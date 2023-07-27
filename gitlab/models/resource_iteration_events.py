from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class IssueIterationEvents(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    issue_iid: int = Field(description='The IID of an issue.')
class SingleIssueIterationEvent(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    issue_iid: int = Field(description='The IID of an issue.')
    resource_iteration_event_id: int = Field(description='The ID of an iteration event.')