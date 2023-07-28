from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ProjectsIdMergerequestsMergerequestiidDraftnotes(BaseModel):
    id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidSingle(BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesCreate(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    note: str
    commit_id: Optional[str] = None
    in_reply_to_discussion_id: Optional[int] = None
    resolve_discussion: Optional[bool] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidModify(BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
    note: Optional[str] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidDelete(BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidPublish(BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesBulkpublish(BaseModel):
    id: Union[int, str]
    merge_request_iid: int