from pydantic import BaseModel
from typing import Optional, List

class ListAllAutolinksParams(BaseModel):
    owner: str
    repo: str

class CreateAutolinkParams(BaseModel):
    owner: str
    repo: str
    key_prefix: str
    url_template: str
    is_alphanumberic: Optional[bool]

class GetAutoRefForRepoParams(BaseModel):
    owner: str
    repo: str
    autolink_id: str

class DeleteAutoRefForRepoParams(BaseModel):
    owner: str
    repo: str
    autolink_id: str

class GetRepoContentParams(BaseModel):
    owner: str
    repo: str
    path: str

class CreateUpdateFileContentsParams(BaseModel):
    owner: str
    repo: str
    path: str
    message: str
    content: str
    sha: Optional[str]
    branch: Optional[str]
    committer: Optional[object]   #come back and validate that it's the right object

class DeleteFileParams(BaseModel):
    owner: str
    repo: str
    path: str
    message: str
    sha: str
    branch: Optional[str]
    committer: Optional[object]

class GetRepoReadmeParams(BaseModel):
    owner: str
    repo: str

class GetRepoReadmeForDirectoryParams(BaseModel):
    owner: str
    repo: str
    dir: str

class DownloadRepoTarParams(BaseModel):
    owner: str
    repo: str
    ref: str

class DownloadRepoZipParams(BaseModel):
    owner: str
    repo: str
    ref: str

class ListForksParams(BaseModel):
    owner: str
    repo: str

class CreateForkParams(BaseModel):
    owner: str
    repo: str
    organization: Optional[str] = None
    name: Optional[str] = None
    default_branch_only: Optional[bool] = None

class EnableGitLfsParams(BaseModel):
    owner: str
    repo: str

class DisableGitLfsParams(BaseModel):
    owner: str
    repo: str

class ListRepoTagProtectionStatesParams(BaseModel):
    owner: str
    repo: str

class CreateRepoTagProtectionStatesParams(BaseModel):
    owner: str
    repo: str
    pattern: str

class DeleteRepoTagProtectionStatesParams(BaseModel):
    owner: str
    repo: str
    tag_protection_id: int

class GetRulesForBranchParams(BaseModel):
    owner: str
    repo: str
    branch: str

class GetRepoRulesetsParams(BaseModel):
    owner: str
    repo: str

class CreateRepoRulesetParams(BaseModel):
    owner: str
    repo: str
    name: str
    target: Optional[str]
    enforcement: str
    bypass_actors: Optional[List]
    conditions: Optional[object]
    rules: Optional[List]

class GetRepoRulesetParams(BaseModel):
    owner: str
    repo: str
    ruleset_id: int

class UpdateRepoRulesetParams(BaseModel):
    owner: Optional[str]
    repo: Optional[str]
    ruleset_id: Optional[int]
    name: Optional[str]
    target: Optional[str]
    enforcement: str
    bypass_actors: Optional[List]
    conditions: Optional[object]
    rules: Optional[List]

class DeleteRepoRulesetParams(BaseModel):
    owner: str
    repo: str
    ruleset_id: int

class CreateRepoParams(BaseModel):
    name: str
    # description: Optional[str] = None
    # homepage: Optional[str] = None
    # private: Optional[bool] = False
    # has_issues: Optional[bool] = False
    # has_projects: Optional[bool] = False
    # has_wiki: Optional[bool] = False
    # has_discussions: Optional[bool] = False
    # team_id: Optional[int] = 0
    # auto_init: Optional[bool] = False
    # gitignore_template: Optional[str] = None
    # license_template: Optional[str] = None
    # allow_squash_merge: Optional[bool] = False
    # allow_merge_commit: Optional[bool] = False
    # allow_rebase_merge: Optional[bool] = False
    # allow_auto_merge: Optional[bool] = False
    # delete_branch_on_merge: Optional[bool] = False
    # squash_merge_commit_title: Optional[str] = None
    # squash_merge_commit_message: Optional[str] = None
    # merge_commit_title: Optional[str] = None
    # merge_commit_message: Optional[str] = None
    # has_downloads: Optional[bool] = False
    # is_template: Optional[bool] = False

class CreateRepoInOrgParams(BaseModel):
    org: str
    name: str
    # description: Optional[str]
    # homepage: Optional[str]
    # private: Optional[bool]
    # has_issues: Optional[bool]
    # has_projects: Optional[bool]
    # has_wiki: Optional[bool]

class GetRepoParams(BaseModel):
    owner: str
    repo: str

class UpdateRepoParams(BaseModel):
    owner: str
    repo: str
    name: Optional[str] = None
    # description: Optional[str] = None
    # homepage: Optional[str] = None
    # private: Optional[bool] = None
    # visibility: Optional[str] = None
    # has_issues: Optional[bool] = None
    # has_projects: Optional[bool] = None
    # has_wiki: Optional[bool] = None
    # is_template: Optional[bool] = None
    # default_branch: Optional[str] = None
    # allow_squash_merge: Optional[bool] = None
    # allow_merge_commit: Optional[bool] = None
    # allow_rebase_merge: Optional[bool] = None
    # allow_auto_merge: Optional[bool] = None
    # delete_branch_on_merge: Optional[bool] = None
    # allow_update_branch: Optional[bool] = None
    # use_squash_pr_title_as_default: Optional[bool] = None
    # squash_merge_commit_title: Optional[str] = None
    # squash_merge_commit_message: Optional[str] = None
    # merge_commit_title: Optional[str] = None
    # merge_commit_message: Optional[str] = None
    # archived: Optional[bool] = None
    # allow_forking: Optional[bool] = None
    # web_commit_signoff_required: Optional[bool] = None

class DeleteRepoParams(BaseModel):
    owner: str
    repo: str

class EnableAutoSecFixesParams(BaseModel):
    owner: str
    repo: str

class DisableAutoSecFixesParams(BaseModel):
    owner: str
    repo: str

class ListCodeownersErrorsParams(BaseModel):
    owner: str
    repo: str

class ListRepoContributorsParams(BaseModel):
    owner: str
    repo: str

class CreateRepoDispatchEventParams(BaseModel):
    owner: str
    repo: str
    event_type: str
    # client_payload: Optional[object] = None

class ListRepoLanguagesParams(BaseModel):
    owner: str
    repo: str

class ListRepoTagsParams(BaseModel):
    owner: str
    repo: str

class ListRepoTeamsParams(BaseModel):
    owner: str
    repo: str

class ListRepoTopicsParams(BaseModel):
    owner: str
    repo: str

class ReplaceRepoTopicsParams(BaseModel):
    owner: str
    repo: str
    names: List[str]

class TransferRepoParams(BaseModel):
    owner: str
    repo: str
    new_owner: str
    # new_name: Optional[str] = None
    # team_ids: Optional[List[int]] = None

class CheckVulnerabilityAlertsParams(BaseModel):
    owner: str
    repo: str

class EnableVulnerabilityAlertsParams(BaseModel):
    owner: str
    repo: str

class DisableVulnerabilityAlertsParams(BaseModel):
    owner: str
    repo: str

class CreateRepoUsingTemplateParams(BaseModel):
    template_owner: str
    template_repo: str
    # owner: Optional[str] = None
    # name: str
    # description: Optional[str] = None
    # include_all_branches: Optional[bool] = None
    # private: Optional[bool] = None
