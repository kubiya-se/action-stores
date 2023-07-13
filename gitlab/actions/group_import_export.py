from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class GroupExport(BaseModel):
    id: Union[int, str] = Field(description="ID of the group owned by the authenticated user.")

@action_store.kubiya_action()
def schedule_new_export(input: GroupExport):
    return post_wrapper(endpoint=f"/groups/{input.id}/export", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def download_export(input: GroupExport):
    return get_wrapper(endpoint=f"/groups/{input.id}/export/download", args=input.dict(exclude_none=True))


class GroupImport(BaseModel):
    name: str = Field(description="The name of the group to be imported")
    path: str = Field(description="Name and path for new group")
    file: str = Field(description="The file to be uploaded")
    parent_id: Optional[int] = Field(None, description="ID of a parent group to import the group into. Defaults to the current user’s namespace if not provided.")

@action_store.kubiya_action()
def import_group(input: GroupImport):
    return post_wrapper(endpoint="/groups/import", args=input.dict(exclude_none=True))