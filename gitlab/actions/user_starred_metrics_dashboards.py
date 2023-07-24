from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime


class ProjectsIdMetricsUserstarreddashboardsAdd(BaseModel):
    id: Union[int,str] # The ID or URL-encoded path of the project
    dashboard_path: str  # URL-encoded path to file defining the dashboard which should be marked as favorite.

@action_store.kubiya_action()
def add_a_star_to_a_dashboard(input: ProjectsIdMetricsUserstarreddashboardsAdd):
    return post_wrapper(endpoint=f"/projects/{input.id}/metrics/user_starred_dashboards",args=input.dict(exclude_none=True))


class ProjectsIdMetricsUserstarreddashboardsRemove(BaseModel):
    id: Union[int,str] # The ID or URL-encoded path of the project
    dashboard_path: Optional[str] = None  # URL-encoded path to file defining the dashboard which should be marked as favorite.

@action_store.kubiya_action()
def remove_a_star_from_a_dashboard(input: ProjectsIdMetricsUserstarreddashboardsRemove):
    return delete_wrapper(endpoint=f"/projects/{input.id}/metrics/user_starred_dashboards", args=input.dict(exclude_none=True))
