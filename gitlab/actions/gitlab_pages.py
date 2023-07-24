from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class ProjectsPagesDelete(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user.")


@action_store.kubiya_action()
def delete_project_pages(input: ProjectsPagesDelete):
    return delete_wrapper(endpoint=f"/projects/{input.id}/pages", args=input.dict(exclude_none=True))
