from typing import List, Any, Optional, Union
from pydantic import BaseModel
from datetime import datetime
from ..models.dora4_metrics import *

from .. import action_store as action_store
from ..http_wrapper import *


@action_store.kubiya_action()
def get_project_level_dora_metrics(input: ProjectsIdDoraMetrics):
    response = get_wrapper(endpoint=f'/projects/{input.id}/dora/metrics', args=input.dict(exclude_none=True))
    return ListDict(response=response)
@action_store.kubiya_action()
def get_group_level_dora_metrics(input: GroupsIdDoraMetrics):
    response = get_wrapper(endpoint=f'/groups/{input.id}/dora/metrics', args=input.dict(exclude_none=True))
    return ListDict(response=response)