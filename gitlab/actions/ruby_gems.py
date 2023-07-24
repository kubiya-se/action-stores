from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class DownloadGemFile(BaseModel):
    id: Union[int, str] = Field(description="The ID or full path of the project.")
    file_name: str = Field(description="The name of the .gem file.")

@action_store.kubiya_action()
def download_a_gem_file(input: DownloadGemFile):
    return get_wrapper(endpoint=f"/projects/{input.id}/packages/rubygems/gems/{input.file_name}")

class FetchDependencies(BaseModel):
    id: Union[int, str] = Field(description="The ID or full path of the project.")
    gems: Optional[str] = Field(None, description="Comma-separated list of gems to fetch dependencies for.")

@action_store.kubiya_action()
def fetch_a_list_of_dependencies(input: FetchDependencies):
    return get_wrapper(endpoint=f"/projects/{input.id}/packages/rubygems/api/v1/dependencies", args=input.dict(exclude_none=True))


class UploadGemFile(BaseModel):
    id: Union[int, str] = Field(description="The ID or full path of the project.")
    file: bytes = Field(..., description="The .gem file to upload.")

@action_store.kubiya_action()
def upload_a_gem_file(input: UploadGemFile):
    # This will depend on how your `post_wrapper` function handles file uploads.
    # You may need to adjust this to match your actual upload handling code.
    return post_wrapper(endpoint=f"/projects/{input.id}/packages/rubygems/api/v1/gems", files={"file": input.file})
