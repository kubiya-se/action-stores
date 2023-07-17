from pydantic import BaseModel
from typing import Optional, List

class ListRepoReviewCommentsParams(BaseModel):
    owner: str
    repo: str
    sort: Optional[str]
    direction: Optional[str]
    since: Optional[str]
    per_page: Optional[int]
    page: Optional[int]

class GetPrReviewCommentParams(BaseModel):
    owner: str
    repo: str
    comment_id: int

class UpdatePrReviewCommentParams(BaseModel):
    owner: str
    repo: str
    comment_id: int
    body: str

class DeletePrReviewCommentParams(BaseModel):
    owner: str
    repo: str
    comment_id: int

class ListPrReviewCommentsParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    sort: Optional[str]
    direction: Optional[str]
    since: Optional[str]
    per_page: Optional[int]
    page: Optional[int]

class CreatePrReviewCommentParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    body: str
    commit_id: str
    path: str
    position: Optional[int]
    side: Optional[str]
    line: Optional[int]
    start_line: Optional[int]
    start_side: Optional[str]
    in_reply_to: Optional[int]
    subject_type: Optional[str]

class CreateRcReplyParams(BaseModel):
    owner: str
    repo: str
    pull_number: str
    comment_id: int
    body: str

class GetAllRequestedReviewersForPrParams(BaseModel):
    owner: str
    repo: str
    pull_number: int

class RequestReviewersForPrParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    reviewers: Optional[List[str]]
    team_reviewers: Optional[List[str]]

class RemoveRequestedReviewersFromPrParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    reviewers: List[str]
    team_reviewers: Optional[List[str]]

class ListPrReviewsParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    per_page: Optional[int]
    page: Optional[int]

class CreatePrReviewParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    commit_id: Optional[int]
    body: Optional[str]
    event: Optional[str]
    comments: List[object]

class GetPrReviewParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    review_id: int

class UpdatePrReviewParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    review_id: int
    body: str

class DeletePrPendingReviewParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    review_id: int

class ListPrReviewCommentsParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    review_id: int
    per_page: Optional[int]
    page: Optional[int]

class DissmissPrReviewParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    review_id: int
    message: str
    event: Optional[str]

class SubmitPrReviewParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    review_id: int
    body: Optional[str]
    event: str

class ListPullRequestsParams(BaseModel):
    owner: str
    repo: str
    state: Optional[str]
    head: Optional[str]
    base: Optional[str]
    sort: Optional[str]
    direction: Optional[str]
    per_page: Optional[int]
    page: Optional[int]

class CreatePullRequestsParams(BaseModel):
    owner: str
    repo: str
    title: Optional[str]
    head: str
    head_repo: Optional[str]
    base: str
    body: Optional[str]
    maintainer_can_modify: Optional[bool]
    draft: Optional[bool]
    issue: Optional[int]

class GetPullRequestParams(BaseModel):
    owner: str
    repo: str
    pull_number: int

class UpdatePullRequestParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    title: Optional[str]
    body: Optional[str]
    state: Optional[str]
    base: Optional[str]
    maintainer_can_modify: Optional[str]

class ListPrCommitsParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    per_page: Optional[int]
    page: Optional[int]

class ListPrRequestsFilesParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    per_page: Optional[int]
    page: Optional[int]

class CheckPrMergedParams(BaseModel):
    owner: str
    repo: str
    pull_number: int

class MergePrParams(BaseModel):
    owner: str
    repo: str
    pull_number: int

class UpdatePrBranchParams(BaseModel):
    owner: str
    repo: str
    pull_number: int
    expected_head_sha: Optional[str]
