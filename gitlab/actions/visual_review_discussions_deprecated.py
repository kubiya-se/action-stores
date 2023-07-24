from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime


class PositionData(BaseModel):
    base_sha: str  # Base commit SHA in the source branch
    start_sha: str  # SHA referencing commit in target branch
    head_sha: str  # SHA referencing HEAD of this merge request
    position_type: str  # Type of the position reference. Either text or image.
    new_path: Optional[str] = None  # File path after change
    new_line: Optional[int] = None  # Line number after change (Only stored for text diff notes)
    old_path: Optional[str] = None  # File path before change
    old_line: Optional[int] = None  # Line number before change (Only stored for text diff notes)
    width: Optional[int] = None  # Width of the image (Only stored for image diff notes)
    height: Optional[int] = None  # Height of the image (Only stored for image diff notes)
    x: Optional[int] = None  # X coordinate (Only stored for image diff notes)
    y: Optional[int] = None  # Y coordinate (Only stored for image diff notes)

class CreateNewMergeRequestThread(BaseModel):
    id: Union[int,str]  # The ID or URL-encoded path of the project
    merge_request_iid: int  # The IID of a merge request
    body: str  # The content of the thread
    position: Optional[PositionData] = None  # Position when creating a diff note

@action_store.kubiya_action()
def create_new_merge_request_thread(input: CreateNewMergeRequestThread):
    return post_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/visual_review_discussions", args=input.dict(exclude_none=True))
