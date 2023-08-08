from typing import List, Any, Optional, Union, Dict, Union
from pydantic import BaseModel, Field
from datetime import datetime

class SingleDict(BaseModel):
    response: dict

class ProjectStatInput(BaseModel):
    id: Union[int,str]