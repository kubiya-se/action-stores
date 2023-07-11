from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class EnvironmentsIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str  # 	ID of the dashboard which needs to be annotated. Treated as a CGI-escaped path, and automatically un-escaped.
    starting_at: str  # 	Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Timestamp marking start point of annotation.
    ending_at: Optional[str]  # 	Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Timestamp marking end point of annotation. When not supplied, an annotation displays as a single event at the start point.
    description: str  # 	Description of the annotation.
@action_store.kubiya_action()
def create_a_new_annotation_environments(input: EnvironmentsIdMetricsdashboardAnnotations):
    return post_wrapper(endpoint=f"/environments/{input.id}/metrics_dashboard/annotations/", args=input.dict(exclude_none=True))


class ClustersIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str  # 	ID of the dashboard which needs to be annotated. Treated as a CGI-escaped path, and automatically un-escaped.
    starting_at: str  # 	Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Timestamp marking start point of annotation.
    ending_at: Optional[str]  # 	Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Timestamp marking end point of annotation. When not supplied, an annotation displays as a single event at the start point.
    description: str  # 	Description of the annotation.

@action_store.kubiya_action()
def create_a_new_annotation_clusters(input: ClustersIdMetricsdashboardAnnotations):
    return post_wrapper(endpoint=f"/clusters/{input.id}/metrics_dashboard/annotations/", args=input.dict(exclude_none=True))


