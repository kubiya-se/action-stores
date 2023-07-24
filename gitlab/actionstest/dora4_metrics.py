from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.dora4_metrics import *
@action_store.kubiya_action()
def get_project_level_dora_metrics(input: ProjectsIdDoraMetrics):
    return get_wrapper(endpoint=f'/projects/{input.id}/dora/metrics', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_group_level_dora_metrics(input: GroupsIdDoraMetrics):
    return get_wrapper(endpoint=f'/groups/{input.id}/dora/metrics', args=input.dict(exclude_none=True))