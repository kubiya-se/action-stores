from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
from modeltest.projects import *
@action_store.kubiya_action()
def list_all_projects(input: ProjectListRequest):
    return get_wrapper(endpoint=f'/projects', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_user_projects(input: UsersUseridProjects):
    return get_wrapper(endpoint=f'/users/{input.user_id}/projects', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_projects_starred_by_a_user(input: UsersUseridStarredprojects):
    return get_wrapper(endpoint=f'/users/{input.user_id}/starred_projects', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_single_project(input: ProjectsIdSingleProjectSingle):
    return get_wrapper(endpoint=f'/projects/{input.id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_project_users(input: ProjectsIdUsers):
    return get_wrapper(endpoint=f'/projects/{input.id}/users', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_a_projects_groups(input: ProjectsIdGroups):
    return get_wrapper(endpoint=f'/projects/{input.id}/groups', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_a_projects_shareable_groups(input: ProjectsIdSharelocations):
    return get_wrapper(endpoint=f'/projects/{input.id}/share_locations', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_project(input: CreateProjectRequest):
    return post_wrapper(endpoint='/projects', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_project_for_user(input: ProjectsUserUserid):
    return post_wrapper(endpoint=f'/projects/user/{input.user_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def edit_project(input: ProjectsIdEdit):
    return put_wrapper(endpoint=f'/projects/{input.id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def fork_project(input: ProjectsIdFork):
    return post_wrapper(endpoint=f'/projects/{input.id}/fork', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_forks_of_a_project(input: ProjectsIdForks):
    return get_wrapper(endpoint=f'/projects/{input.id}/forks', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def star_a_project(input: ProjectsIdStar):
    return post_wrapper(endpoint=f'/projects/{input.id}/star', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def unstar_a_project(input: ProjectsIdUnstar):
    return post_wrapper(endpoint=f'/projects/{input.id}/unstar', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_starrers_of_a_project(input: ProjectsIdStarrers):
    return get_wrapper(endpoint=f'/projects/{input.id}/starrers', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def languages(input: ProjectsIdLanguages):
    return get_wrapper(endpoint=f'/projects/{input.id}/languages', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def archive_a_project(input: ProjectsIdArchive):
    return post_wrapper(endpoint=f'/projects/{input.id}/archive', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def unarchive_a_project(input: ProjectsIdUnarchive):
    return post_wrapper(endpoint=f'/projects/{input.id}/unarchive', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_project(input: ProjectsIdDelete):
    return delete_wrapper(endpoint=f'/projects/{input.id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def restore_project_marked_for_deletion_(input: ProjectsIdRestore):
    return post_wrapper(endpoint=f'/projects/{input.id}/restore', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def upload_a_file(input: ProjectsIdUploads):
    return post_wrapper(endpoint=f'/projects/{input.id}/uploads', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def upload_a_project_avatar(input: ProjectsIdAvatar):
    return put_wrapper(endpoint=f'/projects/{input.id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def remove_a_project_avatar(input: ProjectsIdAvatar):
    return put_wrapper(endpoint=f'/projects/{input.id}', args={'avatar': ''})
@action_store.kubiya_action()
def share_project_with_group(input: ProjectsIdShare):
    return post_wrapper(endpoint=f'/projects/{input.id}/share', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_a_shared_project_link_within_a_group(input: ProjectsIdShareGroupid):
    return delete_wrapper(endpoint=f'/projects/{input.id}/share/{input.group_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def import_project_members(input: ProjectsIdImportprojectmembersProjectid):
    return post_wrapper(endpoint=f'/projects/{input.id}/import_project_members/{input.project_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def list_project_hooks(input: ProjectsIdHooksList):
    return get_wrapper(endpoint=f'/projects/{input.id}/hooks', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_project_hook(input: ProjectsIdGetProjectHook):
    return get_wrapper(endpoint=f'/projects/{input.id}/hooks/{input.hook_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def add_project_hook(input: ProjectsIdHooks):
    return post_wrapper(endpoint=f'/projects/{input.id}/hooks', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def edit_project_hook(input: ProjectsIdEditProjectHook):
    return put_wrapper(endpoint=f'/projects/{input.id}/hooks/{input.hook_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_project_hook(input: ProjectsIdDeleteProjectHook):
    return delete_wrapper(endpoint=f'/projects/{input.id}/hooks/{input.hook_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def create_a_forked_from_to_relation_between_existing_projects(input: CreatedForkedRelationship):
    return post_wrapper(endpoint=f'/projects/{input.id}/fork/{input.forked_from_id}', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_an_existing_forked_from_relationship(input: DeleteExistingForkedRelationship):
    return delete_wrapper(endpoint=f'/projects/{input.id}/fork', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def search_for_projects_by_name(input: ProjectsByNameRequest):
    return get_wrapper(endpoint=f'/projects', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def start_the_housekeeping_task_for_a_project(input: ProjectsIdHousekeeping):
    return post_wrapper(endpoint=f'/projects/{input.id}/housekeeping', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def push_rules_(input: ProjectsIdPushrule):
    return get_wrapper(endpoint=f'/projects/{input.id}/push_rule', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def push_rules_(input: ProjectsIdPushruleAdd):
    return post_wrapper(endpoint=f'/projects/{input.id}/push_rule', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def push_rules_(input: ProjectsIdPushruleEdit):
    return put_wrapper(endpoint=f'/projects/{input.id}/push_rule', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def delete_project_push_rule(input: ProjectsIdPushruleDelete):
    return delete_wrapper(endpoint=f'/projects/{input.id}/push_rule', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_groups_to_which_a_user_can_transfer_a_project(input: ProjectsIdTransferlocations):
    return get_wrapper(endpoint=f'/projects/{input.id}/transfer_locations', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def transfer_a_project_to_a_new_namespace(input: ProjectsIdTransfer):
    return put_wrapper(endpoint=f'/projects/{input.id}/transfer', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_a_projects_pull_mirror_details_(input: ProjectsIdMirrorPull):
    return get_wrapper(endpoint=f'/projects/{input.id}/mirror/pull', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def start_the_pull_mirroring_process_for_a_project_(input: ProjectsIdMirrorPullStart):
    return post_wrapper(endpoint=f'/projects/{input.id}/mirror/pull', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def download_snapshot_of_a_git_repository(input: ProjectsIdSnapshot):
    return get_wrapper(endpoint=f'/projects/{input.id}/snapshot', args=input.dict(exclude_none=True))
@action_store.kubiya_action()
def get_the_path_to_repository_storage(input: ProjectsIdStorage):
    return get_wrapper(endpoint=f'/projects/{input.id}/storage', args=input.dict(exclude_none=True))