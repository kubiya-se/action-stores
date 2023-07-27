from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ListMetricImages(BaseModel):
    id: int
    alert_iid: int
class UpdateMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int
    url: Optional[str] = None
    url_text: Optional[str] = None
class DeleteMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int