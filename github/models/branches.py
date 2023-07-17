from pydantic import BaseModel
from typing import Optional, List


class ListBranchesParams(BaseModel):
    owner: str
    repo: str
    protected: Optional[bool]
    per_page: Optional[int]
    page: Optional[int]

class GetBranchParams(BaseModel):
    owner: str
    repo: str
    branch: str

class RenameBranchParams(BaseModel):
    owner: str
    repo: str
    branch: str
    new_name: str

class SyncForkWithUpstreamParams(BaseModel):
    owner: str
    repo: str
    branch: str

class MergeBranchParams(BaseModel):
    owner: str
    repo: str
    base: str
    head: str
    commit_message: Optional[str]

class GetBranchProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str

class UpdateBranchProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str
    required_status_checks: Union[object, None]
    enforce_admins: Union[bool, None]
    required_pull_request_reviews: Union[object, None]
    restrictions: Union[object, None]
    required_linear_history: Optional[bool]
    allow_force_pushes: Optional[Union[bool, None]]
    allow_deletions: Optional[bool]
    block_creations: Optional[bool]
    required_conversation_resolution: Optional[bool]
    lock_branch: Optional[bool]
    allow_fork_synching: Optional[bool]

class DeleteBranchProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str

class GetAdminBranchProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str

class SetAdminBranchProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str

class DeleteAdminBranchProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str

class GetPrRequestReviewProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str

class UpdatePullRequestReviewProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str
    dismissal_restrictions: Optional[object]
    dismiss_stale_reviews: Optional[bool]
    require_code_owner_reviews: Optional[bool]
    required_approving_review_count: Optional[int]
    require_last_push_approval: Optional[bool]
    bypass_pull_request_allowances: Optional[object]

class DeletePullRequestReviewProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str

class GetCommitSignatureProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str

class CreateCommitSignatureProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str

class DeleteCommitSignatureProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str

class GetStatusChecksProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str

class UpdateStatusChecksProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str
    strict: Optional[bool]
    contexts: Optional[List[str]]
    checks: Optional[List[object]]

class DeleteStatusChecksProtectionParams(BaseModel):
    owner: str
    repo: str
    branch: str

class GetAllStatusCheckContextsParams(BaseModel):
    owner: str
    repo: str
    branch: str

class AddStatusCheckContextsParams(BaseModel):
    owner: str
    repo: str
    branch: str
    contexts: List[str]

class SetStatusCheckContextsParams(BaseModel):
    owner: str
    repo: str
    branch: str
    contexts: List[str]

class RemoveStatusCheckContextsParams(BaseModel):
    owner: str
    repo: str
    branch: str
    contexts: List[str]

class GetAccessRestrictionsParams(BaseModel):
    owner: str
    repo: str
    branch: str

class DeleteAccessRestrictionsParams(BaseModel):
    owner: str
    repo: str
    branch: str

class GetAppsWithProtectedBranchAccessParams(BaseModel):
    owner: str
    repo: str
    branch: str

class AddAppAccessRestrictionsParams(BaseModel):
    owner: str
    repo: str
    branch: str
    apps: List[str]

class SetAppAccessRestrictionsParams(BaseModel):
    owner: str
    repo: str
    branch: str
    apps: List[str]

class RemoveAppAccessRestrictionsParams(BaseModel):
    owner: str
    repo: str
    branch: str
    apps: List[str]

class GetTeamsWithAccessToProtectedBranchParams(BaseModel):
    owner: str
    repo: str
    branch: str

class AddTeamAccessRestrictionsParams(BaseModel):
    owner: str
    repo: str
    branch: str
    apps: List[str]

class SetTeamAccessRestrictionsParams(BaseModel):
    owner: str
    repo: str
    branch: str
    apps: List[str]

class RemoveTeamAccessRestrictionsParams(BaseModel):
    owner: str
    repo: str
    branch: str
    apps: List[str]  

class GetUsersWithAccessToProtectedBranchParams(BaseModel):
    owner: str
    repo: str
    branch: str

class AddUserAccessRestrictionsParams(BaseModel):
    owner: str
    repo: str
    branch: str
    apps: List[str]

class SetUserAccessRestrictionsParams(BaseModel):
    owner: str
    repo: str
    branch: str
    apps: List[str]

class RemoveUserAccessRestrictionsParams(BaseModel):
    owner: str
    repo: str
    branch: str
    apps: List[str]