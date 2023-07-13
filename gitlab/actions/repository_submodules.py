
from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class UpdateSubmodule(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    submodule: str = Field(description="URL-encoded full path to the submodule.")
    branch: str = Field(description="Name of the branch to commit into.")
    commit_sha: str = Field(description="Full commit SHA to update the submodule to.")
    commit_message: Optional[str] = Field(None, description="Commit message. If no message is provided, a default is set")

@action_store.kubiya_action()
def update_existing_submodule_reference_in_repository(input: UpdateSubmodule):
    return put_wrapper(endpoint=f"/projects/{input.id}/repository/submodules/{input.submodule}", args=input.dict(exclude_none=True))
