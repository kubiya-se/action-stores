from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime
class ListProjectIssueDiscussionItems(BaseModel):
    id: Union[int, str]
    issue_iid: int
class GetSingleIssueDiscussionItem(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
class CreateNewIssueThread(BaseModel):
    body: str
    id: Union[int, str]
    issue_iid: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingIssueThreadPayload(BaseModel):
    body: str = Field(..., description='The content of the note or reply.')
    discussion_id: int = Field(..., description='The ID of a thread.')
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project.')
    issue_iid: int = Field(..., description='The IID of an issue.')
    note_id: int = Field(..., description='The ID of a thread note.')
    created_at: Optional[datetime] = Field(None, description='Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.')
class ModifyExistingIssueThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    issue_iid: int
    note_id: int
class DeleteIssueThreadNote(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
    note_id: int
class ProjectsIdSnippetsSnippetidDiscussions(BaseModel):
    id: Union[int, str]
    snippet_id: int
class ListProjectSnippetDiscussionItems(BaseModel):
    id: Union[int, str]
    snippet_id: int
class GetSingleSnippetDiscussionItem(BaseModel):
    id: Union[int, str]
    snippet_id: int
    discussion_id: int
class CreateNewSnippetThread(BaseModel):
    body: str
    id: Union[int, str]
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingSnippetThread(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class ModifyExistingSnippetThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class DeleteSnippetThreadNote(BaseModel):
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class GroupsIdEpicsEpicidDiscussions(BaseModel):
    epic_id: int
    id: Union[int, str]
class SingleEpicDiscussionItem(BaseModel):
    discussion_id: int = Field(description='The ID of a discussion item.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group.')
class CreateNewEpicThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group.')
    created_at: Optional[Union[str, datetime]] = Field(None, description='Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.')
class AddNoteToEpicThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[Union[str, datetime]] = Field(None, description='Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.')
class ModifyEpicThreadNote(BaseModel):
    body: str = Field(description='The content of note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class DeleteEpicThreadNote(BaseModel):
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class ListMergeRequestDiscussionItems(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class SingleMergeRequestDiscussionItem(BaseModel):
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class BasicMergeRequestParams(BaseModel):
    body: str = Field(description='The content of the thread.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class DiffNoteParams(BaseModel):
    base_sha: str = Field(description='Base commit SHA in the source branch.')
    head_sha: str = Field(description='SHA referencing HEAD of this merge request.')
    start_sha: str = Field(description='SHA referencing commit in target branch.')
    new_path: str = Field(description='File path after change.')
    old_path: str = Field(description='File path before change.')
    position_type: str = Field(description='Type of the position reference. Allowed values: text or image.')
class TextDiffNoteParams(BaseModel):
    new_line: Optional[int] = Field(description='For text diff notes, the line number after change.')
    old_line: Optional[int] = Field(description='For text diff notes, the line number before change.')
class ImageDiffNoteParams(BaseModel):
    width: Optional[int] = Field(description='For image diff notes, width of the image.')
    height: Optional[int] = Field(description='For image diff notes, height of the image.')
    x: Optional[float] = Field(description='For image diff notes, X coordinate.')
    y: Optional[float] = Field(description='For image diff notes, Y coordinate.')
class MultilineCommentsParams(BaseModel):
    line_range: dict = Field(description='Line range for a multi-line diff note.')
class CreateNewMergeRequestThread(BasicMergeRequestParams):
    position: DiffNoteParams = Field(description='Position when creating a diff note.')
    text_position: Optional[TextDiffNoteParams] = Field(description='Position parameters for text diff notes.')
    image_position: Optional[ImageDiffNoteParams] = Field(description='Position parameters for image diff notes.')
    multiline_comments: Optional[MultilineCommentsParams] = Field(description='Parameters for multiline comments.')
    commit_id: Optional[str] = Field(description='SHA referencing commit to start this thread on.')
    created_at: Optional[str] = Field(description='Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.')
class ResolveMergeRequestThread(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    discussion_id: str = Field(description='The ID of a thread.')
    resolved: bool = Field(description='Resolve or unresolve the discussion.')
class AddNoteToMergeRequestThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    discussion_id: str = Field(description='The ID of a thread.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description='Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.')
class ModifyMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description='The content of the note or reply. Exactly one of body or resolved must be set.')
    resolved: Optional[bool] = Field(description='Resolve or unresolve the note. Exactly one of body or resolved must be set.')
class DeleteMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
class ListProjectCommitDiscussionItems(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
class GetSingleCommitDiscussionItem(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
class Position(BaseModel):
    base_sha: str = Field(description='SHA of the parent commit.')
    head_sha: str = Field(description='The SHA of this commit. Same as commit_id.')
    start_sha: str = Field(description='SHA of the parent commit.')
    position_type: str = Field(description='Type of the position reference. Allowed values: text or image.')
    hash: Optional[str] = Field(description='Position when creating a diff note.')
    new_path: Optional[str] = Field(description='File path after change.')
    new_line: Optional[int] = Field(description='Line number after change.')
    old_path: Optional[str] = Field(description='File path before change.')
    old_line: Optional[int] = Field(description='Line number before change.')
    height: Optional[int] = Field(description='For image diff notes, image height.')
    width: Optional[int] = Field(description='For image diff notes, image width.')
    x: Optional[int] = Field(description='For image diff notes, X coordinate.')
    y: Optional[int] = Field(description='For image diff notes, Y coordinate.')
class CreateNewCommitThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    position: Position = Field(description='Position when creating a diff note.')
    created_at: Optional[str] = Field(description='Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.')
class AddNoteToCommitThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description='Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.')
class ModifyCommitThreadNote(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description='The content of a note.')
class DeleteCommitThreadNote(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    note_id: int = Field(description='The ID of a thread note.')