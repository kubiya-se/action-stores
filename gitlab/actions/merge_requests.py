
from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class ProjectsMergeRequestCreate(BaseModel):

    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user.")
    source_branch: str = Field(description="The source branch name.")
    target_branch: str = Field(description="The target branch name.")
    title: str = Field(description="The title of merge request.")
    allow_collaboration: Optional[bool] = Field(None, description="Allow commits from members who can merge to the target branch.")
    approvals_before_merge: Optional[int] = Field(None, description="The amount of approvals required before merging.")
    allow_maintainer_to_push: Optional[bool] = Field(None, description="Allow users who can merge to the target branch to push to the source branch.")
    assignee_id: Optional[int] = Field(None, description="The ID of a user to assign merge request.")
    assignee_ids: Optional[List[int]] = Field(None, description="The IDs of users to assign merge request.")
    description: Optional[str] = Field(None, description="The description of merge request.")
    labels: Optional[str] = Field(None, description="Comma-separated list of label names.")
    milestone_id: Optional[int] = Field(None, description="The global ID of a milestone to assign merge request.")
    remove_source_branch: Optional[bool] = Field(None, description="Flag indicating if a merge request should remove the source branch when merging.")
    reviewer_ids: Optional[List[int]] = Field(None, description="The IDs of users to request review from when merge request created.")
    squash: Optional[bool] = Field(None, description="Squash commits into a single commit when merging.")
    squash_on_merge: Optional[bool] = Field(None, description="Squash commits into a single commit after merging.")
    target_project_id: Optional[int] = Field(None, description="The target project ID. If the user is a maintainer of the target project, the source project is set as the target_project_id.")


@action_store.kubiya_action()
def create_new_merge_request(input: ProjectsMergeRequestCreate):
    return post_wrapper(endpoint=f"/projects/{input.id}/merge_requests", args=input.dict(exclude_none=True))
