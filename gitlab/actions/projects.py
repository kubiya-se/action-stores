from typing import List, Any, Optional, Union, Dict
from pydantic import BaseModel, Field, parse_obj_as
from datetime import datetime
from ..models.projects import *

from .. import action_store as action_store
from ..http_wrapper import *


@action_store.kubiya_action()
def list_all_projects(input: ProjectListRequest):
    response = get_wrapper(endpoint=f'/projects', args=input.dict(exclude_none=True))
    return Projects(projects=response)


@action_store.kubiya_action()
def list_user_projects(input: UsersUseridProjects):
    response = get_wrapper(endpoint=f'/users/{input.user_id}/projects', args=input.dict(exclude_none=True))
    return Projects(projects=response)


@action_store.kubiya_action()
def list_projects_a_user_has_contributed_to(input: ListContributed):
    response = get_wrapper(endpoint = f'/users/{input.user_id}/contributed_projects', args = input.dict(exclude_none = True))
    return Projects(projects=response)


@action_store.kubiya_action()
def list_projects_starred_by_a_user(input: UsersUseridProjects):
    response = get_wrapper(endpoint=f'/users/{input.user_id}/starred_projects', args=input.dict(exclude_none=True))
    return Projects(projects=response)


@action_store.kubiya_action()
def get_single_project(input: ProjectsIdSingleProjectSingle):
    response = get_wrapper(endpoint=f'/projects/{input.id}', args=input.dict(exclude_none=True))
    return SingleProject(projects=response)


@action_store.kubiya_action()
def get_project_users(input: ProjectsIdUsers):
    response = get_wrapper(endpoint=f'/projects/{input.id}/users', args=input.dict(exclude_none=True))
    return Users(users = response)


@action_store.kubiya_action()
def list_a_projects_groups(input: ProjectsIdGroups):
    response = get_wrapper(endpoint=f'/projects/{input.id}/groups', args=input.dict(exclude_none=True))
    return Groups(groups = response)

@action_store.kubiya_action()
def list_a_projects_shareable_groups(input: ProjectsIdSharelocations):
    response = get_wrapper(endpoint=f'/projects/{input.id}/share_locations', args=input.dict(exclude_none=True))
    return Groups(groups = response)

@action_store.kubiya_action()
def create_project(input: CreateProjectRequest):
    response = post_wrapper(endpoint='/projects', args=input.dict(exclude_none=True))
    return SingleProject(projects=response)

# @action_store.kubiya_action()
# def create_project_for_user(input: ProjectsUserUserid):
#     response = post_wrapper(endpoint=f'/projects/user/{input.user_id}', args=input.dict(exclude_none=True))
#     return SingleProject(projects=response)


@action_store.kubiya_action()
def edit_project(input: ProjectsIdEdit):
    response = put_wrapper(endpoint=f'/projects/{input.id}', args=input.dict(exclude_none=True))
    return SingleProject(projects=response)


# @action_store.kubiya_action()
# def fork_project(input: ProjectsIdFork):
#     return post_wrapper(endpoint=f'/projects/{input.id}/fork', args=input.dict(exclude_none=True))


# @action_store.kubiya_action()
# def list_forks_of_a_project(input: ProjectsIdForks):
#     response = get_wrapper(endpoint=f'/projects/{input.id}/forks', args=input.dict(exclude_none=True))
#     return parse_obj_as(List[Project], response)

# @action_store.kubiya_action()
# def star_a_project(input: ProjectsIdStar):
#     response = post_wrapper(endpoint=f'/projects/{input.id}/star', args=input.dict(exclude_none=True))
#     return parse_obj_as(List[Project], response)

# @action_store.kubiya_action()
# def unstar_a_project(input: ProjectsIdUnstar):
#     response =  post_wrapper(endpoint=f'/projects/{input.id}/unstar', args=input.dict(exclude_none=True))
#     return parse_obj_as(List[Project], response)

# class Starrer(BaseModel):
#     starred_sinced: Optional[datetime]
#     user: User

# @action_store.kubiya_action()
# def list_starrers_of_a_project(input: ProjectsIdStarrers):
#     return get_wrapper(endpoint=f'/projects/{input.id}/starrers', args=input.dict(exclude_none=True))


# class LanguagePercentages(BaseModel):
#     languages: Dict[str, float]

# @action_store.kubiya_action()
# def languages(input: ProjectsIdLanguages):
#     response = get_wrapper(endpoint=f'/projects/{input.id}/languages', args=input.dict(exclude_none=True))
#     return parse_obj_as(List[LanguagePercentages], response)

# @action_store.kubiya_action()
# def archive_a_project(input: ProjectsIdArchive):
#     response = post_wrapper(endpoint=f'/projects/{input.id}/archive', args=input.dict(exclude_none=True))
#     return parse_obj_as(List[Project], response)

# @action_store.kubiya_action()
# def unarchive_a_project(input: ProjectsIdUnarchive):
#     response = post_wrapper(endpoint=f'/projects/{input.id}/unarchive', args=input.dict(exclude_none=True))
#     return parse_obj_as(List[Project], response)

# @action_store.kubiya_action()
# def delete_project(input: ProjectsIdDelete):
#     return delete_wrapper(endpoint=f'/projects/{input.id}', args=input.dict(exclude_none=True))

# @action_store.kubiya_action()
# def restore_project_marked_for_deletion_(input: ProjectsIdRestore):
#     return post_wrapper(endpoint=f'/projects/{input.id}/restore', args=input.dict(exclude_none=True))

# class FileUpload(BaseModel):
#     alt: Optional[str]
#     url: Optional[str]
#     full_path: Optional[str]
#     markdown: Optional[str]

# @action_store.kubiya_action()
# def upload_a_file(input: ProjectsIdUploads):
#     response = post_wrapper(endpoint=f'/projects/{input.id}/uploads', args=input.dict(exclude_none=True))
#     return parse_obj_as(FileUpload, response)

# class AvatarResponse(BaseModel):
#     avatar_url: Optional[str]

# @action_store.kubiya_action()
# def upload_a_project_avatar(input: ProjectsIdAvatar):
#     response = put_wrapper(endpoint=f'/projects/{input.id}', args=input.dict(exclude_none=True))
#     return parse_obj_as(AvatarResponse, response)

# @action_store.kubiya_action()
# def remove_a_project_avatar(input: ProjectsIdAvatar):
#     return put_wrapper(endpoint=f'/projects/{input.id}', args={'avatar': ''})
# @action_store.kubiya_action()
# def share_project_with_group(input: ProjectsIdShare):
#     return post_wrapper(endpoint=f'/projects/{input.id}/share', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def delete_a_shared_project_link_within_a_group(input: ProjectsIdShareGroupid):
#     return delete_wrapper(endpoint=f'/projects/{input.id}/share/{input.group_id}', args=input.dict(exclude_none=True))

# @action_store.kubiya_action()
# def import_project_members(input: ProjectsIdImportprojectmembersProjectid):
#     return post_wrapper(endpoint=f'/projects/{input.id}/import_project_members/{input.project_id}', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def list_project_hooks(input: ProjectsIdHooksList):
#     return get_wrapper(endpoint=f'/projects/{input.id}/hooks', args=input.dict(exclude_none=True))


# @action_store.kubiya_action()
# def get_project_hook(input: ProjectsIdGetProjectHook):
#     response =  get_wrapper(endpoint=f'/projects/{input.id}/hooks/{input.hook_id}', args=input.dict(exclude_none=True))
#     return parse_obj_as(Project, response)

# @action_store.kubiya_action()
# def add_project_hook(input: ProjectsIdHooks):
#     return post_wrapper(endpoint=f'/projects/{input.id}/hooks', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def edit_project_hook(input: ProjectsIdEditProjectHook):
#     return put_wrapper(endpoint=f'/projects/{input.id}/hooks/{input.hook_id}', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def delete_project_hook(input: ProjectsIdDeleteProjectHook):
#     return delete_wrapper(endpoint=f'/projects/{input.id}/hooks/{input.hook_id}', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def create_a_forked_from_to_relation_between_existing_projects(input: CreatedForkedRelationship):
#     return post_wrapper(endpoint=f'/projects/{input.id}/fork/{input.forked_from_id}', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def delete_an_existing_forked_from_relationship(input: DeleteExistingForkedRelationship):
#     return delete_wrapper(endpoint=f'/projects/{input.id}/fork', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def search_for_projects_by_name(input: ProjectsByNameRequest):
#     return get_wrapper(endpoint=f'/projects', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def start_the_housekeeping_task_for_a_project(input: ProjectsIdHousekeeping):
#     return post_wrapper(endpoint=f'/projects/{input.id}/housekeeping', args=input.dict(exclude_none=True))

# class ProjectSettings(BaseModel):
#     id: Optional[int]
#     project_id: Optional[int]
#     commit_message_regex: Optional[str]
#     commit_message_negative_regex: Optional[str]
#     branch_name_regex: Optional[str]
#     deny_delete_tag: Optional[bool]
#     created_at: Optional[datetime]
#     member_check: Optional[bool]
#     prevent_secrets: Optional[bool]
#     author_email_regex: Optional[str]
#     file_name_regex: Optional[str]
#     max_file_size: Optional[int]
#     commit_committer_check: Optional[bool]
#     reject_unsigned_commits: Optional[bool]

# @action_store.kubiya_action()
# def get_project_push_rules(input: ProjectsIdPushrule):
#     response = get_wrapper(endpoint=f'/projects/{input.id}/push_rule', args=input.dict(exclude_none=True))
#     return parse_obj_as(ProjectSettings, response)

# @action_store.kubiya_action()
# def push_rules_(input: ProjectsIdPushruleAdd):
#     return post_wrapper(endpoint=f'/projects/{input.id}/push_rule', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def push_rules_(input: ProjectsIdPushruleEdit):
#     return put_wrapper(endpoint=f'/projects/{input.id}/push_rule', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def delete_project_push_rule(input: ProjectsIdPushruleDelete):
#     return delete_wrapper(endpoint=f'/projects/{input.id}/push_rule', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def get_groups_to_which_a_user_can_transfer_a_project(input: ProjectsIdTransferlocations):
#     response =  get_wrapper(endpoint=f'/projects/{input.id}/transfer_locations', args=input.dict(exclude_none=True))
#     return parse_obj_as(List[Group], response)
# @action_store.kubiya_action()
# def transfer_a_project_to_a_new_namespace(input: ProjectsIdTransfer):
#     response =  put_wrapper(endpoint=f'/projects/{input.id}/transfer', args=input.dict(exclude_none=True))
#     return parse_obj_as(Project, response)

# class PullMirrorDetails(BaseModel):
#     id: Optional[str]
#     last_error: Optional[str]
#     last_sucessful_update_at: Optional[datetime]
#     last_update_at: Optional[datetime]
#     last_update_started_at: Optional[datetime]
#     update_status: Optional[str]
#     url: Optional[str]

# @action_store.kubiya_action()
# def get_a_projects_pull_mirror_details_(input: ProjectsIdMirrorPull):
#     response = get_wrapper(endpoint=f'/projects/{input.id}/mirror/pull', args=input.dict(exclude_none=True))
#     return parse_obj_as(PullMirrorDetails, response)
# @action_store.kubiya_action()
# def start_the_pull_mirroring_process_for_a_project_(input: ProjectsIdMirrorPullStart):
#     return post_wrapper(endpoint=f'/projects/{input.id}/mirror/pull', args=input.dict(exclude_none=True))
# @action_store.kubiya_action()
# def download_snapshot_of_a_git_repository(input: ProjectsIdSnapshot):
#     return get_wrapper(endpoint=f'/projects/{input.id}/snapshot', args=input.dict(exclude_none=True))

# class PathToRepositoryStorage(BaseModel):
#     project_id: Optional[str]
#     disk_path: Optional[str]
#     created_at: Optional[datetime]
#     repository_storage: Optional[str]

# @action_store.kubiya_action()
# def get_the_path_to_repository_storage(input: ProjectsIdStorage):
#     response =  get_wrapper(endpoint=f'/projects/{input.id}/storage', args=input.dict(exclude_none=True))
#     return parse_obj_as(PathToRepositoryStorage, response)