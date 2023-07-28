from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ProjectsIdDependencies(BaseModel):
    id: Union[int, str]
    package_manager: Optional[str] = None