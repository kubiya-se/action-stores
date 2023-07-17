from .. import action_store as action_store
import logging
from ..models.pull_request import *
from ..http_wrapper import get_wrapper, post_wrapper, patch_wrapper, delete_wrapper, put_wrapper

FAILED_MSG = "Insufficient data"

logger = logging.getLogger(__name__)

@action_store.kubiya_action()     
def list_review_comments_in_a_repo(params: ListRepoReviewCommentsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/comments")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()         
def get_a_review_comment_for_a_pull_request(params: GetPrReviewCommentParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/comments/{params.comment_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()         
def update_a_review_comment_for_a_pull_request(params: UpdatePrReviewCommentParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('comment_id')
        resp = patch_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/comments/{params.comment_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()         
def delete_a_review_comment_for_a_pull_request(params: DeletePrReviewCommentParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/comments/{params.comment_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def list_review_comments_for_a_pull_request(params: ListPrReviewCommentsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/{params.pull_number}/comments")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def create_a_review_comment_for_a_pull_request(params: CreatePrReviewCommentParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/{params.pull_number}/comments", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()     
def create_reply_for_a_review_comment(params: CreateRcReplyParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        data.pop('comment_id')
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/{params.pull_number}/comments/{params.comment_id}/replies", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def get_all_requested_reviewers_for_a_pull_request(params: GetAllRequestedReviewersForPrParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/{params.pull_number}/requested_reviewers")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def request_reviewers_for_a_pull_request(params: RequestReviewersForPrParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/{params.pull_number}/requested_reviewers", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()   
def remove_requested_reviewers_from_a_pull_request(params: RemoveRequestedReviewersFromPrParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/{params.pull_number}/requested_reviewers", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()   
def list_reviews_for_a_pull_request(params: ListPrReviewsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/puls/{params.pull_number}/reviews", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()       
def create_a_review_for_a_pull_request(params: CreatePrReviewParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/puls/{params.pull_number}/reviews", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()       
def get_a_review_for_a_pull_reuqest(params: GetPrReviewParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/puls/{params.pull_number}/reviews/{params.review_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()       
def update_a_review_for_a_pull_request(params: UpdatePrReviewParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/puls/{params.pull_number}/reviews/{params.review_id}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()       
def delete_a_pending_review_for_a_pull_request(params: DeletePrPendingReviewParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = delete_wrapper(f"/repos/{params.owner}/{params.repo}/puls/{params.pull_number}/reviews/{params.review_id}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()       
def list_comments_for_a_pull_request_review(params: ListPrReviewCommentsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        data.pop('review_id')
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/puls/{params.pull_number}/reviews/{params.review_id}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def dismiss_a_review_for_a_pull_request(params: DissmissPrReviewParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        data.pop('review_id')
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/puls/{params.pull_number}/reviews/{params.review_id}/dismissals", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()      
def submit_a_review_for_a_pull_request(params: SubmitPrReviewParams):
    data = params.dict(exclude_none = True)
    if data: 
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        data.pop('review_id')
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/puls/{params.pull_number}/reviews/{params.review_id}/events", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def list_pull_requests(params: ListPullRequestsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/pulls")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def create_pull_request(params: CreatePullRequestsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        resp = post_wrapper(f"/repos/{params.owner}/{params.repo}/pulls")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def get_pull_request(params: GetPullRequestParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/{params.pull_number}")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def update_pull_request(params: UpdatePullRequestParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        resp = patch_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/{params.pull_number}", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def list_commits_on_pull_request(params: ListPrCommitsParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/{params.pull_number}/commits", data)
        return resp
    else:
        return FAILED_MSG
    
@action_store.kubiya_action()
def list_pr_requests_files(params: ListPrRequestsFilesParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/{params.pull_number}/files", data)
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def check_if_a_pull_request_has_been_merged(params: CheckPrMergedParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = get_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/{params.pull_number}/merge")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()
def merge_a_pull_request(params: MergePrParams):
    data = params.dict(exclude_none = True)
    if data:
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/{params.pull_number}/merge")
        return resp
    else:
        return FAILED_MSG

@action_store.kubiya_action()    
def update_a_pull_request_branch(params: UpdatePrBranchParams):
    data = params.dict(exclude_none = True)
    if data:
        data.pop('owner')
        data.pop('repo')
        data.pop('pull_number')
        resp = put_wrapper(f"/repos/{params.owner}/{params.repo}/pulls/{params.pull_number}/update-branch", data)
        return resp
    else:
        return FAILED_MSG