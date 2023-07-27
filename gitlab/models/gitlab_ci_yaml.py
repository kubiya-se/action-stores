from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ListAllCICDYamlTemplates(BaseModel):
    pass
class GetSingleCICDYamlTemplate(BaseModel):
    key: str