from .. import action_store as action_store
import logging
from ..models.repository import *
from ..http_wrapper import get_wrapper, post_wrapper, patch_wrapper, delete_wrapper, put_wrapper

FAILED_MSG = "Insufficient data"

logger = logging.getLogger(__name__)

@action_store.kubiya_action()
def list_all_autolinks(params: ListAllAutolinksParams) -> str:
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/autolinks")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def create_autolink(params: CreateAutolinkParams) -> str:
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/autolinks", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_autolink_ref_for_repo(params: GetAutoRefForRepoParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/autolinks/{params.autolink_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()
def delete_autolink_ref_for_repo(params: DeleteAutoRefForRepoParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/autolinks/{params.autolink_id}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def get_repo_content(params: GetRepoContentParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/contents/{params.path}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def create_update_file_contents(params: CreateUpdateFileContentsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("path")
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/contents/{params.path}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()  
def delete_file(params: DeleteFileParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("path")
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/contents/{params.path}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_repo_readme(params: GetRepoReadmeParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/readme")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()
def get_repo_readme_for_directory(params: GetRepoReadmeForDirectoryParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/readme/{params.dir}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def download_repo_archive_tar(params: DownloadRepoTarParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/tarball/{params.ref}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def download_repo_archive_zip(params: DownloadRepoZipParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/zipball/{params.ref}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def list_forks(params: ListForksParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/forks")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def create_fork(params: CreateForkParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        if len(data) == 0:
            data = None
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/forks", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def enable_git_lfs(params: EnableGitLfsParams):
    if params.dict(exclude_none = True):
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/lfs")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def disable_git_lfs(params: DisableGitLfsParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/lfs")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def list_tag_protection_states_for_repo(params:ListRepoTagProtectionStatesParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/tags/protection")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def create_tag_protection_states_for_repo(params:CreateRepoTagProtectionStatesParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/tags/protection", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def list_tag_protection_states_for_repo(params:DeleteRepoTagProtectionStatesParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/tags/protection/{params.tag_protection_id}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def get_rules_for_branch(params: GetRulesForBranchParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/rules/branches/{params.branch}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_repo_rulesets(params: GetRepoRulesetsParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/rulesets")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def create_repo_ruleset(params: CreateRepoRulesetParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/rulesets", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_repo_ruleset(params: GetRepoRulesetParams):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/rulesets/{params.ruleset_id}")
        return resp
    return FAILED_MSG

@action_store.kubiya_action()
def update_repo_ruleset(params: UpdateRepoRulesetParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop("owner")
        data.pop("repo")
        data.pop("ruleset_id")
        if len(data) == 0:
            data = None
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/rulesets", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_repo_ruleset(params: GetRepoRulesetParams):
    if params.dict(exclude_none = True):
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/rulesets/{params.ruleset_id}")
        return resp
    return FAILED_MSG

@action_store.kubiya_action()  
def create_repo(params:CreateRepoParams) -> str:
    logging.info(params.dict())
    logging.info(params.dict(exclude_none=True))
    if params.dict():
        post_wrapper("/user/repos", params.dict(exclude_none=True))
        logging.info("asdf")
        return f"Creating repo {params.name} with args {params.dict()}"
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()    
def create_repo_in_org(params:CreateRepoInOrgParams) -> str:
    data = params.dict(exclude_none=True)
    if data:
        org_name = data.pop("org")
        post_wrapper(f"/orgs/{params.org}/repos", data)
        return f"Creating repo {params.name} in org {org_name} with args {data}"
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def get_repo(params:GetRepoParams) -> str: #tested, works
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def update_repo(params:UpdateRepoParams) -> str:
    data = params.dict(exclude_none=True)
    if data:
        data.pop("owner")
        data.pop("repo")
        resp = patch_wrapper(f"/repos/{params.owner}/{params.repo}", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def delete_repo(params:DeleteRepoParams) -> str:
    if params.dict():
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def enable_automated_security_fixes(params:EnableAutoSecFixesParams) -> str:
    if params.dict():
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/automated-security-fixes")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def disable_automated_security_fixes(params:DisableAutoSecFixesParams) -> str:
    if params.dict():
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/automated-security-fixes")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def list_codeowners_error(params:ListCodeownersErrorsParams) -> str:
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/codeowners/errors")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def list_repo_contributors(params:ListRepoContributorsParams) -> str:
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/contributors")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def create_repo_dispatch_event(params:CreateRepoDispatchEventParams) -> str:
    data = params.dict(exclude_none=True)
    if data:
        data.pop("owner")
        data.pop("repo")
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/dispatches", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()    
def list_repo_languages(params: ListRepoLanguagesParams) -> str:
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/languages")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def list_repo_tags(params: ListRepoTagsParams) -> str:
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/tags")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def list_repo_teams(params: ListRepoTeamsParams) -> str:
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/teams")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def list_repo_topics(params: ListRepoTopicsParams) -> str:
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/topics")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def replace_repo_topics(params: ReplaceRepoTopicsParams) -> str:
    if params.dict():
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/topics", params.names)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def transfer_repo(params: TransferRepoParams) -> str:
    data = params.dict(exclude_none=True)
    if data:
        data.drop("owner")
        data.drop("repo")
        resp = post_wrapper(f"repos/{params.owner}/{params.repo}/transfer", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def check_vulnerability_alerts_enabled(params: CheckVulnerabilityAlertsParams):
    if params.dict():
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/vulnerability-alerts")
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def enable_vulnerability_alerts(params: EnableVulnerabilityAlertsParams):
    if params.dict():
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/vulnerability-alerts")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()
def disable_vulnerability_alerts(params: DisableVulnerabilityAlertsParams):
    if params.dict():
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/vulnerability-alerts")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()
def create_repo_using_template(params: CreateRepoUsingTemplateParams):
    data = params.dict(exclude_none=True)
    if data:
        data.pop("template_owner")
        data.pop("template_repo")
        resp = post_wrapper(f"/repos/{params.template_owner}/{params.template_repo}/generate", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()
def list_public_repos():
    resp = get_wrapper("/repositories")
    return resp

@action_store.kubiya_action()
def list_repos_for_authenticated_user():
    resp = get_wrapper("/user/repos")
    return resp

def list_repos_via_username(params: ListUserRepos):
    if params.dict(exclude_none = True):
        resp = get_wrapper(f"/users/{params.username}/repos")
        return resp
    else:
        return FAILED_MSG