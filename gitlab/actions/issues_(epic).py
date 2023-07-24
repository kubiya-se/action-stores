from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime

class ListIssuesForAnEpic(BaseModel):
    id: Union[int,str]
    epic_iid: Union[int,str]

@action_store.kubiya_action()
def list_issues_for_an_epic(input: ListIssuesForAnEpic):
    return get_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_iid}/issues")


class AssignIssueToEpic(BaseModel):
    id: Union[int,str]
    epic_iid: Union[int,str]
    issue_id: Union[int,str]

@action_store.kubiya_action()
def assign_issue_to_epic(input: AssignIssueToEpic):
    return post_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_iid}/issues/{input.issue_id}")


class RemoveIssueFromEpic(BaseModel):
    id: Union[int,str]
    epic_iid: Union[int,str]
    epic_issue_id: Union[int,str]

@action_store.kubiya_action()
def remove_issue_from_epic(input: RemoveIssueFromEpic):
    return delete_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_iid}/issues/{input.epic_issue_id}")


class UpdateEpicIssueAssociation(BaseModel):
    id: Union[int,str]
    epic_iid: Union[int,str]
    epic_issue_id: Union[int,str]
    move_before_id: Optional[Union[int,str]] = None
    move_after_id: Optional[Union[int,str]] = None

@action_store.kubiya_action()
def update_epic_issue_association(input: UpdateEpicIssueAssociation):
    return put_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_iid}/issues/{input.epic_issue_id}", args=input.dict(exclude_none=True))
