from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ProjectsIdMetricsUserstarreddashboardsAdd(BaseModel):
    id: Union[int, str]
    dashboard_path: str
class ProjectsIdMetricsUserstarreddashboardsRemove(BaseModel):
    id: Union[int, str]
    dashboard_path: Optional[str] = None