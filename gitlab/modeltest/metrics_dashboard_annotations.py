from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class EnvironmentsIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str
class ClustersIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str