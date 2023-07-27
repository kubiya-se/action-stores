from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class AwardEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
class SingleEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class NewEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    name: str
class DeleteEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class ListCommentEmojiReactionsParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
class GetCommentEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int
class AwardCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    name: str
class DeleteCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int