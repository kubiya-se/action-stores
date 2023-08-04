from pydantic import BaseModel, Field
from .common import SimpleResponse
from typing import List, Optional, Any

class GetEventsResponse(BaseModel):
    resp: Optional[List[int]]

class CreateIssueParams(BaseModel):
    fields: Optional[object]
    historyMetadata: Optional[object]
    transition: Optional[object]
    update: Optional[object]
    additional: Optional[Any]

class CreateIssueResponse(BaseModel):
    id: Optional[str]
    key: Optional[str]
    self: Optional[str]
    transition: Optional[object]
    watchers: Optional[object]

class BulkCreateIssueParams(BaseModel):
    issueUpdates: Optional[List]
    additional: Optional[Any]

class BulkCreateIssueResponse(BaseModel):
    errors: Optional[List[object]]
    issues: Optional[List[object]]

class GetCreateIssueMetadataParams(BaseModel):
    projectIds: Optional[List[str]]
    projectKeys: Optional[List[str]]
    issuetypeIds: Optional[List[str]]
    issuetypeNames: Optional[List[str]]

class GetCreateIssueMetadataResponse(BaseModel):
    expand: Optional[str]
    projects: Optional[List[object]]

class GetIssueParams(BaseModel):
    issueIdOrKey: str
    fields: Optional[List[str]]
    fieldsByKeys: Optional[bool]
    expand: Optional[str]
    properties: Optional[List[str]]
    updateHistory: Optional[bool]

class GetIssueResponse(BaseModel):
    changelog: Optional[object]
    editmeta: Optional[object]
    expand: Optional[str]
    fields: Optional[object]
    fieldsToInclude: Optional[object]
    id: Optional[str]
    key: Optional[str]
    names: Optional[object]
    operations: Optional[object]
    properties: Optional[object]
    renderedFields: Optional[object]
    schema1: Optional[object] = Field(alias = 'schema')
    self: Optional[str]
    transitions: Optional[List[object]]
    versionedRepresentations: Optional[object]





class EditIssueParams(BaseModel):
    issueIdOrKey: str
    notifyUsers: Optional[bool]
    overrideScreenSecurity: Optional[bool]
    overrideEditableFlag: Optional[bool]
    fields: Optional[object]
    historyMetadata: Optional[object]
    transition: Optional[object]
    update: Optional[object]
    additional: Optional[Any]

class EditIssueResponse(BaseModel):
    resp: Optional[Any]

class DeleteIssueParams(BaseModel):
    issueIdOrKey: str
    deleteSubtasks: Optional[str]


class AssignIssueParams(BaseModel):
    issueIdOrKey: str
    accountId: Optional[str]
    key: Optional[str]
    name: Optional[str]

class AssignIssueResponse(BaseModel):
    resp: Optional[Any]


class GetChangelogsParams(BaseModel):
    issueIdOrKey: str
    startAt: Optional[int]
    maxResults: Optional[int]

class GetChangelogsResponse(BaseModel):
    isLast: Optional[bool]
    maxResults: Optional[int]
    nextPage: Optional[str]
    self: Optional[str]
    startAt: Optional[str]
    total: Optional[int]
    values: Optional[List[int]]


class GetChangelogByIdParams(BaseModel):
    issueIdOrKey: str
    changelogIds: List[int]

class GetChangelogByIdResponse(BaseModel):
    histories: Optional[List[object]]
    maxResults: Optional[int]
    startAt: Optional[int]
    total: Optional[int]

class GetEditIssueMetadataParams(BaseModel):
    issueIdOrKey: str
    overrideScreenSecurity: Optional[bool]
    overrideEditableFlag: Optional[bool]

class GetEditIssueMetadataResponse(BaseModel):
    fields: Optional[object]



class SendNotificationForIssueParams(BaseModel):
    issueIdOrKey: str
    htmlBody: Optional[str]
    restrict: Optional[object]
    subject: Optional[str]
    textBody: Optional[str]
    to: Optional[object]
    additional: Optional[Any]

class SendNotificationForIssueResponse(BaseModel):
    resp: Optional[Any]

class GetTransitionsParams(BaseModel):
    issueIdOrKey: str
    expand: Optional[str]
    transitionId: Optional[str]
    skipRemoteOnlyCondition: Optional[bool]
    includeUnavailableTransitions: Optional[bool]
    sortByOpsBarAndStatus: Optional[bool]

class GetTransitionResponse(BaseModel):
    expand: Optional[str]
    transitions: Optional[List]

class TransitionIssueParams(BaseModel):
    issueIdOrKey: str
    fields: Optional[object]
    historyMetadata: Optional[object]
    properties: Optional[List]
    transition: Optional[object]
    update: Optional[object]
    additional: Optional[Any]


class TransitionIssueResponse(BaseModel):
    resp: Optional[Any]


class GetAttachmentContentParams(BaseModel):
    id: str
    redirect: Optional[bool]

class GetAttachmentContentResponse(BaseModel):
    resp: object

class GetAttachmentThumbnailParams(BaseModel):
    id: str
    redirect: Optional[bool]
    fallbackToDefault: Optional[bool]
    width: Optional[int]
    height: Optional[int]


class GetAttachmentThumbnailResponse(BaseModel):
    resp: Optional[object]

class GetJiraAttachmentSettingsResponse(BaseModel):
    enabled: Optional[bool]
    uploadLimit: Optional[int]

class GetAttachmentMetadataParams(BaseModel):
    id: str

class GetAttachmentMetadataResponse(BaseModel):
    author: Optional[object]
    content: Optional[str]
    created: Optional[str]
    filename: Optional[str]
    id: Optional[int]
    mimeType: Optional[str]
    properties: Optional[object]
    self: Optional[str]
    size: Optional[int]
    thumbnail: Optional[str]



class DeleteAttachmentParams(BaseModel):
    id: str

class GetAllMetadataForExpandedAttachmentParams(BaseModel):
    id: str

class GetAllMetadataForAnExpandedAttachmentResponse(BaseModel):
    entries: Optional[List]
    id: Optional[int]
    mediaType: Optional[str]
    name: Optional[str]
    totalEntryCount: Optional[int]

class GetContentsMetadataForExpandedAttachmentParams(BaseModel):
    id: str

class GetContentsMetadataForExpandedAttachmentResponse(BaseModel):
    entries: Optional[List]
    totalEntryCount: Optional[int]

class AddAttachmentParams(BaseModel):
    issueIdOrKey: str

class AddAttachmentResponse(BaseModel):
    resp: Optional[List]

class GetCommentsByIdsParams(BaseModel):
    expand: Optional[str]
    ids: List[int]

class GetCommentsByIdsResponse(BaseModel):
    isLast: Optional[bool]
    maxResults: Optional[int]
    nextPage: Optional[str]
    self: Optional[str]
    startAt: Optional[int]
    total: Optional[int]
    values: Optional[List]

class GetCommentsParams(BaseModel):
    issueIdOrKey: str
    startAt: Optional[int]
    maxResults: Optional[int]
    orderBy: Optional[str]
    expand: Optional[str]

class GetCommentsResponse(BaseModel):
    comments: Optional[List]
    maxResults: Optional[int]
    startAt: Optional[int]
    total: Optional[int]
    properties: Optional[Any]

class AddCommentParams(BaseModel):
    issueIdOrKey: str
    startAt: Optional[int]
    expand: Optional[str]

class AddCommentResponse(BaseModel):
    author: Optional[object]
    body: Optional[Any]
    created: Optional[str]
    id: Optional[str]
    jsdAuthorCanSeeRequest: Optional[bool]
    jsdPublic: Optional[bool]
    properties: Optional[List]
    renderedBody: Optional[str]
    self: Optional[str]
    updateAuthor: Optional[object]
    updated: Optional[str]
    visibility: Optional[object]
    properties: Optional[Any]

