from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.user_starred_metrics_dashboards import *
@action_store.kubiya_action()
def add_a_star_to_a_dashboard(input: ProjectsIdMetricsUserstarreddashboardsAdd):
    return post_wrapper(endpoint=f'/projects/{input.id}/metrics/user_starred_dashboards', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def remove_a_star_from_a_dashboard(input: ProjectsIdMetricsUserstarreddashboardsRemove):
    return delete_wrapper(endpoint=f'/projects/{input.id}/metrics/user_starred_dashboards', args=input.dict(exclude_none=True))