from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime


class NotMatch(BaseModel):
    author_id: Optional[int] = Field(None, description="Can exclude by author ID")
    author_username: Optional[str] = Field(None, description="Can exclude by author username (GitLab 14.7 and later)")
    labels: Optional[str] = Field(None, description="Can exclude by labels")

class GroupsIdEpics(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group owned by the authenticated user

    author_id: Optional[int] = None # Return epics created by the given user id

    author_username: Optional[str] = None # Return epics created by the user with the given username. Available in GitLab 14.7 and later

    labels: Optional[str] = None # Return epics matching a comma-separated list of labels names. Label names from the epic group or a parent group can be used

    with_labels_details: Optional[bool] = None # If true, response returns more details for each label in labels field: :name, :color, :description, :description_html, :text_color. Default is false. Available in GitLab 12.7 and later

    order_by: Optional[str] = None # Return epics ordered by created_at, updated_at, or title fields. Default is created_at

    sort: Optional[str] = None # Return epics sorted in asc or desc order. Default is desc

    search: Optional[str] = None # Search epics against their title and description

    state: Optional[str] = None # Search epics against their state, possible filters: opened, closed and all, default: all

    created_after: Optional[datetime] = None # Return epics created on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z)

    created_before: Optional[datetime] = None # Return epics created on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z)

    updated_after: Optional[datetime] = None # Return epics updated on or after the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z)

    updated_before: Optional[datetime] = None # Return epics updated on or before the given time. Expected in ISO 8601 format (2019-03-15T08:00:00Z)

    include_ancestor_groups: Optional[bool] = None # Include epics from the requested group’s ancestors. Default is false

    include_descendant_groups: Optional[bool] = None # Include epics from the requested group’s descendants. Default is true

    my_reaction_emoji: Optional[str] = None # Return epics reacted by the authenticated user by the given emoji. None returns epics not given a reaction. Any returns epics given at least one reaction. Available in GitLab 13.0 and later

    not_: Optional[NotMatch] = Field(None, alias="not", description="Return epics that do not match the parameters supplied")


@action_store.kubiya_action()
def list_epics_for_a_group_0(input: GroupsIdEpics):
    return get_wrapper(endpoint=f"/groups/{input.id}/epics", args=input.dict(exclude_none=True, by_alias = True))


class SingleEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]

@action_store.kubiya_action()
def single_epic(input: SingleEpic):
    return get_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_iid}", args=input.dict(exclude_none=True))

class NewEpicInput(BaseModel):
    id: Union[int, str]  # The ID or URL-encoded path of the group owned by the authenticated user
    title: str  # The title of the epic
    labels: Optional[str]  # The comma-separated list of labels
    description: Optional[str]  # The description of the epic
    color: Optional[str]  # The color of the epic
    confidential: Optional[bool]  # Whether the epic should be confidential
    created_at: Optional[datetime]  # When the epic was created
    start_date_is_fixed: Optional[bool]  # Whether start date should be sourced from start_date_fixed or from milestones
    start_date_fixed: Optional[str]  # The fixed start date of an epic
    due_date_is_fixed: Optional[bool]  # Whether due date should be sourced from due_date_fixed or from milestones
    due_date_fixed: Optional[str]  # The fixed due date of an epic
    parent_id: Optional[Union[int, str]]  # The ID of a parent epic

@action_store.kubiya_action()
def new_epic(input: NewEpicInput):
    return post_wrapper(endpoint=f"/groups/{input.id}/epics", args=input.dict(exclude_none=True))    


class UpdateEpic(BaseModel):

    id: int # The ID or URL-encoded path of the group owned by the authenticated user

    epic_iid: int # The internal ID of the epic

    add_labels: Optional[str] = None # Comma-separated label names to add to an issue.

    confidential: Optional[bool] = None # Whether the epic should be confidential

    description: Optional[str] = None # The description of an epic. Limited to 1,048,576 characters.

    due_date_fixed: Optional[str] = None # The fixed due date of an epic (in GitLab 11.3 and later)

    due_date_is_fixed: Optional[bool] = None # Whether due date should be sourced from due_date_fixed or from milestones (in GitLab 11.3 and later)

    labels: Optional[str] = None # Comma-separated label names for an issue. Set to an empty string to unassign all labels.

    parent_id: Optional[int] = None # The ID of a parent epic. Available in GitLab 14.6 and later

    remove_labels: Optional[str] = None # Comma-separated label names to remove from an issue.

    start_date_fixed: Optional[str] = None # The fixed start date of an epic (in GitLab 11.3 and later)

    start_date_is_fixed: Optional[bool] = None # Whether start date should be sourced from start_date_fixed or from milestones (in GitLab 11.3 and later)

    state_event: Optional[str] = None # State event for an epic. Set close to close the epic and reopen to reopen it (in GitLab 11.4 and later)

    title: Optional[str] = None # The title of an epic

    updated_at: Optional[str] = None # When the epic was updated. Date time string, ISO 8601 formatted, for example 2016-03-11T03:45:40Z . Requires administrator or project/group owner privileges (available in GitLab 13.5 and later)

    color: Optional[str] = None # The color of the epic. Introduced in GitLab 14.8, behind a feature flag named epic_highlight_color (disabled by default)


@action_store.kubiya_action()
def update_epic(input: UpdateEpic):
    return put_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_iid}", args=input.dict(exclude_none=True))


class DeleteEpic(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the group owned by the authenticated user

    epic_iid: Union[int, str] # The internal ID of the epic.


@action_store.kubiya_action()
def delete_epic(input: DeleteEpic):
    return delete_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_iid}", args=input.dict(exclude_none=True))


class CreateAToDoItem(BaseModel):

    id: Union[int,str] # The ID or URL-encoded path of the group owned by the authenticated user

    epic_iid: int # The internal ID of a group’s epic


@action_store.kubiya_action()
def create_a_to_do_item(input: CreateAToDoItem):
    return post_wrapper(endpoint=f"/groups/{input.id}/epics/{input.epic_iid}/todo", args=input.dict(exclude_none=True))
