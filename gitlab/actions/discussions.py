from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class ListProjectIssueDiscussionItems(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.#
    issue_iid: int # The IID of an issue.

@action_store.kubiya_action()
def list_project_issue_discussion_items(input: ListProjectIssueDiscussionItems):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/discussions", args=input.dict(exclude_none=True))


class GetSingleIssueDiscussionItem(BaseModel):
    id: Union[int,str]
    issue_iid: int
    discussion_id: int

@action_store.kubiya_action()
def get_single_issue_discussion_item(input: GetSingleIssueDiscussionItem):
    return get_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/discussions/{input.discussion_id}", args=input.dict(exclude_none=True))


class CreateNewIssueThread(BaseModel):
    body: str
    id: Union[int,str]
    issue_iid: int
    created_at: Optional[Union[str, datetime]]

@action_store.kubiya_action()
def create_new_issue_thread(input: CreateNewIssueThread):
    return post_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/discussions", args=input.dict(exclude_none=True))


class AddNoteToExistingIssueThreadPayload(BaseModel):
    body: str = Field(..., description="The content of the note or reply.")
    discussion_id: int = Field(..., description="The ID of a thread.")
    id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project.")
    issue_iid: int = Field(..., description="The IID of an issue.")
    note_id: int = Field(..., description="The ID of a thread note.")
    created_at: Optional[datetime] = Field(
        None, 
        description="Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights."
    )

@action_store.kubiya_action()
def add_note_to_existing_issue_thread(input: AddNoteToExistingIssueThreadPayload):
    return post_wrapper(
        endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/discussions/{input.discussion_id}/notes", 
        args=input.dict(exclude_none=True)
    )


class ModifyExistingIssueThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int,str]
    issue_iid: int
    note_id: int

@action_store.kubiya_action()
def modify_existing_issue_thread_note(input: ModifyExistingIssueThreadNote):
    return put_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/discussions/{input.discussion_id}/notes/{input.note_id}", args=input.dict(exclude_none=True))


class DeleteIssueThreadNote(BaseModel):
    id: Union[int,str]
    issue_iid: int
    discussion_id: int
    note_id: int

@action_store.kubiya_action()
def delete_issue_thread_note(input: DeleteIssueThreadNote):
    return delete_wrapper(endpoint=f"/projects/{input.id}/issues/{input.issue_iid}/discussions/{input.discussion_id}/notes/{input.note_id}")


class ProjectsIdSnippetsSnippetidDiscussions(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.#
    snippet_id: int # The ID of an snippet.

@action_store.kubiya_action()
def snippets(input: ProjectsIdSnippetsSnippetidDiscussions):
    return get_wrapper(endpoint=f"/projects/{input.id}/snippets/{input.snippet_id}/discussions", args=input.dict(exclude_none=True))


class ListProjectSnippetDiscussionItems(BaseModel):
    id: Union[int, str]
    snippet_id: int

@action_store.kubiya_action()
def list_project_snippet_discussion_items(input: ListProjectSnippetDiscussionItems):
    return get_wrapper(endpoint=f"/projects/{input.id}/snippets/{input.snippet_id}/discussions")


class GetSingleSnippetDiscussionItem(BaseModel):
    id: Union[int, str]
    snippet_id: int
    discussion_id: int

@action_store.kubiya_action()
def get_single_snippet_discussion_item(input: GetSingleSnippetDiscussionItem):
    return get_wrapper(endpoint=f"/projects/{input.id}/snippets/{input.snippet_id}/discussions/{input.discussion_id}")


class CreateNewSnippetThread(BaseModel):
    body: str
    id: Union[int, str]
    snippet_id: int
    created_at: Optional[Union[str, datetime]]

@action_store.kubiya_action()
def create_new_snippet_thread(input: CreateNewSnippetThread):
    return post_wrapper(endpoint=f"/projects/{input.id}/snippets/{input.snippet_id}/discussions", args=input.dict(exclude_none=True))

class AddNoteToExistingSnippetThread(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
    created_at: Optional[Union[str, datetime]]

@action_store.kubiya_action()
def add_note_to_existing_snippet_thread(input: AddNoteToExistingSnippetThread):
    return post_wrapper(endpoint=f"/projects/{input.id}/snippets/{input.snippet_id}/discussions/{input.discussion_id}/notes", args=input.dict(exclude_none=True))


class ModifyExistingSnippetThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int

@action_store.kubiya_action()
def modify_existing_snippet_thread_note(input: ModifyExistingSnippetThreadNote):
    return put_wrapper(endpoint=f"/projects/{input.id}/snippets/{input.snippet_id}/discussions/{input.discussion_id}/notes/{input.note_id}", args=input.dict(exclude_none=True))


class DeleteSnippetThreadNote(BaseModel):
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int

@action_store.kubiya_action()
def delete_snippet_thread_note(input: DeleteSnippetThreadNote):
    return delete_wrapper(endpoint=f"/projects/{input.id}/snippets/{input.snippet_id}/discussions/{input.discussion_id}/notes/{input.note_id}")



class GroupsIdEpicsEpicidDiscussions(BaseModel):

    epic_id: int # The ID of an epic.

    id: Union[int, str] # The ID or URL-encoded path of the group.

@action_store.kubiya_action()
def epics_(input: GroupsIdEpicsEpicidDiscussions):
    return get_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_id}/discussions", args=input.dict(exclude_none=True))



# Get single epic discussion item
class SingleEpicDiscussionItem(BaseModel):
    discussion_id: int = Field( description="The ID of a discussion item.")
    epic_id: int = Field( description="The ID of an epic.")
    id: Union[int, str] = Field( description="The ID or URL-encoded path of the group.")

@action_store.kubiya_action()
def get_single_epic_discussion_item(input: SingleEpicDiscussionItem):
    return get_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_id}/discussions/{input.discussion_id}")

# Create new epic thread
class CreateNewEpicThread(BaseModel):
    body: str = Field( description="The content of the thread.")
    epic_id: int = Field( description="The ID of an epic.")
    id: Union[int, str] = Field( description="The ID or URL-encoded path of the group.")
    created_at: Optional[Union[str, datetime]] = Field(None, description="Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.")

@action_store.kubiya_action()
def create_new_epic_thread(input: CreateNewEpicThread):
    return post_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_id}/discussions", args=input.dict(exclude_none=True))

# Add note to existing epic thread
class AddNoteToEpicThread(BaseModel):
    body: str = Field(description="The content of the note or reply.")
    discussion_id: int = Field( description="The ID of a thread.")
    epic_id: int = Field(description="The ID of an epic.")
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group.")
    note_id: int = Field(description="The ID of a thread note.")
    created_at: Optional[Union[str, datetime]] = Field(None, description="Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.")

@action_store.kubiya_action()
def add_note_to_epic_thread(input: AddNoteToEpicThread):
    return post_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_id}/discussions/{input.discussion_id}/notes", args=input.dict(exclude_none=True))

# Modify existing epic thread note
class ModifyEpicThreadNote(BaseModel):
    body: str = Field(description="The content of note or reply.")
    discussion_id: int = Field( description="The ID of a thread.")
    epic_id: int = Field( description="The ID of an epic.")
    id: Union[int, str] = Field( description="The ID or URL-encoded path of the group.")
    note_id: int = Field( description="The ID of a thread note.")

@action_store.kubiya_action()
def modify_epic_thread_note(input: ModifyEpicThreadNote):
    return put_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_id}/discussions/{input.discussion_id}/notes/{input.note_id}", args=input.dict(exclude_none=True))

# Delete an epic thread note
class DeleteEpicThreadNote(BaseModel):
    discussion_id: int = Field(description="The ID of a thread.")
    epic_id: int = Field( description="The ID of an epic.")
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the group.")
    note_id: int = Field(description="The ID of a thread note.")

@action_store.kubiya_action()
def delete_epic_thread_note(input: DeleteEpicThreadNote):
    return delete_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_id}/discussions/{input.discussion_id}/notes/{input.note_id}")

class ListMergeRequestDiscussionItems(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    merge_request_iid: int = Field(description="The IID of a merge request.")

@action_store.kubiya_action()
def get_project_merge_request_discussion_items(input: ListMergeRequestDiscussionItems):
    return get_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/discussions")

# Get single merge request discussion item
class SingleMergeRequestDiscussionItem(BaseModel):
    discussion_id: str = Field(description="The ID of a discussion item.")
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    merge_request_iid: int = Field(description="The IID of a merge request.")


# Basic parameters for all comments
class BasicMergeRequestParams(BaseModel):
    body: str = Field(description="The content of the thread.")
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    merge_request_iid: int = Field(description="The IID of a merge request.")

# Parameters for diff notes
class DiffNoteParams(BaseModel):
    base_sha: str = Field(description="Base commit SHA in the source branch.")
    head_sha: str = Field(description="SHA referencing HEAD of this merge request.")
    start_sha: str = Field(description="SHA referencing commit in target branch.")
    new_path: str = Field(description="File path after change.")
    old_path: str = Field(description="File path before change.")
    position_type: str = Field(description="Type of the position reference. Allowed values: text or image.")

# Parameters for text diff notes
class TextDiffNoteParams(BaseModel):
    new_line: Optional[int] = Field(description="For text diff notes, the line number after change.")
    old_line: Optional[int] = Field(description="For text diff notes, the line number before change.")

# Parameters for image diff notes
class ImageDiffNoteParams(BaseModel):
    width: Optional[int] = Field(description="For image diff notes, width of the image.")
    height: Optional[int] = Field(description="For image diff notes, height of the image.")
    x: Optional[float] = Field(description="For image diff notes, X coordinate.")
    y: Optional[float] = Field(description="For image diff notes, Y coordinate.")

# Parameters for multiline comments
class MultilineCommentsParams(BaseModel):
    line_range: dict = Field(description="Line range for a multi-line diff note.")

# Create new merge request thread input model
class CreateNewMergeRequestThread(BasicMergeRequestParams):
    position: DiffNoteParams = Field(description="Position when creating a diff note.")
    text_position: Optional[TextDiffNoteParams] = Field(description="Position parameters for text diff notes.")
    image_position: Optional[ImageDiffNoteParams] = Field(description="Position parameters for image diff notes.")
    multiline_comments: Optional[MultilineCommentsParams] = Field(description="Parameters for multiline comments.")
    commit_id: Optional[str] = Field(description="SHA referencing commit to start this thread on.")
    created_at: Optional[str] = Field(description="Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.")

@action_store.kubiya_action()
def create_new_merge_request_thread(input: CreateNewMergeRequestThread):
    return post_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/discussions/", args=input.dict(exclude_none=True))

# Resolve a merge request thread
class ResolveMergeRequestThread(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    merge_request_iid: int = Field(description="The IID of a merge request.")
    discussion_id: str = Field(description="The ID of a thread.")
    resolved: bool = Field(description="Resolve or unresolve the discussion.")

@action_store.kubiya_action()
def put_resolve_merge_request_thread(input: ResolveMergeRequestThread):
    return put_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/discussions/{input.discussion_id}?resolved={input.resolved}")




# Add note to existing merge request thread
class AddNoteToMergeRequestThread(BaseModel):
    body: str = Field(description="The content of the note or reply.")
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    discussion_id: str = Field(description="The ID of a thread.")
    merge_request_iid: int = Field(description="The IID of a merge request.")
    note_id: int = Field(description="The ID of a thread note.")
    created_at: Optional[str] = Field(description="Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.")

@action_store.kubiya_action()
def post_add_note_to_merge_request_thread(input: AddNoteToMergeRequestThread):
    return post_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/discussions/{input.discussion_id}/notes", args=input.dict(exclude_none=True))


# Modify an existing merge request thread note
class ModifyMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description="The ID of a thread.")
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    merge_request_iid: int = Field(description="The IID of a merge request.")
    note_id: int = Field(description="The ID of a thread note.")
    body: Optional[str] = Field(description="The content of the note or reply. Exactly one of body or resolved must be set.")
    resolved: Optional[bool] = Field(description="Resolve or unresolve the note. Exactly one of body or resolved must be set.")

@action_store.kubiya_action()
def put_modify_merge_request_thread_note(input: ModifyMergeRequestThreadNote):
    return put_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/discussions/{input.discussion_id}/notes/{input.note_id}", args=input.dict(exclude_none=True))


# Delete a merge request thread note
class DeleteMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description="The ID of a thread.")
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    merge_request_iid: int = Field(description="The IID of a merge request.")
    note_id: int = Field(description="The ID of a thread note.")

@action_store.kubiya_action()
def delete_merge_request_thread_note(input: DeleteMergeRequestThreadNote):
    return delete_wrapper(endpoint=f"/projects/{input.id}/merge_requests/{input.merge_request_iid}/discussions/{input.discussion_id}/notes/{input.note_id}")


# List project commit discussion items
class ListProjectCommitDiscussionItems(BaseModel):
    commit_id: str = Field(description="The SHA of a commit.")
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")

@action_store.kubiya_action()
def get_project_commit_discussion_items(input: ListProjectCommitDiscussionItems):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.commit_id}/discussions")


# Get single commit discussion item
class GetSingleCommitDiscussionItem(BaseModel):
    commit_id: str = Field(description="The SHA of a commit.")
    discussion_id: str = Field(description="The ID of a discussion item.")
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")

@action_store.kubiya_action()
def get_single_commit_discussion_item(input: GetSingleCommitDiscussionItem):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.commit_id}/discussions/{input.discussion_id}")

# Position model
class Position(BaseModel):
    base_sha: str = Field(description="SHA of the parent commit.")
    head_sha: str = Field(description="The SHA of this commit. Same as commit_id.")
    start_sha: str = Field(description="SHA of the parent commit.")
    position_type: str = Field(description="Type of the position reference. Allowed values: text or image.")
    hash: Optional[str] = Field(description="Position when creating a diff note.")
    new_path: Optional[str] = Field(description="File path after change.")
    new_line: Optional[int] = Field(description="Line number after change.")
    old_path: Optional[str] = Field(description="File path before change.")
    old_line: Optional[int] = Field(description="Line number before change.")
    height: Optional[int] = Field(description="For image diff notes, image height.")
    width: Optional[int] = Field(description="For image diff notes, image width.")
    x: Optional[int] = Field(description="For image diff notes, X coordinate.")
    y: Optional[int] = Field(description="For image diff notes, Y coordinate.")


# Create new commit thread
class CreateNewCommitThread(BaseModel):
    body: str = Field(description="The content of the thread.")
    commit_id: str = Field(description="The SHA of a commit.")
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    position: Position = Field(description="Position when creating a diff note.")
    created_at: Optional[str] = Field(description="Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.")

@action_store.kubiya_action()
def post_create_new_commit_thread(input: CreateNewCommitThread):
    return post_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.commit_id}/discussions", payload=input.dict())

# Add note to existing commit thread
class AddNoteToCommitThread(BaseModel):
    body: str = Field(description="The content of the note or reply.")
    commit_id: str = Field(description="The SHA of a commit.")
    discussion_id: str = Field(description="The ID of a thread.")
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    note_id: int = Field(description="The ID of a thread note.")
    created_at: Optional[str] = Field(description="Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.")

@action_store.kubiya_action()
def post_add_note_to_commit_thread(input: AddNoteToCommitThread):
    return post_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.commit_id}/discussions/{input.discussion_id}/notes", payload=input.dict())

# Modify an existing commit thread note
class ModifyCommitThreadNote(BaseModel):
    commit_id: str = Field(description="The SHA of a commit.")
    discussion_id: str = Field(description="The ID of a thread.")
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    note_id: int = Field(description="The ID of a thread note.")
    body: Optional[str] = Field(description="The content of a note.")

@action_store.kubiya_action()
def put_modify_commit_thread_note(input: ModifyCommitThreadNote):
    return put_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.commit_id}/discussions/{input.discussion_id}/notes/{input.note_id}", payload=input.dict())


# Delete a commit thread note
class DeleteCommitThreadNote(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project.")
    commit_id: str = Field(description="The SHA of a commit.")
    discussion_id: str = Field(description="The ID of a thread.")
    note_id: int = Field(description="The ID of a thread note.")

@action_store.kubiya_action()
def delete_commit_thread_note(input: DeleteCommitThreadNote):
    return delete_wrapper(endpoint=f"/projects/{input.id}/repository/commits/{input.commit_id}/discussions/{input.discussion_id}/notes/{input.note_id}")
