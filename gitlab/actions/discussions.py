from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..main_store import action_store as action_store
from .http_wrapper import *
from datetime import datetime
from ..models.discussions import *
@action_store.kubiya_action()
def list_project_issue_discussion_items(input: ListProjectIssueDiscussionItems):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/discussions', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_single_issue_discussion_item(input: GetSingleIssueDiscussionItem):
    return get_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/discussions/{input.discussion_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_new_issue_thread(input: CreateNewIssueThread):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/discussions', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def add_note_to_existing_issue_thread(input: AddNoteToExistingIssueThreadPayload):
    return post_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/discussions/{input.discussion_id}/notes', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def modify_existing_issue_thread_note(input: ModifyExistingIssueThreadNote):
    return put_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/discussions/{input.discussion_id}/notes/{input.note_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_issue_thread_note(input: DeleteIssueThreadNote):
    return delete_wrapper(endpoint=f'/projects/{input.id}/issues/{input.issue_iid}/discussions/{input.discussion_id}/notes/{input.note_id}')
@action_store.kubiya_action()
def snippets(input: ProjectsIdSnippetsSnippetidDiscussions):
    return get_wrapper(endpoint=f'/projects/{input.id}/snippets/{input.snippet_id}/discussions', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_project_snippet_discussion_items(input: ListProjectSnippetDiscussionItems):
    return get_wrapper(endpoint=f'/projects/{input.id}/snippets/{input.snippet_id}/discussions')
@action_store.kubiya_action()
def get_single_snippet_discussion_item(input: GetSingleSnippetDiscussionItem):
    return get_wrapper(endpoint=f'/projects/{input.id}/snippets/{input.snippet_id}/discussions/{input.discussion_id}')
@action_store.kubiya_action()
def create_new_snippet_thread(input: CreateNewSnippetThread):
    return post_wrapper(endpoint=f'/projects/{input.id}/snippets/{input.snippet_id}/discussions', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def add_note_to_existing_snippet_thread(input: AddNoteToExistingSnippetThread):
    return post_wrapper(endpoint=f'/projects/{input.id}/snippets/{input.snippet_id}/discussions/{input.discussion_id}/notes', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def modify_existing_snippet_thread_note(input: ModifyExistingSnippetThreadNote):
    return put_wrapper(endpoint=f'/projects/{input.id}/snippets/{input.snippet_id}/discussions/{input.discussion_id}/notes/{input.note_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_snippet_thread_note(input: DeleteSnippetThreadNote):
    return delete_wrapper(endpoint=f'/projects/{input.id}/snippets/{input.snippet_id}/discussions/{input.discussion_id}/notes/{input.note_id}')
@action_store.kubiya_action()
def epics_(input: GroupsIdEpicsEpicidDiscussions):
    return get_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_id}/discussions', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_single_epic_discussion_item(input: SingleEpicDiscussionItem):
    return get_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_id}/discussions/{input.discussion_id}')
@action_store.kubiya_action()
def create_new_epic_thread(input: CreateNewEpicThread):
    return post_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_id}/discussions', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def add_note_to_epic_thread(input: AddNoteToEpicThread):
    return post_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_id}/discussions/{input.discussion_id}/notes', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def modify_epic_thread_note(input: ModifyEpicThreadNote):
    return put_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_id}/discussions/{input.discussion_id}/notes/{input.note_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_epic_thread_note(input: DeleteEpicThreadNote):
    return delete_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_id}/discussions/{input.discussion_id}/notes/{input.note_id}')
@action_store.kubiya_action()
def get_project_merge_request_discussion_items(input: ListMergeRequestDiscussionItems):
    return get_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/discussions')
@action_store.kubiya_action()
def create_new_merge_request_thread(input: CreateNewMergeRequestThread):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/discussions/', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def put_resolve_merge_request_thread(input: ResolveMergeRequestThread):
    return put_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/discussions/{input.discussion_id}?resolved={input.resolved}')
@action_store.kubiya_action()
def post_add_note_to_merge_request_thread(input: AddNoteToMergeRequestThread):
    return post_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/discussions/{input.discussion_id}/notes', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def put_modify_merge_request_thread_note(input: ModifyMergeRequestThreadNote):
    return put_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/discussions/{input.discussion_id}/notes/{input.note_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_merge_request_thread_note(input: DeleteMergeRequestThreadNote):
    return delete_wrapper(endpoint=f'/projects/{input.id}/merge_requests/{input.merge_request_iid}/discussions/{input.discussion_id}/notes/{input.note_id}')
@action_store.kubiya_action()
def get_project_commit_discussion_items(input: ListProjectCommitDiscussionItems):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.commit_id}/discussions')
@action_store.kubiya_action()
def get_single_commit_discussion_item(input: GetSingleCommitDiscussionItem):
    return get_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.commit_id}/discussions/{input.discussion_id}')
@action_store.kubiya_action()
def post_create_new_commit_thread(input: CreateNewCommitThread):
    return post_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.commit_id}/discussions', payload=input.dict())
@action_store.kubiya_action()
def post_add_note_to_commit_thread(input: AddNoteToCommitThread):
    return post_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.commit_id}/discussions/{input.discussion_id}/notes', payload=input.dict())
@action_store.kubiya_action()
def put_modify_commit_thread_note(input: ModifyCommitThreadNote):
    return put_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.commit_id}/discussions/{input.discussion_id}/notes/{input.note_id}', payload=input.dict())
@action_store.kubiya_action()
def delete_commit_thread_note(input: DeleteCommitThreadNote):
    return delete_wrapper(endpoint=f'/projects/{input.id}/repository/commits/{input.commit_id}/discussions/{input.discussion_id}/notes/{input.note_id}')