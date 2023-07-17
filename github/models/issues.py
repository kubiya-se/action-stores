from pydantic import BaseModel
from typing import List, Optional, Union

class ListIssuesParams(BaseModel):
    filter: Optional[str]
    state: Optional[str]
    labels: Optional[str]
    sort: Optional[str]
    direction: Optional[str]
    since: Optional[str]
    collab: Optional[bool]
    orgs: Optional[bool]
    owned: Optional[bool]
    pulls: Optional[bool]
    per_page: Optional[int]
    page: Optional[int]

class ListOrganizationIssuesParams(BaseModel):
    org: set
    filter: Optional[str]
    state: Optional[str]
    labels: Optional[str]
    sort: Optional[str]
    direction: Optional[str]
    since: Optional[str]
    per_page: Optional[int]
    page: Optional[int]

class ListRepositoryIssuesParams(BaseModel):
    owner: str
    repo: str
    milestone: Optional[str]
    state: Optional[str]
    assignee: Optional[str]
    creator: Optional[str]
    mentioned: Optional[str]
    labels: Optional[str]
    sort: Optional[str]
    direction: Optional[str]
    since: Optional[str]
    per_page: Optional[int]
    page: Optional[int]

class CreateIssueParams(BaseModel):
    owner: str
    repo: str
    title: str
    body: Optional[str]
    assignee: Optional[Union[str, None]]
    milestone: Optional[Union[Union[str, int], None]]
    labels: Optional[List]
    assignees: Optional[List[str]]


class GetIssueParams(BaseModel):
    owner: str
    repo: str
    issue_number: int

class UpdateIssueParams(BaseModel):
    owner: str
    repo: str
    issue_number: int
    title: Optional[Union[Union[str, int], None]]
    body: Optional[str]
    assignee: Optional[Union[str, None]]
    state: Optional[str]
    state_reason: Optional[Union[str, None]]
    milestone: Optional[Union[Union[str, int], None]]
    labels: Optional[List]
    assignees: Optional[List[str]]

class LockIsuseParams(BaseModel):
    owner: str
    repo: str
    issue_number: int
    lock_reason: Optional[str]

class UnlockIssueParams(BaseModel):
    owner: str
    repo: str
    issue_number: int

class ListAccountIssuesAssignedToUserParams(BaseModel):
    filter: Optional[str]
    state: Optional[str]
    labels: Optional[str]
    sort: Optional[str]
    direction: Optional[str]
    since: Optional[str]
    per_page: Optional[int]
    page: Optional[int]

class ListAssigneesParams(BaseModel):
    owner: str
    repo: str
    per_page: Optional[int]
    page: Optional[int]

class CheckUserAssignabilityParams(BaseModel):
    owner: str
    repo: str
    assignee: str

class AddAssigneesToIssueParams(BaseModel):
    owner: str
    repo: str
    issue_number: int
    assignees: Optional[List[str]]

class RemoveAssigneesFromIssueParams(BaseModel):
    owner: str
    repo: str
    issue_number: int
    assignees: Optional[List[str]]

class CheckIfUserCanBeAssignedToIssueParams(BaseModel):
    owner: str
    repo: str
    issue_number: int
    assignee: str

class ListIssueCommentsForARepositoryParams(BaseModel):
    owner: str
    repo: str
    sort: Optional[str]
    direction: Optional[str]
    since: Optional[str]
    per_page: Optional[int]
    page: Optional[int]

class GetIssueCommentParams(BaseModel):
    owner: str
    repo: str
    comment_id: int

class UpdateIssueCommentParams(BaseModel):
    owner: str
    repo: str
    comment_id: int
    body: str    

class DeleteIssueCommentParams(BaseModel):
    owner: str
    repo: str
    comment_id: int

class ListIssueCommentsParams(BaseModel):
    owner: str
    repo: str
    issue_number: int
    since: Optional[str]
    per_page: Optional[int]
    page: Optional[int]

class CreateIssueCommentParams(BaseModel):
    owner: str
    repo: str
    issue_number: int
    body: str    

class ListIssueEventsForRepoParams(BaseModel):
    owner: str
    repo: str
    per_page: Optional[int]
    page: Optional[int]

class GetIssueEventParams(BaseModel):
    owner: str
    repo: str
    event_id: int

class ListIssueEventsParams(BaseModel):
    owner: str
    repo: str
    issue_number: int
    per_page: Optional[int]
    page: Optional[int]

class ListIssueLabelsParams(BaseModel):
    owner: str
    repo: str
    issue_number: int
    per_page: Optional[int]
    page: Optional[int]

class AddIssueLabelsParams(BaseModel):
    owner: str
    repo: str
    issue_number: int
    labels: Optional[List[str]]

class SetIssueLabelsParams(BaseModel):
    owner: str
    repo: str
    issue_number: int
    labels: Optional[List[str]]

class RemoveIssueLabelsParams(BaseModel):
    owner: str
    repo: str
    issue_number: int

class RemoveIssueLabelParams(BaseModel):
    owner: str
    repo: str
    issue_number: int
    name: str

class ListRepoIssueLabelsParams(BaseModel):
    owner: str
    repo: str
    per_page: Optional[int]
    page: Optional[int]

class CreateLabelParams(BaseModel):
    owner: str
    repo: str
    name: str
    color: Optional[str]
    description: Optional[str]

class GetLabelParams(BaseModel):
    owner: str
    repo: str
    name: str

class UpdateLabelParams(BaseModel):
    owner: str
    repo: str
    name: str
    new_name: Optional[str]
    color: Optional[str]
    description: Optional[str]

class DeleteLabelParams(BaseModel):
    owner: str
    repo: str
    name: str

class ListIssueLabelsInMilestoneParams(BaseModel):
    owner: str
    repo: str
    milestone_number: int
    per_page: Optional[int]
    page: Optional[int]

class ListMilestonesParams(BaseModel):
    owner: str
    repo: str
    state: Optional[str]
    sort: Optional[str]
    direction: Optional[str]
    per_page: Optional[int]
    page: Optional[int]

class CreateMilestoneParams(BaseModel):
    owner: str
    repo: str
    title: str
    state: Optional[str]
    description: Optional[str]
    due_on: Optional[str]

class GetMilestonesParams(BaseModel):
    owner: str
    repo: str
    milestone_number: int

class UpdateMilestoneParams(BaseModel):
    owner: str
    repo: str
    milestone_number: int
    title: Optional[str]
    state: Optional[str]
    description: Optional[str]
    due_on: Optional[str]

class DeleteMilestonesParams(BaseModel):
    owner: str
    repo: str
    milestone_number: int

class ListTimelineEventsForIssueParams(BaseModel):
    owner: str
    repo: str
    issue_number: int 
    per_page: Optional[int]
    page: Optional[int]








