from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class AwardEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]

@action_store.kubiya_action()
def get_issue_emoji_reactions(input: AwardEmojiParams):
    endpoint = f"/projects/{input.id}/issues/{input.issue_iid}/award_emoji"
    return get_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def get_merge_request_emoji_reactions(input: AwardEmojiParams):
    endpoint = f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/award_emoji"
    return get_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def get_snippet_emoji_reactions(input: AwardEmojiParams):
    endpoint = f"/projects/{input.id}/snippets/{input.snippet_id}/award_emoji"
    return get_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))


class SingleEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int

@action_store.kubiya_action()
def get_single_issue_emoji_reaction(input: SingleEmojiReactionParams):
    endpoint = f"/projects/{input.id}/issues/{input.issue_iid}/award_emoji/{input.award_id}"
    return get_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def get_single_merge_request_emoji_reaction(input: SingleEmojiReactionParams):
    endpoint = f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/award_emoji/{input.award_id}"
    return get_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def get_single_snippet_emoji_reaction(input: SingleEmojiReactionParams):
    endpoint = f"/projects/{input.id}/snippets/{input.snippet_id}/award_emoji/{input.award_id}"
    return get_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))


class NewEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    name: str

@action_store.kubiya_action()
def add_new_issue_emoji_reaction(input: NewEmojiReactionParams):
    endpoint = f"/projects/{input.id}/issues/{input.issue_iid}/award_emoji"
    return post_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def add_new_merge_request_emoji_reaction(input: NewEmojiReactionParams):
    endpoint = f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/award_emoji"
    return post_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def add_new_snippet_emoji_reaction(input: NewEmojiReactionParams):
    endpoint = f"/projects/{input.id}/snippets/{input.snippet_id}/award_emoji"
    return post_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))


class DeleteEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int

@action_store.kubiya_action()
def delete_issue_emoji_reaction(input: DeleteEmojiReactionParams):
    endpoint = f"/projects/{input.id}/issues/{input.issue_iid}/award_emoji/{input.award_id}"
    return delete_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def delete_merge_request_emoji_reaction(input: DeleteEmojiReactionParams):
    endpoint = f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/award_emoji/{input.award_id}"
    return delete_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def delete_snippet_emoji_reaction(input: DeleteEmojiReactionParams):
    endpoint = f"/projects/{input.id}/snippets/{input.snippet_id}/award_emoji/{input.award_id}"
    return delete_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))

class ListCommentEmojiReactionsParams(BaseModel):
    id: Union[int, str] 
    issue_iid: int 
    note_id: int 

@action_store.kubiya_action()
def list_comment_emoji_reactions(input: ListCommentEmojiReactionsParams):
    endpoint = f"/projects/{input.id}/issues/{input.issue_iid}/notes/{input.note_id}/award_emoji"
    return get_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))

class GetCommentEmojiReactionParams(BaseModel):
    id: Union[int, str] 
    issue_iid: int 
    note_id: int 
    award_id: int 

@action_store.kubiya_action()
def get_comment_emoji_reaction(input: GetCommentEmojiReactionParams):
    endpoint = f"/projects/{input.id}/issues/{input.issue_iid}/notes/{input.note_id}/award_emoji/{input.award_id}"
    return get_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))

class AwardCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    name: str

@action_store.kubiya_action()
def award_comment_emoji(input: AwardCommentEmojiParams):
    endpoint = f"/projects/{input.id}/issues/{input.issue_iid}/notes/{input.note_id}/award_emoji"
    return post_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))

class DeleteCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int

@action_store.kubiya_action()
def delete_comment_emoji(input: DeleteCommentEmojiParams):
    endpoint = f"/projects/{input.id}/issues/{input.issue_iid}/notes/{input.note_id}/award_emoji/{input.award_id}"
    return delete_wrapper(endpoint=endpoint, args=input.dict(exclude_none=True))
