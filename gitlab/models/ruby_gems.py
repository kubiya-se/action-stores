from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class DownloadGemFile(BaseModel):
    id: Union[int, str] = Field(description='The ID or full path of the project.')
    file_name: str = Field(description='The name of the .gem file.')
class FetchDependencies(BaseModel):
    id: Union[int, str] = Field(description='The ID or full path of the project.')
    gems: Optional[str] = Field(None, description='Comma-separated list of gems to fetch dependencies for.')
class UploadGemFile(BaseModel):
    id: Union[int, str] = Field(description='The ID or full path of the project.')
    file: bytes = Field(..., description='The .gem file to upload.')