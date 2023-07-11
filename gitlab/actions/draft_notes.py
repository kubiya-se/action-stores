
from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class ProjectsIdMergerequestsMergerequestiidDraftnotes(BaseModel):

    id: int # The ID or URL-encoded path of the project

    merge_request_iid: int # The IID of a project merge request


@action_store.kubiya_action()
def list_all_merge_request_draft_notes(input: ProjectsIdMergerequestsMergerequestiidDraftnotes):
    return get_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/draft_notes", args=input.dict(exclude_none=True))


class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidSingle(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.
    draft_note_id: int # The ID of a draft note.

    merge_request_iid: int # The IID of a project merge request.


@action_store.kubiya_action()
def get_a_single_draft_note(input: ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidSingle):
    return get_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/draft_notes/{input.draft_note_id}", args=input.dict(exclude_none=True))


class ProjectsIdMergerequestsMergerequestiidDraftnotesCreate(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.
    merge_request_iid: int # The IID of a project merge request.

    note: str # The content of a note.

    commit_id: Optional[str] = None # The SHA of a commit to associate the draft note to.

    in_reply_to_discussion_id: Optional[int] = None # The ID of a discussion the draft note replies to.

    resolve_discussion: Optional[bool] = None # The associated discussion should be resolved.


@action_store.kubiya_action()
def create_a_draft_note(input: ProjectsIdMergerequestsMergerequestiidDraftnotesCreate):
    return post_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/draft_notes", args=input.dict(exclude_none=True))


class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidModify(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.
    draft_note_id: int # The ID of a draft note.

    merge_request_iid: int # The IID of a project merge request.

    note: Optional[str] = None # The content of a note.


@action_store.kubiya_action()
def modify_existing_draft_note(input: ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidModify):
    return put_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/draft_notes/{input.draft_note_id}", args=input.dict(exclude_none=True))


class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidDelete(BaseModel):

    draft_note_id: int # The ID of a draft note.

    id: Union[int, str] # The ID or URL-encoded path of the project.
    merge_request_iid: int # The IID of a project merge request.


@action_store.kubiya_action()
def delete_a_draft_note(input: ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidDelete):
    return delete_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/draft_notes/{input.draft_note_id}", args=input.dict(exclude_none=True))


class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidPublish(BaseModel):

    draft_note_id: int # The ID of a draft note.

    id: Union[int, str] # The ID or URL-encoded path of the project.
    merge_request_iid: int # The IID of a project merge request.


@action_store.kubiya_action()
def publish_a_draft_note(input: ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidPublish):
    return put_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/draft_notes/{input.draft_note_id}/publish", args=input.dict(exclude_none=True))


class ProjectsIdMergerequestsMergerequestiidDraftnotesBulkpublish(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.
    merge_request_iid: int # The IID of a project merge request.


@action_store.kubiya_action()
def publish_all_pending_draft_notes(input: ProjectsIdMergerequestsMergerequestiidDraftnotesBulkpublish):
    return post_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/draft_notes/bulk_publish", args=input.dict(exclude_none=True))
