from ..jira_wrapper import get_jira_instance
from atlassian import Jira
from ..models.issue import *
from ..models.jql import RunJQLParams, RunJQLResponse
from ..models.common import SimpleResponse
from .. import action_store as action_store
from ..http_wrapper import get_wrapper, patch_wrapper, post_wrapper, put_wrapper, delete_wrapper

FAILED_MSG = "Insufficient data"


def get_jira_url(issue_key: str, jira_instance: Jira) -> str:
    """
    Returns the URL of an issue
    """
    return jira_instance.url + '/browse/' + issue_key

@action_store.kubiya_action()
def get_events() -> GetEventsResponse:
    response = get_wrapper("/rest/api/3/events")
    events = []
    for i in response['Events']:
        events.extend(i)
    return GetEventsResponse(resp = events)

@action_store.kubiya_action()
def create_issue(params: CreateIssueParams) -> CreateIssueResponse:
    data = params.dict(exclude_none = True)
    if data:
        resp = post_wrapper("/rest/api/3/events", data)
        resp_dict = {'id': resp['id'], 
                     'key': resp['key'],
                     'self': resp['self'],
                     'transition': resp['transition'],
                     'watchers': resp['watchers']
                     }
        return CreateIssueResponse(resp_dict)
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def bulk_create_issue(params: BulkCreateIssueParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = post_wrapper("/rest/api/3/issue/bulk", data)
        resp_dict = {'issueUpdates': resp['issueUpdates'],
                     'additional': resp['Additional Properties']
                    }
        return BulkCreateIssueResponse(resp_dict)
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_create_issue_metadata(params: GetCreateIssueMetadataParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = get_wrapper("/rest/api/3/issue/createmeta", data)
        resp_dict = {'expand': resp['expand'],
                    'projects': resp['projects'] 
                    }
        return GetCreateIssueMetadataResponse(resp_dict)
    else:
        return FAILED_MSG

@action_store.kubiya_action()   
def get_issue(params: GetIssueParams) -> GetIssueResponse:
    data = params.dict(exclude_none = True)
    if data: 
        data.pop("issueIdOrKey")
        resp = get_wrapper(f"/rest/api/3/issue/{params.issueIdOrKey}", data)
        resp_dict = {'changelog': resp['changelog'],
                     'editmeta': resp['editmeta'],
                     'expand': resp['expand'],
                     'fields': resp['fields'],
                     'fieldsToInclude': resp['fieldsToInclude'],
                     'id': resp['id'],
                     'key': resp['key'],
                     'names': resp['names'],
                     'operations': resp['operations'],
                     'properties': resp['properties'],
                     'renderedFields': resp['renderedFields'],
                     'schema': resp['schema'],
                     'self': resp['self'],
                     'transitions': resp['transitions'],
                     'versionedRepresentations': resp['versionedRepresentations']
                    }
        return GetIssueResponse(resp_dict)
    else:
        return FAILED_MSG

@action_store.kubiya_action()   
def edit_issue(params: EditIssueParams) -> EditIssueResponse:
    data = params.dict(exclude_none = True)
    if data: 
        data.pop("issueIdOrKey")
        resp = put_wrapper(f"/rest/api/3/issue/{params.issueIdOrKey}", data)
        resp_dict = {resp: resp}
        return EditIssueResponse(resp_dict)
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def delete_issue(params: DeleteIssueParams):
    data = params.dict(exclude_none = True)
    if data: 
        data.pop("issueIdOrKey")
        resp = delete_wrapper(f"/rest/api/3/issue/{params.issueIdOrKey}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()
def assign_issue(params: AssignIssueParams) -> AssignIssueResponse:
    data = params.dict(exclude_none = True)
    if data:
        data.pop("issueIdOrKey")
        resp = put_wrapper(f"/rest/api/3/issue/{params.issueIdOrKey}/assignee", data)
        resp_dict = {'resp': resp}
        return AssignIssueResponse(resp_dict)
    else:
        return FAILED_MSG

@action_store.kubiya_action()   
def get_changelogs(params: GetChangelogsParams) -> GetChangelogsResponse:
    data = params.dict(exclude_none = True)
    if data:
        data.pop("issueIdOrKey")
        resp = get_wrapper(f"/rest/api/3/issue/{params.issueIdOrKey}/changelog", data)
        resp_dict = {'isLast': resp['isLast'],
                     'maxResults': resp['maxResults'],
                     'nextPage': resp['nextPage'],
                     'self': resp['self'],
                     'startAt': resp['startAt'],
                     'total': resp['total'],
                     'values': resp['values']}
        return GetChangelogsResponse(resp_dict)
    else:
        return FAILED_MSG

@action_store.kubiya_action()   
def get_changelogs_by_ids(params: GetChangelogByIdParams) -> GetChangelogByIdResponse:
    data = params.dict(exclude_none = True)
    if data:
        data.pop("issueIdOrKey")
        resp = post_wrapper(f"/rest/api/3/issue/{params.issueIdOrKey}/changelog/list", data)
        resp_dict = {'histories': resp['histories'],
                     'maxResults': resp['maxResults'],
                     'startAt': resp['startAt'],
                     'total': resp['total']}
        return GetChangelogByIdResponse(resp_dict)
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def get_edit_issue_metadata(params: GetEditIssueMetadataParams) -> GetEditIssueMetadataResponse:
    data = params.dict(exclude_none = True)
    if data:
        data.pop("issueIdOrKey")
        resp = get_wrapper(f"/rest/api/3/issue/{params.issueIdOrKey}/editmeta", data)
        resp_dict = {'fields': resp['fields']}
        return GetEditIssueMetadataResponse(resp_dict)
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def send_notification_for_issue(params: SendNotificationForIssueParams) -> SendNotificationForIssueResponse:
    data = params.dict(exclude_none = True)
    if data:
        data.pop("issueIdOrKey")
        resp = post_wrapper(f"/rest/api/3/issue/{params.issueIdOrKey}/notify", data)
        resp_dict = {'resp': resp}
        return SendNotificationForIssueResponse(resp_dict)
    else:
        return FAILED_MSG

@action_store.kubiya_action()
def get_transitions(params: GetTransitionsParams) -> GetTransitionResponse:
    data = params.dict(exclude_none = True)
    if data:
        data.pop("issueIdOrKey")
        resp = get_wrapper(f"/rest/api/3/issue/{params.issueIdOrKey}/transitions", data)
        resp_dict = {'expand': resp['expand'],
                     'transitions': resp['transitions']}
        return GetTransitionsParams(resp_dict)
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def transition_issue(params: TransitionIssueParams) -> TransitionIssueResponse:
    data = params.dict(exclude_none = True)
    if data:
        data.pop("issueIdOrKey")
        resp = post_wrapper(f"/rest/api/3/issue/{params.issueIdOrKey}/transitions", data)
        resp_dict = {'resp': resp}
        return TransitionIssueResponse(resp_dict)
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_attachment_content(params: GetAttachmentContentParams) -> GetAttachmentContentResponse:
    data = params.dict(exclude_none = True)
    if data:
        data.pop("id")
        resp = get_wrapper(f"/rest/api/3/attachment/content/{params.id}", data)
        resp_dict = {'resp': resp}
        return GetAttachmentContentResponse(resp_dict)
    else:
        return FAILED_MSG

@action_store.kubiya_action()
def get_jira_attachment_settigns() -> GetJiraAttachmentSettingsResponse:
    resp = get_wrapper(f"/rest/api/3/attachment/meta")
    resp_dict = {'enabled': resp['enabled'],
                 'uploadLimit': resp['uploadLimit']}
    return GetJiraAttachmentSettingsResponse(resp_dict)

@action_store.kubiya_action()
def get_attachment_thumbnail(params: GetAttachmentThumbnailParams) -> GetAttachmentThumbnailResponse:
    data = params.dict(exclude_none = True)
    if data:
        data.pop("id")
        resp = get_wrapper(f"/rest/api/3/attachment/thumbnail/{params.id}", data)
        resp_dict = {'resp': resp}
        return GetAttachmentThumbnailResponse(resp_dict)
    else:
        return FAILED_MSG

@action_store.kubiya_action()   
def get_attachment_metadata(params: GetAttachmentMetadataParams) -> GetAttachmentMetadataResponse:
    data = params.dict(exclude_none = True)
    if data:
        data.pop("id")
        resp = get_wrapper(f"/rest/api/3/attachment/{params.id}")
        resp_dict = {'author': resp['author'],
                     'content': resp['content'],
                     'created': resp['created'],
                     'filename': resp['filename'],
                     'id': resp['id'],
                     'mimeType': resp['mimeType'],
                     'properties': resp['properties'],
                     'self': resp['self'],
                     'size': resp['size'],
                     'thumbnail': resp['thumbnail']}
        return GetAttachmentMetadataResponse(resp_dict)
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def delete_attachment(params: DeleteAttachmentParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("id")
        resp = delete_wrapper(f"/rest/api/3/attachment/{params.id}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()   
def get_all_metadata_for_expanded_attachment(params: GetAllMetadataForExpandedAttachmentParams) -> GetAllMetadataForAnExpandedAttachmentResponse:
    data = params.dict(exclude_none = True)
    if data:
        data.pop("id")
        resp = get_wrapper(f"/rest/api/3/attachment/{params.id}/expand/human")
        resp_dict = {'entries': resp['entries'],
                     'id': resp['id'],
                     'mediaType': resp['mediaType'],
                     'name': resp['name'],
                     'totalEntryCount': resp['totalEntryCount']}
        return GetAllMetadataForAnExpandedAttachmentResponse(resp_dict)
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_contents_metadata_for_expanded_attachment(params: GetContentsMetadataForExpandedAttachmentParams) -> GetContentsMetadataForExpandedAttachmentResponse:
    data = params.dict(exclude_none = True)
    if data:
        data.pop("id")
        resp = get_wrapper(f"/rest/api/3/attachment/content/{params.id}/expand/raw", data)
        resp_dict = {'entries': resp['entries'],
                     'totalEntryCount': resp['totalEntryCount']}
        return GetContentsMetadataForExpandedAttachmentResponse
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def add_attachment(params: AddAttachmentParams) -> AddAttachmentResponse:
    data = params.dict(exclude_none = True)
    if data:
        resp = post_wrapper(f"/rest/api/3/issue/{params.issueIdOrKey}/attachments")
        resp_dict = {'author': resp['author'],
                     'content': resp['content'],
                     'created': resp['created'],
                     'filename': resp['filename'],
                     'id': resp['id'],
                     'mimeType': resp['mimeType'],
                     'self': resp['self'],
                     'size': resp['size'],
                     'thumbnail': resp['thumbnail'],
                     'properties': resp['properties']}
        return AddAttachmentResponse(resp_dict)
    else:
        return FAILED_MSG


