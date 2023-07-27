from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.dashboard_annotations import *

@action_store.kubiya_action()
def create_new_annotation_in_environment(input: CreateNewAnnotation):
    return post_wrapper(endpoint=f'/environments/{input.id}/metrics_dashboard/annotations', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_new_annotation_in_cluster(input: CreateNewAnnotation):
    return post_wrapper(endpoint=f'/clusters/{input.id}/metrics_dashboard/annotations', args=input.dict(exclude_none=True))