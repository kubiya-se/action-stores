from .. import action_store as action_store
import logging
from ..models.issues import *
from ..http_wrapper import get_wrapper, post_wrapper, patch_wrapper, delete_wrapper, put_wrapper

FAILED_MSG = "Insufficient data"

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def list_issues_assigned_to_authenticated_user(params: ListIssuesParams):
    resp = get_wrapper("/issues", params.dict(exclude_none = True))
    return resp

@action_store.kubiya_action()
def list_organization_issues_assigned_to_authenticated_user(params: ListOrganizationIssuesParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("org")
        resp = get_wrapper(f"/orgs/{params.org}/issues", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def list_repository_issues(params: ListRepositoryIssuesParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/issues", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def create_issue(params: CreateIssueParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/issues", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def get_issue(params: GetIssueParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()
def update_issue(params: UpdateIssueParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("issue_number")
        resp = patch_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def update_issue(params: UpdateIssueParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("issue_number")
        resp = patch_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def lock_issue(params: LockIsuseParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("issue_number")
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/lock", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def unlock_issue(params: UnlockIssueParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("issue_number")
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/lock", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def link_user_account_issues_assigned_to_authenticated_user(params: ListAccountIssuesAssignedToUserParams):
    resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/lock", data)
    return resp
    

@action_store.kubiya_action()
def list_assignees(params: ListAssigneesParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/assignees", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def check_if_a_user_can_be_assigned(params: CheckUserAssignabilityParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/assignees/{params.assignee}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def add_assignees_to_an_issue(params: AddAssigneesToIssueParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("issue_number")
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/assignees", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def remove_assignees_from_an_issue(params: RemoveAssigneesFromIssueParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("issue_number")
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/assignees", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def check_if_a_user_can_be_assigned_to_an_issue(params: CheckIfUserCanBeAssignedToIssueParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/assignees/{params.assignee}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def list_issue_comments_for_a_repository(params: ListIssueCommentsForARepositoryParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/issues/comments", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def get_an_issue_comment(params: GetIssueCommentParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/issues/comments/{params.comment_id}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()      
def update_an_issue_comment(params: UpdateIssueCommentParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("comment_id")
        resp = patch_wrapper(f"/repos/{params.owner}/{params.repo}/issues/comments/{params.comment_id}", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()      
def delete_an_issue_comment(params: DeleteIssueCommentParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/issues/comments/{params.comment_id}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()      
def list_issue_comments(params: ListIssueCommentsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("issue_number")
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/comments", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()      
def create_issue_comment(params: CreateIssueCommentParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("issue_number")
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/comments", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def list_issue_events_for_a_repository(params: ListIssueEventsForRepoParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/issues/events", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action() 
def get_issue_event(params: GetIssueEventParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/issues/events/{params.event_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def list_issue_events(params: ListIssueEventsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("issue_number")
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/events", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action() 
def list_labels_for_an_issue(params: ListIssueLabelsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("issue_number")
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/labels", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def add_labels_to_an_issue(params: AddIssueLabelsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("issue_number")
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/labels", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def set_labels_for_an_issue(params: SetIssueLabelsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("issue_number")
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/labels", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def remove_all_labels_from_an_issue(params: RemoveIssueLabelsParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/labels")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def remove_label_from_an_issue(params: RemoveIssueLabelParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/labels/{params.name}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def list_labels_for_a_repo(params: ListRepoIssueLabelsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/labels", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def create_label(params: CreateLabelParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/labels", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action() 
def get_label(params: GetLabelParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/labels/{params.name}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def update_label(params: UpdateLabelParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = patch_wrapper(f"/repos/{params.owner}/{params.repo}/labels/{params.name}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def delete_label(params: DeleteLabelParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/labels/{params.name}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def list_labels_for_issues_in_milestone(params: ListIssueLabelsInMilestoneParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("milestone_number")
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/milestones/{params.milestone_number}/labels", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def list_milestones(params: ListMilestonesParams):
    data = params.dict(exclude_none = True)
    if data: 
        data.pop("owner")
        data.pop("repo")
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/milestones", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def create_a_milestone(params: CreateMilestoneParams):
    data = params.dict(exclude_none = True)
    if data: 
        data.pop("owner")
        data.pop("repo")
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/milestones", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def get_a_milestone(params: GetMilestonesParams):
    data = params.dict(exclude_none = True)
    if data: 
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/milestones/{params.milestone_number}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def update_a_milestone(params: UpdateMilestoneParams):
    data = params.dict(exclude_none = True)
    if data: 
        data.pop("owner")
        data.pop("repo")
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/milestones", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_a_milestone(params: GetMilestonesParams):
    data = params.dict(exclude_none = True)
    if data: 
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/milestones/{params.milestone_number}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def list_timeline_events_for_an_issue(params: ListTimelineEventsForIssueParams):
    data = params.dict(exclude_none = True)
    if data: 
        data.pop("owner")
        data.pop("repo")
        data.pop("issue_number")
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/issues/{params.issue_number}/timeline")
        return resp
    else:
        return FAILED_MSG
    
    


    

    

    

    




    



    
