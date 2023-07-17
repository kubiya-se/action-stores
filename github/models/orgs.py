from typing import List, Any, Optional
from pydantic import BaseModel

class OrgParams(BaseModel):
    name: str