from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.draft_notes import *
@action_store.kubiya_action()
def list_all_merge_request_draft_notes(input: ProjectsIdMergerequestsMergerequestiidDraftnotes):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/draft_notes', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_single_draft_note(input: ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidSingle):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/draft_notes/{input.draft_note_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_draft_note(input: ProjectsIdMergerequestsMergerequestiidDraftnotesCreate):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/draft_notes', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def modify_existing_draft_note(input: ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidModify):
    return put_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/draft_notes/{input.draft_note_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_draft_note(input: ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidDelete):
    return delete_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/draft_notes/{input.draft_note_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def publish_a_draft_note(input: ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidPublish):
    return put_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/draft_notes/{input.draft_note_id}/publish', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def publish_all_pending_draft_notes(input: ProjectsIdMergerequestsMergerequestiidDraftnotesBulkpublish):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/draft_notes/bulk_publish', args=input.dict(exclude_none=True))