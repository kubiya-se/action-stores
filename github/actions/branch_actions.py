from .. import action_store as action_store
import logging
from ..models.branches import *
from ..http_wrapper import get_wrapper, post_wrapper, patch_wrapper, delete_wrapper, put_wrapper

FAILED_MSG = "Insufficient data"

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def list_branches(params: ListBranchesParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/branches", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()   
def get_branch(params: GetBranchParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def rename_branch(params: RenameBranchParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/rename", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def sync_fork_branch_with_upstream_repo(params: SyncForkWithUpstreamParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/merge-up", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()   
def merge_branch(params: MergeBranchParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/merges", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def get_branch_protection(params: GetBranchProtectionParams):
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection")
        return resp
    else:
        FAILED_MSG

@action_store.kubiya_action()  
def update_branch_protection(params: UpdateBranchProtectionParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = put_wrapper(f"repos/{params.owner}/{params.repo}/branches/{params.branch}/protection", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def delete_branch_protection(params: DeleteBranchProtectionParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"repos/{params.owner}/{params.repo}/branches/{params.branch}/protection")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def get_admin_branch_protection(params: GetAdminBranchProtectionParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/enforce_admins")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def set_admin_branch_protection(params: SetAdminBranchProtectionParams):
    if params.dict(exclude_none = True):
        resp = post_wrapper(f"repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/enforce_admins")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def delete_admin_branch_protection(params: DeleteAdminBranchProtectionParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/enforce_admins")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def get_pull_request_review_protection(params: GetPrRequestReviewProtectionParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/required_pull_request_reviews")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def update_pull_request_review_protection(params: UpdatePullRequestReviewProtectionParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = patch_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/required_pull_request_reviews", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def delete_pull_request_review_protection(params: DeletePullRequestReviewProtectionParams):
    if params.dict():
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/required_pull_request_reviews")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def get_commit_signature_protection(params: GetCommitSignatureProtectionParams):
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/required_signatures")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def create_commit_signature_protection(params: CreateCommitSignatureProtectionParams):
    if params.dict():
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/required_signatures")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def delete_commit_signature_protection(params: DeleteCommitSignatureProtectionParams):
    if params.dict():
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/required_signatures")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def get_status_checks_protection(params: GetStatusChecksProtectionParams):
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/required_status_checks")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def update_status_checks_protection(params: UpdateStatusChecksProtectionParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        if len(data == 0):
            data = None
        resp = patch_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/required_status_checks", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def remove_status_checks_protection(params: DeleteStatusChecksProtectionParams):
    if params.dict():
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/required_status_checks")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def get_all_status_check_contexts(params: GetAllStatusCheckContextsParams):
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/required_status_checks/contexts")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()  
def add_status_check_contexts(params: AddStatusCheckContextsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/required_status_checks/contexts", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def set_status_check_contexts(params: SetStatusCheckContextsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/required_status_checks/contexts", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def remove_status_check_contexts(params: RemoveStatusCheckContextsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/required_status_checks/contexts", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()  
def get_access_restrictions(params: GetAccessRestrictionsParams):
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/restrictions")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()  
def delete_access_restrictions(params: DeleteAccessRestrictionsParams):
    if params.dict():
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/restrictions")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()  
def get_apps_with_protected_branch_access(params: GetAppsWithProtectedBranchAccessParams):
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/restrictions/apps")
        return resp
    else:
        return FAILED_MSG  

@action_store.kubiya_action()  
def add_app_access_restrictions(params: AddAppAccessRestrictionsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/restrictions/apps", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def set_app_access_restrictions(params: SetAppAccessRestrictionsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/restrictions/apps", data)
        return resp
    else:
        return FAILED_MSG


@action_store.kubiya_action()  
def remove_app_access_restrictions(params: RemoveAppAccessRestrictionsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/restrictions/apps", data)
        return resp
    else:
        return FAILED_MSG
    

@action_store.kubiya_action()  
def get_teams_with_access_to_protected_branch(params: GetTeamsWithAccessToProtectedBranchParams):
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/restrictions/teams")
        return resp
    else:
        return FAILED_MSG 

@action_store.kubiya_action()  
def add_team_access_restrictions(params: AddTeamAccessRestrictionsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/restrictions/teams", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def set_team_access_restrictions(params: SetTeamAccessRestrictionsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/restrictions/teams", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()  
def remove_team_access_restrictions(params: RemoveTeamAccessRestrictionsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/restrictions/teams", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()  
def get_users_with_access_to_protected_branch(params: GetUsersWithAccessToProtectedBranchParams):
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/restrictions/users")
        return resp
    else:
        return FAILED_MSG 

@action_store.kubiya_action()  
def add_user_access_restrictions(params: AddUserAccessRestrictionsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/restrictions/users", data)
        return resp
    else:
        return FAILED_MSG
 
@action_store.kubiya_action()     
def set_user_access_restrictions(params: SetUserAccessRestrictionsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/restrictions/users", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()  
def remove_user_access_restrictions(params: RemoveUserAccessRestrictionsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('branch')
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/branches/{params.branch}/protection/restrictions/users", data)
        return resp
    else:
        return FAILED_MSG