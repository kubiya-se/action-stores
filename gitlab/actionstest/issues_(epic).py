from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.issues_(epic) import *
@action_store.kubiya_action()
def list_issues_for_an_epic(input: ListIssuesForAnEpic):
    return get_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_iid}/issues')
@action_store.kubiya_action()
def assign_issue_to_epic(input: AssignIssueToEpic):
    return post_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_iid}/issues/{input.issue_id}')
@action_store.kubiya_action()
def remove_issue_from_epic(input: RemoveIssueFromEpic):
    return delete_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_iid}/issues/{input.epic_issue_id}')
@action_store.kubiya_action()
def update_epic_issue_association(input: UpdateEpicIssueAssociation):
    return put_wrapper(endpoint=f'/groups/{input.id}/epics/{input.epic_iid}/issues/{input.epic_issue_id}', args=input.dict(exclude_none=True))