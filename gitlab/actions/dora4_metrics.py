from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class ProjectsIdDoraMetrics(BaseModel):

    id: int # The ID or URL-encoded path of the project can be accessed by the authenticated user.

    metric: str # One of deployment_frequency, lead_time_for_changes, time_to_restore_service or change_failure_rate.

    end_date: Optional[str] = None # Date range to end at. ISO 8601 Date format, for example 2021-03-01. Default is the current date.

    environment_tiers: Optional[List[str]] = None # The tiers of the environments. Default is production.

    interval: Optional[str] = None # The bucketing interval. One of all, monthly or daily. Default is daily.

    start_date: Optional[str] = None # Date range to start from. ISO 8601 Date format, for example 2021-03-01. Default is 3 months ago.


@action_store.kubiya_action()
def get_project_level_dora_metrics(input: ProjectsIdDoraMetrics):
    return get_wrapper(endpoint=f"/projects/{input.id}/dora/metrics", args=input.dict(exclude_none=True))


class GroupsIdDoraMetrics(BaseModel):

    id: int # The ID or URL-encoded path of the project can be accessed by the authenticated user.

    metric: str # One of deployment_frequency, lead_time_for_changes, time_to_restore_service or change_failure_rate.


    end_date: Optional[str] = None # Date range to end at. ISO 8601 Date format, for example 2021-03-01. Default is the current date.

    environment_tiers: Optional[List[str]] = None # The tiers of the environments. Default is production.

    interval: Optional[str] = None # The bucketing interval. One of all, monthly or daily. Default is daily.

    start_date: Optional[str] = None # Date range to start from. ISO 8601 Date format, for example 2021-03-01. Default is 3 months ago.


@action_store.kubiya_action()
def get_group_level_dora_metrics(input: GroupsIdDoraMetrics):
    return get_wrapper(endpoint=f"/groups/{input.id}/dora/metrics", args=input.dict(exclude_none=True))

    