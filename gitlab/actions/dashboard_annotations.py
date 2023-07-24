from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field, validator
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

from typing import Optional

class CreateNewAnnotation(BaseModel):
    id: Union[int,str]  # The ID or URL-encoded path of the environment or cluster
    dashboard_path: str  # ID of the dashboard which needs to be annotated. Treated as a CGI-escaped path, and automatically un-escaped.
    starting_at: str  # Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Timestamp marking start point of annotation.
    ending_at: Optional[str] = None  # Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Timestamp marking end point of annotation. When not supplied, an annotation displays as a single event at the start point.
    description: str  # Description of the annotation.

    @validator('starting_at', 'ending_at', pre=True)
    def parse_iso8601(cls, v):
        if v is None:
            return v
        try:
            return datetime.fromisoformat(v)
        except ValueError:
            raise ValueError("datetime is not in ISO 8601 format")

@action_store.kubiya_action()
def create_new_annotation_in_environment(input: CreateNewAnnotation):
    return post_wrapper(endpoint=f"/environments/{input.id}/metrics_dashboard/annotations", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def create_new_annotation_in_cluster(input: CreateNewAnnotation):
    return post_wrapper(endpoint=f"/clusters/{input.id}/metrics_dashboard/annotations", args=input.dict(exclude_none=True))
