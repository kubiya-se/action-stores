from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.visual_review_discussions_deprecated import *
@action_store.kubiya_action()
def create_new_merge_request_thread(input: CreateNewMergeRequestThread):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/visual_review_discussions', args=input.dict(exclude_none=True))