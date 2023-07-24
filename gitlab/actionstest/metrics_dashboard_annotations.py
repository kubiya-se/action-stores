from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.metrics_dashboard_annotations import *
@action_store.kubiya_action()
def create_a_new_annotation_environments(input: EnvironmentsIdMetricsdashboardAnnotations):
    return post_wrapper(endpoint=f'/environments/{input.id}/metrics_dashboard/annotations/', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_new_annotation_clusters(input: ClustersIdMetricsdashboardAnnotations):
    return post_wrapper(endpoint=f'/clusters/{input.id}/metrics_dashboard/annotations/', args=input.dict(exclude_none=True))