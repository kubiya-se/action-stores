from cmd import IDENTCHARS
from typing import List, Any, Optional, Union, Union
from enum import Enum
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from ..actions.http_wrapper import *
from datetime import datetime

class ProjectListRequest(BaseModel):
    archived: Optional[bool] = Field(None)
    id_after: Optional[int] = Field(None)
    id_before: Optional[int] = Field(None)
    imported: Optional[bool] = Field(None)
    last_activity_after: Optional[datetime] = Field(None)
    last_activity_before: Optional[datetime] = Field(None)
    membership: Optional[bool] = Field(None)
    min_access_level: Optional[int] = Field(None)
    order_by: Optional[str] = Field(None)
    owned: Optional[bool] = Field(None)
    repository_checksum_failed: Optional[bool] = Field(None)
    repository_storage: Optional[str] = Field(None)
    search_namespaces: Optional[bool] = Field(None)
    search: Optional[str] = Field(None)
    simple: Optional[bool] = Field(None)
    sort: Optional[str] = Field(None)
    starred: Optional[bool] = Field(None)
    statistics: Optional[bool] = Field(None)
    topic: Optional[str] = Field(None)
    topic_id: Optional[int] = Field(None)
    visibility: Optional[str] = Field(None)
    wiki_checksum_failed: Optional[bool] = Field(None)
    with_custom_attributes: Optional[bool] = Field(None)
    with_issues_enabled: Optional[bool] = Field(None)
    with_merge_requests_enabled: Optional[bool] = Field(None)
    with_programming_language: Optional[str] = Field(None)
    updated_before: Optional[datetime] = Field(None)
    updated_after: Optional[datetime] = Field(None)
    custom_attributes: Optional[Dict[str, str]] = Field(None, description="A dictionary of custom attributes to filter by")


@action_store.kubiya_action()
def list_all_projects(input: ProjectListRequest):
    return get_wrapper(endpoint=f"/projects", args=input.dict(exclude_none=True))


class UsersUseridProjects(BaseModel):

    user_id: str # The ID or username of the user.

    archived: Optional[bool] = None # Limit by archived status.

    id_after: Optional[int] = None # Limit results to projects with IDs greater than the specified ID.

    id_before: Optional[int] = None # Limit results to projects with IDs less than the specified ID.

    membership: Optional[bool] = None # Limit by projects that the current user is a member of.

    min_access_level: Optional[int] = None # Limit by current user minimal role (access_level).

    order_by: Optional[str] = None # Return projects ordered by id, name, path, created_at, updated_at, or last_activity_at fields. Default is created_at.

    owned: Optional[bool] = None # Limit by projects explicitly owned by the current user.

    search: Optional[str] = None # Return list of projects matching the search criteria.

    simple: Optional[bool] = None # Return only limited fields for each project. Without authentication, this operation is a no-op; only simple fields are returned.

    sort: Optional[str] = None # Return projects sorted in asc or desc order. Default is desc.

    starred: Optional[bool] = None # Limit by projects starred by the current user.

    statistics: Optional[bool] = None # Include project statistics. Available only to users with at least the Reporter role.

    visibility: Optional[str] = None # Limit by visibility public, internal, or private.

    with_custom_attributes: Optional[bool] = None # Include custom attributes in response. (administrator only)

    with_issues_enabled: Optional[bool] = None # Limit by enabled issues feature.

    with_merge_requests_enabled: Optional[bool] = None # Limit by enabled merge requests feature.

    with_programming_language: Optional[str] = None # Limit by projects which use the given programming language.

    updated_before: Optional[datetime] = None # Limit results to projects last updated before the specified time. Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ). Introduced in GitLab 15.10.

    updated_after: Optional[datetime] = None # Limit results to projects last updated after the specified time. Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ). Introduced in GitLab 15.10.


@action_store.kubiya_action()
def list_user_projects(input: UsersUseridProjects):
    return get_wrapper(endpoint=f"/users/{input.user_id}/projects", args=input.dict(exclude_none=True))


class UsersUseridStarredprojects(BaseModel):

    user_id: str # The ID or username of the user.

    archived: Optional[bool] = None # Limit by archived status.

    membership: Optional[bool] = None # Limit by projects that the current user is a member of.

    min_access_level: Optional[int] = None # Limit by current user minimal role (access_level).

    order_by: Optional[str] = None # Return projects ordered by id, name, path, created_at, updated_at, or last_activity_at fields. Default is created_at.

    owned: Optional[bool] = None # Limit by projects explicitly owned by the current user.

    search: Optional[str] = None # Return list of projects matching the search criteria.

    simple: Optional[bool] = None # Return only limited fields for each project. Without authentication, this operation is a no-op; only simple fields are returned.

    sort: Optional[str] = None # Return projects sorted in asc or desc order. Default is desc.

    starred: Optional[bool] = None # Limit by projects starred by the current user.

    statistics: Optional[bool] = None # Include project statistics. Available only to users with at least the Reporter role.

    visibility: Optional[str] = None # Limit by visibility public, internal, or private.

    with_custom_attributes: Optional[bool] = None # Include custom attributes in response. (administrator only)

    with_issues_enabled: Optional[bool] = None # Limit by enabled issues feature.

    with_merge_requests_enabled: Optional[bool] = None # Limit by enabled merge requests feature.

    updated_before: Optional[datetime] = None # Limit results to projects last updated before the specified time. Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ). Introduced in GitLab 15.10.

    updated_after: Optional[datetime] = None # Limit results to projects last updated after the specified time. Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ). Introduced in GitLab 15.10.


@action_store.kubiya_action()
def list_projects_starred_by_a_user(input: UsersUseridStarredprojects):
    return get_wrapper(endpoint=f"/users/{input.user_id}/starred_projects", args=input.dict(exclude_none=True))


class ProjectsIdSingleProjectSingle(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

    license: Optional[bool] = None # Include project license data.

    statistics: Optional[bool] = None # Include project statistics. Available only to users with at least the Reporter role.

    with_custom_attributes: Optional[bool] = None # Include custom attributes in response. (administrators only)


@action_store.kubiya_action()
def get_single_project(input: ProjectsIdSingleProjectSingle):
    return get_wrapper(endpoint=f"/projects/{input.id}", args=input.dict(exclude_none=True))


class ProjectsIdUsers(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

    search: Optional[str] = None # Search for specific users.

    skip_users: Optional[int] = None # Filter out users with the specified IDs.


@action_store.kubiya_action()
def get_project_users(input: ProjectsIdUsers):
    return get_wrapper(endpoint=f"/projects/{input.id}/users", args=input.dict(exclude_none=True))


class ProjectsIdGroups(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

    search: Optional[str] = None # Search for specific groups.

    shared_min_access_level: Optional[int] = None # Limit to shared groups with at least this role (access_level).

    shared_visible_only: Optional[bool] = None # Limit to shared groups user has access to.

    skip_groups: Optional[int] = None # Skip the group IDs passed.

    with_shared: Optional[bool] = None # Include projects shared with this group. Default is false.


@action_store.kubiya_action()
def list_a_projects_groups(input: ProjectsIdGroups):
    return get_wrapper(endpoint=f"/projects/{input.id}/groups", args=input.dict(exclude_none=True))


class ProjectsIdSharelocations(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.
    search: Optional[str] = None # Search for specific groups.


@action_store.kubiya_action()
def list_a_projects_shareable_groups(input: ProjectsIdSharelocations):
    return get_wrapper(endpoint=f"/projects/{input.id}/share_locations", args=input.dict(exclude_none=True))


class CreateProjectRequest(BaseModel):
    name: Optional[str] = Field(None, description="The name of the new project. Equals path if not provided.")
    path: Optional[str] = Field(None, description="Repository name for new project. Generated based on name if not provided (generated as lowercase with dashes). Starting with GitLab 14.9, path must not start or end with a special character and must not contain consecutive special characters.")
    allow_merge_on_skipped_pipeline: Optional[bool] = Field(None, description="Set whether or not merge requests can be merged with skipped jobs.")
    only_allow_merge_if_all_status_checks_passed: Optional[bool] = Field(None, description="Indicates that merges of merge requests should be blocked unless all status checks have passed. Defaults to false. Introduced in GitLab 15.5 with feature flag only_allow_merge_if_all_status_checks_passed disabled by default.")
    analytics_access_level: Optional[str] = Field(None, description="One of disabled, private or enabled.")
    approvals_before_merge: Optional[int] = Field(None, description="How many approvers should approve merge requests by default. To configure approval rules, see Merge request approvals API. Deprecated in GitLab 16.0.")
    auto_cancel_pending_pipelines: Optional[str] = Field(None, description="Auto-cancel pending pipelines. This action toggles between an enabled state and a disabled state; it is not a boolean.")
    auto_devops_deploy_strategy: Optional[str] = Field(None, description="Auto Deploy strategy (continuous, manual or timed_incremental).")
    auto_devops_enabled: Optional[bool] = Field(None, description="Enable Auto DevOps for this project.")
    autoclose_referenced_issues: Optional[bool] = Field(None, description="Set whether auto-closing referenced issues on default branch.")
    avatar: Optional[Union[str, Any]] = Field(None, description="Image file for avatar of the project.")
    build_git_strategy: Optional[str] = Field(None, description="The Git strategy. Defaults to fetch.")    
    build_timeout: Optional[int] = Field(None, description="The maximum amount of time, in seconds, that a job can run.")
    builds_access_level: Optional[str] = Field(None, description="One of disabled, private, or enabled.")
    ci_config_path: Optional[str] = Field(None, description="The path to CI configuration file.")
    container_expiration_policy_attributes: Optional[dict] = Field(None, description="Update the image cleanup policy for this project.")
    container_registry_access_level: Optional[str] = Field(None, description="Set visibility of container registry, for this project, to one of disabled, private or enabled.")
    container_registry_enabled: Optional[bool] = Field(None, description="(Deprecated) Enable container registry for this project. Use container_registry_access_level instead.")
    default_branch: Optional[str] = Field(None, description="The default branch name. Requires initialize_with_readme to be true.")
    description: Optional[str] = Field(None, description="Short project description.")
    emails_disabled: Optional[bool] = Field(None, description="Disable email notifications.")
    external_authorization_classification_label: Optional[str] = Field(None, description="The classification label for the project.")
    forking_access_level: Optional[str] = Field(None, description="One of disabled, private, or enabled.")
    group_with_project_templates_id: Optional[int] = Field(None, description="For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true.")
    import_url: Optional[str] = Field(None, description="URL to import repository from. When the URL value isn’t empty, you must not set initialize_with_readme to true. Doing so might result in the following error: not a git repository.")
    initialize_with_readme: Optional[bool] = Field(None, description="Whether to create a Git repository with just a README.md file. Default is false.")
    issues_access_level: Optional[str] = Field(None, description="One of disabled, private, or enabled.")
    issues_enabled: Optional[bool] = Field(None, description="(Deprecated) Enable issues for this project. Use issues_access_level instead.")
    jobs_enabled: Optional[bool] = Field(None, description="(Deprecated) Enable jobs for this project. Use builds_access_level instead.")
    lfs_enabled: Optional[bool] = Field(None, description="Enable LFS.")
    merge_method: Optional[str] = Field(None, description="Set the merge method used.")
    merge_pipelines_enabled: Optional[bool] = Field(None, description="Enable or disable merge pipelines.")
    merge_requests_access_level: Optional[str] = Field(None, description="One of disabled, private, or enabled.")
    merge_requests_enabled: Optional[bool] = Field(None, description="(Deprecated) Enable merge requests for this project. Use merge_requests_access_level instead.")
    merge_trains_enabled: Optional[bool] = Field(None, description="Enable or disable merge trains.")
    mirror_trigger_builds: Optional[bool] = Field(None, description="Pull mirroring triggers builds.")
    mirror: Optional[bool] = Field(None, description="Enables pull mirroring in a project.")
    namespace_id: Optional[int] = Field(None, description="Namespace for the new project (defaults to the current user’s namespace).")
    only_allow_merge_if_all_discussions_are_resolved: Optional[bool] = Field(None, description="Set whether merge requests can only be merged when all the discussions are resolved.")
    only_allow_merge_if_pipeline_succeeds: Optional[bool] = Field(None, description="Set whether merge requests can only be merged with successful pipelines.")
    packages_enabled: Optional[bool] = Field(None, description="Enable or disable packages repository feature.")
    pages_access_level: Optional[str] = Field(None, description="One of disabled, private, enabled, or public.")
    printing_merge_request_link_enabled: Optional[bool] = Field(None, description="Show link to create/view merge request when pushing from the command line.")
    public_builds: Optional[bool] = Field(None, description="If true, jobs can be viewed by non-project members.")
    releases_access_level: Optional[str] = Field(None, description="One of disabled, private, or enabled.")
    environments_access_level: Optional[str] = Field(None, description="One of disabled, private, or enabled.")
    feature_flags_access_level: Optional[str] = Field(None, description="One of disabled, private, or enabled.")
    infrastructure_access_level: Optional[str] = Field(None, description="One of disabled, private, or enabled.")
    monitor_access_level: Optional[str] = Field(None, description="One of disabled, private, or enabled.")
    remove_source_branch_after_merge: Optional[bool] = Field(None, description="Enable Delete source branch option by default for all new merge requests.")
    repository_access_level: Optional[str] = Field(None, description="One of disabled, private, or enabled.")
    repository_storage: Optional[str] = Field(None, description="Which storage shard the repository is on. (administrator only)")
    request_access_enabled: Optional[bool] = Field(None, description="Allow users to request member access.")
    requirements_access_level: Optional[str] = Field(None, description="One of disabled, private or enabled")
    resolve_outdated_diff_discussions: Optional[bool] = Field(None, description="Automatically resolve merge request diffs discussions on lines changed with a push.")
    security_and_compliance_access_level: Optional[str] = Field(None, description="(GitLab 14.9 and later) Security and compliance access level. One of disabled, private, or enabled.")
    shared_runners_enabled: Optional[bool] = Field(None, description="Enable shared runners for this project.")
    group_runners_enabled: Optional[bool] = Field(None, description="Enable group runners for this project.")
    snippets_access_level: Optional[str] = Field(None, description="One of disabled, private, or enabled.")
    snippets_enabled: Optional[bool] = Field(None, description="(Deprecated) Enable snippets for this project. Use snippets_access_level instead.")
    squash_option: Optional[str] = Field(None, description="One of never, always, default_on, or default_off.")
    tag_list: Optional[list] = Field(None, description="(Deprecated in GitLab 14.0) The list of tags for a project; put array of tags, that should be finally assigned to a project. Use topics instead.")
    template_name: Optional[str] = Field(None, description="When used without use_custom_template, name of a built-in project template.")
    template_project_id: Optional[int] = Field(None, description="When used with use_custom_template, project ID of a custom project template.")
    topics: Optional[list] = Field(None, description="The list of topics for a project; put array of topics, that should be finally assigned to a project. (Introduced in GitLab 14.0.)")
    use_custom_template: Optional[bool] = Field(None, description="Use either custom instance or group (with group_with_project_templates_id) project template.")
    visibility: Optional[str] = Field(None, description="See project visibility level.")
    wiki_access_level: Optional[str] = Field(None, description="One of disabled, private, or enabled.")
    wiki_enabled: Optional[bool] = Field(None, description="(Deprecated) Enable wiki for this project. Use wiki_access_level instead.")

@action_store.kubiya_action()
def create_project(input: CreateProjectRequest):
    return post_wrapper(endpoint="/projects", args=input.dict(exclude_none=True))


class ProjectsUserUserid(BaseModel):

    user_id: int # The user ID of the project owner.

    name: str # The name of the new project.

    allow_merge_on_skipped_pipeline: Optional[bool] = None # Set whether or not merge requests can be merged with skipped jobs.

    only_allow_merge_if_all_status_checks_passed: Optional[bool] = None # Indicates that merges of merge requests should be blocked unless all status checks have passed. Defaults to false. Introduced in GitLab 15.5 with feature flag only_allow_merge_if_all_status_checks_passed disabled by default.

    analytics_access_level: Optional[str] = None # One of disabled, private or enabled

    approvals_before_merge: Optional[int] = None # How many approvers should approve merge requests by default. Deprecated in GitLab 16.0. To configure approval rules, see Merge request approvals API.

    auto_cancel_pending_pipelines: Optional[str] = None # Auto-cancel pending pipelines. This action toggles between an enabled state and a disabled state; it is not a boolean.

    auto_devops_deploy_strategy: Optional[str] = None # Auto Deploy strategy (continuous, manual or timed_incremental).

    auto_devops_enabled: Optional[bool] = None # Enable Auto DevOps for this project.

    autoclose_referenced_issues: Optional[bool] = None # Set whether auto-closing referenced issues on default branch.

    avatar: Optional[Any] = None # Image file for avatar of the project.

    build_git_strategy: Optional[str] = None # The Git strategy. Defaults to fetch.

    build_timeout: Optional[int] = None # The maximum amount of time, in seconds, that a job can run.

    builds_access_level: Optional[str] = None # One of disabled, private, or enabled.

    ci_config_path: Optional[str] = None # The path to CI configuration file.

    container_registry_access_level: Optional[str] = None # Set visibility of container registry, for this project, to one of disabled, private or enabled.

    container_registry_enabled: Optional[bool] = None # (Deprecated) Enable container registry for this project. Use container_registry_access_level instead.

    default_branch: Optional[str] = None # The default branch name. Requires initialize_with_readme to be true.

    description: Optional[str] = None # Short project description.

    emails_disabled: Optional[bool] = None # Disable email notifications.

    enforce_auth_checks_on_uploads: Optional[bool] = None # Enforce auth checks on uploads.

    external_authorization_classification_label: Optional[str] = None # The classification label for the project.

    forking_access_level: Optional[str] = None # One of disabled, private, or enabled.

    group_with_project_templates_id: Optional[int] = None # For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true.

    import_url: Optional[str] = None # URL to import repository from.

    initialize_with_readme: Optional[bool] = None # false by default.

    issues_access_level: Optional[str] = None # One of disabled, private, or enabled.

    issues_enabled: Optional[bool] = None # (Deprecated) Enable issues for this project. Use issues_access_level instead.

    jobs_enabled: Optional[bool] = None # (Deprecated) Enable jobs for this project. Use builds_access_level instead.

    lfs_enabled: Optional[bool] = None # Enable LFS.

    merge_commit_template: Optional[str] = None # Template used to create merge commit message in merge requests. (Introduced in GitLab 14.5.)

    merge_method: Optional[str] = None # Set the merge method used.

    merge_requests_access_level: Optional[str] = None # One of disabled, private, or enabled.

    merge_requests_enabled: Optional[bool] = None # (Deprecated) Enable merge requests for this project. Use merge_requests_access_level instead.

    mirror_trigger_builds: Optional[bool] = None # Pull mirroring triggers builds.

    mirror: Optional[bool] = None # Enables pull mirroring in a project.

    namespace_id: Optional[int] = None # Namespace for the new project (defaults to the current user‚Äôs namespace).

    only_allow_merge_if_all_discussions_are_resolved: Optional[bool] = None # Set whether merge requests can only be merged when all the discussions are resolved.

    only_allow_merge_if_pipeline_succeeds: Optional[bool] = None # Set whether merge requests can only be merged with successful jobs.

    packages_enabled: Optional[bool] = None # Enable or disable packages repository feature.

    pages_access_level: Optional[str] = None # One of disabled, private, enabled, or public.

    path: Optional[str] = None # Custom repository name for new project. By default generated based on name.

    printing_merge_request_link_enabled: Optional[bool] = None # Show link to create/view merge request when pushing from the command line.

    public_builds: Optional[bool] = None # If true, jobs can be viewed by non-project-members.

    releases_access_level: Optional[str] = None # One of disabled, private, or enabled.

    environments_access_level: Optional[str] = None # One of disabled, private, or enabled.

    feature_flags_access_level: Optional[str] = None # One of disabled, private, or enabled.

    infrastructure_access_level: Optional[str] = None # One of disabled, private, or enabled.

    monitor_access_level: Optional[str] = None # One of disabled, private, or enabled.

    remove_source_branch_after_merge: Optional[bool] = None # Enable Delete source branch option by default for all new merge requests.

    repository_access_level: Optional[str] = None # One of disabled, private, or enabled.

    repository_storage: Optional[str] = None # Which storage shard the repository is on. (administrators only)

    request_access_enabled: Optional[bool] = None # Allow users to request member access.

    requirements_access_level: Optional[str] = None # One of disabled, private, enabled or public

    resolve_outdated_diff_discussions: Optional[bool] = None # Automatically resolve merge request diffs discussions on lines changed with a push.

    security_and_compliance_access_level: Optional[str] = None # (GitLab 14.9 and later) Security and compliance access level. One of disabled, private, or enabled.

    shared_runners_enabled: Optional[bool] = None # Enable shared runners for this project.

    group_runners_enabled: Optional[bool] = None # Enable group runners for this project.

    snippets_access_level: Optional[str] = None # One of disabled, private, or enabled.

    snippets_enabled: Optional[bool] = None # (Deprecated) Enable snippets for this project. Use snippets_access_level instead.

    issue_branch_template: Optional[str] = None # Template used to suggest names for branches created from issues. (Introduced in GitLab 15.6.)

    squash_commit_template: Optional[str] = None # Template used to create squash commit message in merge requests. (Introduced in GitLab 14.6.)

    squash_option: Optional[str] = None # One of never, always, default_on, or default_off.

    suggestion_commit_message: Optional[str] = None # The commit message used to apply merge request suggestions.

    tag_list: Optional[List[str]] = None # (Deprecated in GitLab 14.0) The list of tags for a project; put array of tags, that should be finally assigned to a project. Use topics instead.

    template_name: Optional[str] = None # When used without use_custom_template, name of a built-in project template. When used with use_custom_template, name of a custom project template.

    topics: Optional[List[str]] = None # The list of topics for the project. (Introduced in GitLab 14.0.)

    use_custom_template: Optional[bool] = None # Use either custom instance or group (with group_with_project_templates_id) project template.

    visibility: Optional[str] = None # See project visibility level.

    wiki_access_level: Optional[str] = None # One of disabled, private, or enabled.

    wiki_enabled: Optional[bool] = None # (Deprecated) Enable wiki for this project. Use wiki_access_level instead.


@action_store.kubiya_action()
def create_project_for_user(input: ProjectsUserUserid):
    return post_wrapper(endpoint=f"/projects/user/{input.user_id}", args=input.dict(exclude_none=True))


class ProjectsIdEdit(BaseModel):
    class AccessLevel(str, Enum):
        disabled = "disabled"
        private = "private"
        enabled = "enabled"

    class AutoDevOpsDeployStrategy(str, Enum):
        continuous = "continuous"
        manual = "manual"
        timed_incremental = "timed_incremental"

    class AutoCancelPendingPipelines(str, Enum):
        enabled = "enabled"
        disabled = "disabled"

    class GitStrategy(str, Enum):
        fetch = "fetch"

    class ContainerExpirationPolicyAttributes(BaseModel):
        cadence: Optional[str] = None
        keep_n: Optional[int] = None
        older_than: Optional[str] = None
        name_regex: Optional[str] = None
        name_regex_delete: Optional[str] = None
        name_regex_keep: Optional[str] = None
        enabled: Optional[bool] = None

    class SquashOption(str, Enum):
        never = "never"
        always = "always"
        default_on = "default_on"
        default_off = "default_off"

    id: Union[int, str] 
    allow_merge_on_skipped_pipeline: Optional[bool] = None
    allow_pipeline_trigger_approve_deployment: Optional[bool] = None
    only_allow_merge_if_all_status_checks_passed: Optional[bool] = None
    analytics_access_level: Optional[AccessLevel] = None
    approvals_before_merge: Optional[int] = None
    auto_cancel_pending_pipelines: Optional[AutoCancelPendingPipelines] = None
    auto_devops_deploy_strategy: Optional[AutoDevOpsDeployStrategy] = None
    auto_devops_enabled: Optional[bool] = None
    autoclose_referenced_issues: Optional[bool] = None
    avatar: Optional[str] = None
    build_git_strategy: Optional[GitStrategy] = None
    build_timeout: Optional[int] = None
    builds_access_level: Optional[AccessLevel] = None
    ci_config_path: Optional[str] = None
    ci_default_git_depth: Optional[int] = None
    ci_forward_deployment_enabled: Optional[bool] = None
    ci_allow_fork_pipelines_to_run_in_parent_project: Optional[bool] = None
    ci_separated_caches: Optional[bool] = None
    container_expiration_policy_attributes: Optional[ContainerExpirationPolicyAttributes] = None
    container_registry_access_level: Optional[AccessLevel] = None
    container_registry_enabled: Optional[bool] = None
    default_branch: Optional[str] = None
    description: Optional[str] = None
    emails_disabled: Optional[bool] = None
    enforce_auth_checks_on_uploads: Optional[bool] = None
    external_authorization_classification_label: Optional[str] = None
    forking_access_level: Optional[AccessLevel] = None
    import_url: Optional[str] = None
    issues_access_level: Optional[AccessLevel] = None
    issues_enabled: Optional[bool] = None
    issues_template: Optional[str] = None
    jobs_enabled: Optional[bool] = None
    keep_latest_artifact: Optional[bool] = None
    lfs_enabled: Optional[bool] = None
    merge_commit_template: Optional[str] = None
    merge_method: Optional[str] = None
    merge_pipelines_enabled: Optional[bool] = None
    merge_requests_access_level: Optional[AccessLevel] = None
    merge_requests_enabled: Optional[bool] = None
    merge_requests_template: Optional[str] = None
    merge_trains_enabled: Optional[bool] = None
    mirror_overwrites_diverged_branches: Optional[bool] = None
    mirror_trigger_builds: Optional[bool] = None
    mirror_user_id: Optional[int] = None
    mirror: Optional[bool] = None
    mr_default_target_self: Optional[bool] = None
    name: Optional[str] = None
    only_allow_merge_if_all_discussions_are_resolved: Optional[bool] = None
    only_allow_merge_if_pipeline_succeeds: Optional[bool] = None
    only_mirror_protected_branches: Optional[bool] = None
    packages_enabled: Optional[bool] = None
    pages_access_level: Optional[AccessLevel] = None
    path: Optional[str] = None
    printing_merge_request_link_enabled: Optional[bool] = None
    public_builds: Optional[bool] = None
    releases_access_level: Optional[AccessLevel] = None
    environments_access_level: Optional[AccessLevel] = None
    feature_flags_access_level: Optional[AccessLevel] = None
    infrastructure_access_level: Optional[AccessLevel] = None
    monitor_access_level: Optional[AccessLevel] = None
    remove_source_branch_after_merge: Optional[bool] = None
    repository_access_level: Optional[AccessLevel] = None
    repository_storage: Optional[str] = None
    request_access_enabled: Optional[bool] = None
    requirements_access_level: Optional[AccessLevel] = None
    resolve_outdated_diff_discussions: Optional[bool] = None
    restrict_user_defined_variables: Optional[bool] = None
    security_and_compliance_access_level: Optional[AccessLevel] = None
    service_desk_enabled: Optional[bool] = None
    shared_runners_enabled: Optional[bool] = None
    group_runners_enabled: Optional[bool] = None
    snippets_access_level: Optional[AccessLevel] = None
    snippets_enabled: Optional[bool] = None
    issue_branch_template: Optional[str] = None
    squash_commit_template: Optional[str] = None
    squash_option: Optional[SquashOption] = None
    suggestion_commit_message: Optional[str] = None
    tag_list: Optional[List[str]] = None
    topics: Optional[List[str]] = None
    visibility: Optional[str] = None
    wiki_access_level: Optional[AccessLevel] = None
    wiki_enabled: Optional[bool] = None


@action_store.kubiya_action()
def edit_project(input: ProjectsIdEdit):
    return put_wrapper(endpoint=f"/projects/{input.id}", args=input.dict(exclude_none=True))


class ProjectsIdFork(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

    description: Optional[str] = None # The description assigned to the resultant project after forking.

    mr_default_target_self: Optional[bool] = None # For forked projects, target merge requests to this project. If false, the target is the upstream project.

    name: Optional[str] = None # The name assigned to the resultant project after forking.

    namespace_id: Optional[int] = None # The ID of the namespace that the project is forked to.

    namespace_path: Optional[str] = None # The path of the namespace that the project is forked to.

    namespace: Optional[int] = None # (Deprecated) The ID or path of the namespace that the project is forked to.

    path: Optional[str] = None # The path assigned to the resultant project after forking.

    visibility: Optional[str] = None # The visibility level assigned to the resultant project after forking.


@action_store.kubiya_action()
def fork_project(input: ProjectsIdFork):
    return post_wrapper(endpoint=f"/projects/{input.id}/fork", args=input.dict(exclude_none=True))


class ProjectsIdForks(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

    archived: Optional[bool] = None # Limit by archived status.

    membership: Optional[bool] = None # Limit by projects that the current user is a member of.

    min_access_level: Optional[int] = None # Limit by current user minimal role (access_level).

    order_by: Optional[str] = None # Return projects ordered by id, name, path, created_at, updated_at, or last_activity_at fields. Default is created_at.

    owned: Optional[bool] = None # Limit by projects explicitly owned by the current user.

    search: Optional[str] = None # Return list of projects matching the search criteria.

    simple: Optional[bool] = None # Return only limited fields for each project. Without authentication, this operation is a no-op; only simple fields are returned.

    sort: Optional[str] = None # Return projects sorted in asc or desc order. Default is desc.

    starred: Optional[bool] = None # Limit by projects starred by the current user.

    statistics: Optional[bool] = None # Include project statistics. Available only to users with at least the Reporter role.

    visibility: Optional[str] = None # Limit by visibility public, internal, or private.

    with_custom_attributes: Optional[bool] = None # Include custom attributes in response. (administrators only)

    with_issues_enabled: Optional[bool] = None # Limit by enabled issues feature.

    with_merge_requests_enabled: Optional[bool] = None # Limit by enabled merge requests feature.

    updated_before: Optional[datetime] = None # Limit results to projects last updated before the specified time. Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ). Introduced in GitLab 15.10.

    updated_after: Optional[datetime] = None # Limit results to projects last updated after the specified time. Format: ISO 8601 (YYYY-MM-DDTHH:MM:SSZ). Introduced in GitLab 15.10.


@action_store.kubiya_action()
def list_forks_of_a_project(input: ProjectsIdForks):
    return get_wrapper(endpoint=f"/projects/{input.id}/forks", args=input.dict(exclude_none=True))


class ProjectsIdStar(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.


@action_store.kubiya_action()
def star_a_project(input: ProjectsIdStar):
    return post_wrapper(endpoint=f"/projects/{input.id}/star", args=input.dict(exclude_none=True))


class ProjectsIdUnstar(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.


@action_store.kubiya_action()
def unstar_a_project(input: ProjectsIdUnstar):
    return post_wrapper(endpoint=f"/projects/{input.id}/unstar", args=input.dict(exclude_none=True))


class ProjectsIdStarrers(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

    search: Optional[str] = None # Search for specific users.


@action_store.kubiya_action()
def list_starrers_of_a_project(input: ProjectsIdStarrers):
    return get_wrapper(endpoint=f"/projects/{input.id}/starrers", args=input.dict(exclude_none=True))


class ProjectsIdLanguages(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

@action_store.kubiya_action()
def languages(input: ProjectsIdLanguages):
    return get_wrapper(endpoint=f"/projects/{input.id}/languages", args=input.dict(exclude_none=True))


class ProjectsIdArchive(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.


@action_store.kubiya_action()
def archive_a_project(input: ProjectsIdArchive):
    return post_wrapper(endpoint=f"/projects/{input.id}/archive", args=input.dict(exclude_none=True))


class ProjectsIdUnarchive(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.


@action_store.kubiya_action()
def unarchive_a_project(input: ProjectsIdUnarchive):
    return post_wrapper(endpoint=f"/projects/{input.id}/unarchive", args=input.dict(exclude_none=True))


class ProjectsIdDelete(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

    permanently_remove: Optional[str] = None # Immediately deletes a project if it is marked for deletion. Introduced in GitLab 15.11

    full_path: Optional[str] = None # Full path of project to use with permanently_remove. Introduced in GitLab 15.11. To find the project path, use path_with_namespace from get single project


@action_store.kubiya_action()
def delete_project(input: ProjectsIdDelete):
    return delete_wrapper(endpoint=f"/projects/{input.id}", args=input.dict(exclude_none=True))


class ProjectsIdRestore(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.


@action_store.kubiya_action()
def restore_project_marked_for_deletion_(input: ProjectsIdRestore):
    return post_wrapper(endpoint=f"/projects/{input.id}/restore", args=input.dict(exclude_none=True))


class ProjectsIdUploads(BaseModel):

    file: str # The file to be uploaded.

    id: Union[int, str] # The ID or URL-encoded path of the project.


@action_store.kubiya_action()
def upload_a_file(input: ProjectsIdUploads):
    return post_wrapper(endpoint=f"/projects/{input.id}/uploads", args=input.dict(exclude_none=True))


class ProjectsIdAvatar(BaseModel):

    avatar: str # The file to be uploaded.

    id: Union[int, str] # The ID or URL-encoded path of the project.

@action_store.kubiya_action()
def upload_a_project_avatar(input: ProjectsIdAvatar):
    return put_wrapper(endpoint=f"/projects/{input.id}", args=input.dict(exclude_none=True))

@action_store.kubiya_action()
def remove_a_project_avatar(input: ProjectsIdAvatar):
    return put_wrapper(endpoint=f"/projects/{input.id}", args={'avatar':""})


class ProjectsIdShare(BaseModel):

    group_access: int # The role (access_level) to grant the group.

    group_id: int # The ID of the group to share with.

    id: Union[int, str] # The ID or URL-encoded path of the project.

    expires_at: Optional[str] = None # Share expiration date in ISO 8601 format: 2016-09-26


@action_store.kubiya_action()
def share_project_with_group(input: ProjectsIdShare):
    return post_wrapper(endpoint=f"/projects/{input.id}/share", args=input.dict(exclude_none=True))


class ProjectsIdShareGroupid(BaseModel):

    group_id: int # The ID of the group.

    id: Union[int, str] # The ID or URL-encoded path of the project.


@action_store.kubiya_action()
def delete_a_shared_project_link_within_a_group(input: ProjectsIdShareGroupid):
    return delete_wrapper(endpoint=f"/projects/{input.id}/share/{input.group_id}", args=input.dict(exclude_none=True))


class ProjectsIdImportprojectmembersProjectid(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the target project to receive the members.

    project_id: int # The ID or URL-encoded path of the source project to import the members from.


@action_store.kubiya_action()
def import_project_members(input: ProjectsIdImportprojectmembersProjectid):
    return post_wrapper(endpoint=f"/projects/{input.id}/import_project_members/{input.project_id}", args=input.dict(exclude_none=True))

class ProjectsIdHooksList(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

@action_store.kubiya_action()
def list_project_hooks(input: ProjectsIdHooksList):
    return get_wrapper(endpoint=f"/projects/{input.id}/hooks", args=input.dict(exclude_none=True))


class ProjectsIdGetProjectHook(BaseModel):

    hook_id: int # The ID of a project hook.

    id: Union[int, str] # The ID or URL-encoded path of the project.


@action_store.kubiya_action()
def get_project_hook(input: ProjectsIdGetProjectHook):
    return get_wrapper(endpoint=f"/projects/{input.id}/hooks/{input.hook_id}", args=input.dict(exclude_none=True))


class ProjectsIdHooks(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

    url: str # The hook URL.

    confidential_issues_events: Optional[bool] = None # Trigger hook on confidential issues events.

    confidential_note_events: Optional[bool] = None # Trigger hook on confidential note events.

    deployment_events: Optional[bool] = None # Trigger hook on deployment events.

    enable_ssl_verification: Optional[bool] = None # Do SSL verification when triggering the hook.

    issues_events: Optional[bool] = None # Trigger hook on issues events.

    job_events: Optional[bool] = None # Trigger hook on job events.

    merge_requests_events: Optional[bool] = None # Trigger hook on merge requests events.

    note_events: Optional[bool] = None # Trigger hook on note events.

    pipeline_events: Optional[bool] = None # Trigger hook on pipeline events.

    push_events_branch_filter: Optional[str] = None # Trigger hook on push events for matching branches only.

    push_events: Optional[bool] = None # Trigger hook on push events.

    releases_events: Optional[bool] = None # Trigger hook on release events.

    tag_push_events: Optional[bool] = None # Trigger hook on tag push events.

    token: Optional[str] = None # Secret token to validate received payloads; the token isn‚Äôt returned in the response.

    wiki_page_events: Optional[bool] = None # Trigger hook on wiki events.


@action_store.kubiya_action()
def add_project_hook(input: ProjectsIdHooks):
    return post_wrapper(endpoint=f"/projects/{input.id}/hooks", args=input.dict(exclude_none=True))


class ProjectsIdEditProjectHook(BaseModel):

    hook_id: int # The ID of the project hook.

    id: Union[int, str] # The ID or URL-encoded path of the project.

    url: str # The hook URL.

    confidential_issues_events: Optional[bool] = None # Trigger hook on confidential issues events.

    confidential_note_events: Optional[bool] = None # Trigger hook on confidential note events.

    deployment_events: Optional[bool] = None # Trigger hook on deployment events.

    enable_ssl_verification: Optional[bool] = None # Do SSL verification when triggering the hook.

    issues_events: Optional[bool] = None # Trigger hook on issues events.

    job_events: Optional[bool] = None # Trigger hook on job events.

    merge_requests_events: Optional[bool] = None # Trigger hook on merge requests events.

    note_events: Optional[bool] = None # Trigger hook on note events.

    pipeline_events: Optional[bool] = None # Trigger hook on pipeline events.

    push_events_branch_filter: Optional[str] = None # Trigger hook on push events for matching branches only.

    push_events: Optional[bool] = None # Trigger hook on push events.

    releases_events: Optional[bool] = None # Trigger hook on release events.

    tag_push_events: Optional[bool] = None # Trigger hook on tag push events.

    token: Optional[str] = None # Secret token to validate received payloads. Not returned in the response. When you change the webhook URL, the secret token is reset and not retained.

    wiki_page_events: Optional[bool] = None # Trigger hook on wiki page events.


@action_store.kubiya_action()
def edit_project_hook(input: ProjectsIdEditProjectHook):
    return put_wrapper(endpoint=f"/projects/{input.id}/hooks/{input.hook_id}", args=input.dict(exclude_none=True))


class ProjectsIdDeleteProjectHook(BaseModel):

    hook_id: int # The ID of the project hook.

    id: Union[int, str] # The ID or URL-encoded path of the project.


@action_store.kubiya_action()
def delete_project_hook(input: ProjectsIdDeleteProjectHook):
    return delete_wrapper(endpoint=f"/projects/{input.id}/hooks/{input.hook_id}", args=input.dict(exclude_none=True))


class CreatedForkedRelationship(BaseModel):

    forked_from_id: Union[int, str] # The ID of the project that was forked from.

    id: Union[int, str] # The ID or URL-encoded path of the project.


@action_store.kubiya_action()
def create_a_forked_from_to_relation_between_existing_projects(input: CreatedForkedRelationship):
    return post_wrapper(endpoint=f"/projects/{input.id}/fork/{input.forked_from_id}", args=input.dict(exclude_none=True))


class DeleteExistingForkedRelationship(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.


@action_store.kubiya_action()
def delete_an_existing_forked_from_relationship(input: DeleteExistingForkedRelationship):
    return delete_wrapper(endpoint=f"/projects/{input.id}/fork", args=input.dict(exclude_none=True))


class ProjectsByNameRequest(BaseModel):

    search: str # A string contained in the project name.

    order_by: Optional[str] = None # Return requests ordered by id, name, created_at or last_activity_at fields.

    sort: Optional[str] = None # Return requests sorted in asc or desc order.


@action_store.kubiya_action()
def search_for_projects_by_name(input: ProjectsByNameRequest):
    return get_wrapper(endpoint=f"/projects", args=input.dict(exclude_none=True))


class ProjectsIdHousekeeping(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

    task: Optional[str] = None # prune to trigger manual prune of unreachable objects or eager to trigger eager housekeeping.


@action_store.kubiya_action()
def start_the_housekeeping_task_for_a_project(input: ProjectsIdHousekeeping):
    return post_wrapper(endpoint=f"/projects/{input.id}/housekeeping", args=input.dict(exclude_none=True))


class ProjectsIdPushrule(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project


@action_store.kubiya_action()
def push_rules_(input: ProjectsIdPushrule):
    return get_wrapper(endpoint=f"/projects/{input.id}/push_rule", args=input.dict(exclude_none=True))


class ProjectsIdPushruleAdd(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

    author_email_regex: Optional[str] = None # All commit author emails must match this, for example @my-company.com$.

    branch_name_regex: Optional[str] = None # All branch names must match this, for example (feature|hotfix)\/*.

    commit_committer_check: Optional[bool] = None # Users can only push commits to this repository if the committer email is one of their own verified emails.

    commit_message_negative_regex: Optional[str] = None # No commit message is allowed to match this, for example ssh\:\/\/.

    commit_message_regex: Optional[str] = None # All commit messages must match this, for example Fixed \d+\..*.

    deny_delete_tag: Optional[bool] = None # Deny deleting a tag.

    file_name_regex: Optional[str] = None # All committed filenames must not match this, for example (jar|exe)$.

    max_file_size: Optional[int] = None # Maximum file size (MB).

    member_check: Optional[bool] = None # Restrict commits by author (email) to existing GitLab users.

    prevent_secrets: Optional[bool] = None # GitLab rejects any files that are likely to contain secrets.

    reject_unsigned_commits: Optional[bool] = None # Reject commit when it‚Äôs not signed through GPG.


@action_store.kubiya_action()
def push_rules_(input: ProjectsIdPushruleAdd):
    return post_wrapper(endpoint=f"/projects/{input.id}/push_rule", args=input.dict(exclude_none=True))


class ProjectsIdPushruleEdit(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

    author_email_regex: Optional[str] = None # All commit author emails must match this, for example @my-company.com$.

    branch_name_regex: Optional[str] = None # All branch names must match this, for example (feature|hotfix)\/*.

    commit_committer_check: Optional[bool] = None # Users can only push commits to this repository if the committer email is one of their own verified emails.

    commit_message_negative_regex: Optional[str] = None # No commit message is allowed to match this, for example ssh\:\/\/.

    commit_message_regex: Optional[str] = None # All commit messages must match this, for example Fixed \d+\..*.

    deny_delete_tag: Optional[bool] = None # Deny deleting a tag.

    file_name_regex: Optional[str] = None # All committed filenames must not match this, for example (jar|exe)$.

    max_file_size: Optional[int] = None # Maximum file size (MB).

    member_check: Optional[bool] = None # Restrict commits by author (email) to existing GitLab users.

    prevent_secrets: Optional[bool] = None # GitLab rejects any files that are likely to contain secrets.

    reject_unsigned_commits: Optional[bool] = None # Reject commits when they are not GPG signed.


@action_store.kubiya_action()
def push_rules_(input: ProjectsIdPushruleEdit):
    return put_wrapper(endpoint=f"/projects/{input.id}/push_rule", args=input.dict(exclude_none=True))


class ProjectsIdPushruleDelete(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.


@action_store.kubiya_action()
def delete_project_push_rule(input: ProjectsIdPushruleDelete):
    return delete_wrapper(endpoint=f"/projects/{input.id}/push_rule", args=input.dict(exclude_none=True))


class ProjectsIdTransferlocations(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

    search: Optional[str] = None # The group names to search for.


@action_store.kubiya_action()
def get_groups_to_which_a_user_can_transfer_a_project(input: ProjectsIdTransferlocations):
    return get_wrapper(endpoint=f"/projects/{input.id}/transfer_locations", args=input.dict(exclude_none=True))


class ProjectsIdTransfer(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.
    namespace: int # The ID or path of the namespace to transfer to project to.


@action_store.kubiya_action()
def transfer_a_project_to_a_new_namespace(input: ProjectsIdTransfer):
    return put_wrapper(endpoint=f"/projects/{input.id}/transfer", args=input.dict(exclude_none=True))


class ProjectsIdMirrorPull(BaseModel):
    id: Union[int, str] # The ID or URL-encoded path of the project.

@action_store.kubiya_action()
def get_a_projects_pull_mirror_details_(input: ProjectsIdMirrorPull):
    return get_wrapper(endpoint=f"/projects/{input.id}/mirror/pull", args=input.dict(exclude_none=True))


class ProjectsIdMirrorPullStart(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

@action_store.kubiya_action()
def start_the_pull_mirroring_process_for_a_project_(input: ProjectsIdMirrorPullStart):
    return post_wrapper(endpoint=f"/projects/{input.id}/mirror/pull", args=input.dict(exclude_none=True))



# class ProjectsIdMirrorConfig(BaseModel):
#     import_url: str
#     mirror: bool
#     mirror_trigger_builds: Optional[bool]
#     only_mirror_protected_branches: Optional[bool]
#     mirror_branch_regex: Optional[str]

# @action_store.kubiya_action()
# def configure_pull_mirroring_for_a_project(input: ProjectsIdMirrorConfig):
    

class ProjectsIdSnapshot(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.
    wiki: Optional[bool] = None # Whether to download the wiki, rather than project, repository.


@action_store.kubiya_action()
def download_snapshot_of_a_git_repository(input: ProjectsIdSnapshot):
    return get_wrapper(endpoint=f"/projects/{input.id}/snapshot", args=input.dict(exclude_none=True))


class ProjectsIdStorage(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.


@action_store.kubiya_action()
def get_the_path_to_repository_storage(input: ProjectsIdStorage):
    return get_wrapper(endpoint=f"/projects/{input.id}/storage", args=input.dict(exclude_none=True))
