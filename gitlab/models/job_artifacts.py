from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class GetJobArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int
    job_token: Optional[str] = None
class DownloadArtifacts(BaseModel):
    id: Union[int, str]
    ref_name: str
    job: str
    job_token: Optional[str] = None
class DownloadSingleArtifactByJobID(BaseModel):
    id: Union[int, str]
    job_id: int
    artifact_path: str
    job_token: Optional[str] = None
class DownloadSingleArtifactFromSpecificTag(BaseModel):
    id: Union[int, str]
    ref_name: str
    artifact_path: str
    job: str
    job_token: Optional[str] = None
class KeepArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int