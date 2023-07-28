from typing import List, Any, Optional, Union, Dict, Union
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

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
    custom_attributes: Optional[Dict[str, str]] = Field(None, description='A dictionary of custom attributes to filter by')
class UsersUseridProjects(BaseModel):
    user_id: str
    archived: Optional[bool] = None
    id_after: Optional[int] = None
    id_before: Optional[int] = None
    membership: Optional[bool] = None
    min_access_level: Optional[int] = None
    order_by: Optional[str] = None
    owned: Optional[bool] = None
    search: Optional[str] = None
    simple: Optional[bool] = None
    sort: Optional[str] = None
    starred: Optional[bool] = None
    statistics: Optional[bool] = None
    visibility: Optional[str] = None
    with_custom_attributes: Optional[bool] = None
    with_issues_enabled: Optional[bool] = None
    with_merge_requests_enabled: Optional[bool] = None
    with_programming_language: Optional[str] = None
    updated_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None
class UsersUseridStarredprojects(BaseModel):
    user_id: str
    archived: Optional[bool] = None
    membership: Optional[bool] = None
    min_access_level: Optional[int] = None
    order_by: Optional[str] = None
    owned: Optional[bool] = None
    search: Optional[str] = None
    simple: Optional[bool] = None
    sort: Optional[str] = None
    starred: Optional[bool] = None
    statistics: Optional[bool] = None
    visibility: Optional[str] = None
    with_custom_attributes: Optional[bool] = None
    with_issues_enabled: Optional[bool] = None
    with_merge_requests_enabled: Optional[bool] = None
    updated_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None
class ProjectsIdSingleProjectSingle(BaseModel):
    id: Union[int, str]
    license: Optional[bool] = None
    statistics: Optional[bool] = None
    with_custom_attributes: Optional[bool] = None
class ProjectsIdUsers(BaseModel):
    id: Union[int, str]
    search: Optional[str] = None
    skip_users: Optional[int] = None
class ProjectsIdGroups(BaseModel):
    id: Union[int, str]
    search: Optional[str] = None
    shared_min_access_level: Optional[int] = None
    shared_visible_only: Optional[bool] = None
    skip_groups: Optional[int] = None
    with_shared: Optional[bool] = None
    
class ProjectsIdSharelocations(BaseModel):
    id: Union[int, str]
    search: Optional[str] = None

class OrderBy(str, Enum):
    id = "id"
    name = "name"
    path = "path"
    created_at = "created_at"
    updated_at = "updated_at"
    last_activity_at = "last_activity_at"

class ListContributed(BaseModel):
    user_id: str
    order_by: Optional[OrderBy]
    simple: Optional[bool]
    sort: Optional[str]

class CreateProjectRequest(BaseModel):
    name: Optional[str] = Field(None, description='The name of the new project. Equals path if not provided.')
    path: Optional[str] = Field(None, description='Repository name for new project. Generated based on name if not provided (generated as lowercase with dashes). Starting with GitLab 14.9, path must not start or end with a special character and must not contain consecutive special characters.')
    allow_merge_on_skipped_pipeline: Optional[bool] = Field(None, description='Set whether or not merge requests can be merged with skipped jobs.')
    only_allow_merge_if_all_status_checks_passed: Optional[bool] = Field(None, description='Indicates that merges of merge requests should be blocked unless all status checks have passed. Defaults to false. Introduced in GitLab 15.5 with feature flag only_allow_merge_if_all_status_checks_passed disabled by default.')
    analytics_access_level: Optional[str] = Field(None, description='One of disabled, private or enabled.')
    approvals_before_merge: Optional[int] = Field(None, description='How many approvers should approve merge requests by default. To configure approval rules, see Merge request approvals API. Deprecated in GitLab 16.0.')
    auto_cancel_pending_pipelines: Optional[str] = Field(None, description='Auto-cancel pending pipelines. This action toggles between an enabled state and a disabled state; it is not a boolean.')
    auto_devops_deploy_strategy: Optional[str] = Field(None, description='Auto Deploy strategy (continuous, manual or timed_incremental).')
    auto_devops_enabled: Optional[bool] = Field(None, description='Enable Auto DevOps for this project.')
    autoclose_referenced_issues: Optional[bool] = Field(None, description='Set whether auto-closing referenced issues on default branch.')
    avatar: Optional[Union[str, Any]] = Field(None, description='Image file for avatar of the project.')
    build_git_strategy: Optional[str] = Field(None, description='The Git strategy. Defaults to fetch.')
    build_timeout: Optional[int] = Field(None, description='The maximum amount of time, in seconds, that a job can run.')
    builds_access_level: Optional[str] = Field(None, description='One of disabled, private, or enabled.')
    ci_config_path: Optional[str] = Field(None, description='The path to CI configuration file.')
    container_expiration_policy_attributes: Optional[dict] = Field(None, description='Update the image cleanup policy for this project.')
    container_registry_access_level: Optional[str] = Field(None, description='Set visibility of container registry, for this project, to one of disabled, private or enabled.')
    container_registry_enabled: Optional[bool] = Field(None, description='(Deprecated) Enable container registry for this project. Use container_registry_access_level instead.')
    default_branch: Optional[str] = Field(None, description='The default branch name. Requires initialize_with_readme to be true.')
    description: Optional[str] = Field(None, description='Short project description.')
    emails_disabled: Optional[bool] = Field(None, description='Disable email notifications.')
    external_authorization_classification_label: Optional[str] = Field(None, description='The classification label for the project.')
    forking_access_level: Optional[str] = Field(None, description='One of disabled, private, or enabled.')
    group_with_project_templates_id: Optional[int] = Field(None, description='For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true.')
    import_url: Optional[str] = Field(None, description='URL to import repository from. When the URL value isn’t empty, you must not set initialize_with_readme to true. Doing so might result in the following error: not a git repository.')
    initialize_with_readme: Optional[bool] = Field(None, description='Whether to create a Git repository with just a README.md file. Default is false.')
    issues_access_level: Optional[str] = Field(None, description='One of disabled, private, or enabled.')
    issues_enabled: Optional[bool] = Field(None, description='(Deprecated) Enable issues for this project. Use issues_access_level instead.')
    jobs_enabled: Optional[bool] = Field(None, description='(Deprecated) Enable jobs for this project. Use builds_access_level instead.')
    lfs_enabled: Optional[bool] = Field(None, description='Enable LFS.')
    merge_method: Optional[str] = Field(None, description='Set the merge method used.')
    merge_pipelines_enabled: Optional[bool] = Field(None, description='Enable or disable merge pipelines.')
    merge_requests_access_level: Optional[str] = Field(None, description='One of disabled, private, or enabled.')
    merge_requests_enabled: Optional[bool] = Field(None, description='(Deprecated) Enable merge requests for this project. Use merge_requests_access_level instead.')
    merge_trains_enabled: Optional[bool] = Field(None, description='Enable or disable merge trains.')
    mirror_trigger_builds: Optional[bool] = Field(None, description='Pull mirroring triggers builds.')
    mirror: Optional[bool] = Field(None, description='Enables pull mirroring in a project.')
    namespace_id: Optional[int] = Field(None, description='Namespace for the new project (defaults to the current user’s namespace).')
    only_allow_merge_if_all_discussions_are_resolved: Optional[bool] = Field(None, description='Set whether merge requests can only be merged when all the discussions are resolved.')
    only_allow_merge_if_pipeline_succeeds: Optional[bool] = Field(None, description='Set whether merge requests can only be merged with successful pipelines.')
    packages_enabled: Optional[bool] = Field(None, description='Enable or disable packages repository feature.')
    pages_access_level: Optional[str] = Field(None, description='One of disabled, private, enabled, or public.')
    printing_merge_request_link_enabled: Optional[bool] = Field(None, description='Show link to create/view merge request when pushing from the command line.')
    public_builds: Optional[bool] = Field(None, description='If true, jobs can be viewed by non-project members.')
    releases_access_level: Optional[str] = Field(None, description='One of disabled, private, or enabled.')
    environments_access_level: Optional[str] = Field(None, description='One of disabled, private, or enabled.')
    feature_flags_access_level: Optional[str] = Field(None, description='One of disabled, private, or enabled.')
    infrastructure_access_level: Optional[str] = Field(None, description='One of disabled, private, or enabled.')
    monitor_access_level: Optional[str] = Field(None, description='One of disabled, private, or enabled.')
    remove_source_branch_after_merge: Optional[bool] = Field(None, description='Enable Delete source branch option by default for all new merge requests.')
    repository_access_level: Optional[str] = Field(None, description='One of disabled, private, or enabled.')
    repository_storage: Optional[str] = Field(None, description='Which storage shard the repository is on. (administrator only)')
    request_access_enabled: Optional[bool] = Field(None, description='Allow users to request member access.')
    requirements_access_level: Optional[str] = Field(None, description='One of disabled, private or enabled')
    resolve_outdated_diff_discussions: Optional[bool] = Field(None, description='Automatically resolve merge request diffs discussions on lines changed with a push.')
    security_and_compliance_access_level: Optional[str] = Field(None, description='(GitLab 14.9 and later) Security and compliance access level. One of disabled, private, or enabled.')
    shared_runners_enabled: Optional[bool] = Field(None, description='Enable shared runners for this project.')
    group_runners_enabled: Optional[bool] = Field(None, description='Enable group runners for this project.')
    snippets_access_level: Optional[str] = Field(None, description='One of disabled, private, or enabled.')
    snippets_enabled: Optional[bool] = Field(None, description='(Deprecated) Enable snippets for this project. Use snippets_access_level instead.')
    squash_option: Optional[str] = Field(None, description='One of never, always, default_on, or default_off.')
    tag_list: Optional[list] = Field(None, description='(Deprecated in GitLab 14.0) The list of tags for a project; put array of tags, that should be finally assigned to a project. Use topics instead.')
    template_name: Optional[str] = Field(None, description='When used without use_custom_template, name of a built-in project template.')
    template_project_id: Optional[int] = Field(None, description='When used with use_custom_template, project ID of a custom project template.')
    topics: Optional[list] = Field(None, description='The list of topics for a project; put array of topics, that should be finally assigned to a project. (Introduced in GitLab 14.0.)')
    use_custom_template: Optional[bool] = Field(None, description='Use either custom instance or group (with group_with_project_templates_id) project template.')
    visibility: Optional[str] = Field(None, description='See project visibility level.')
    wiki_access_level: Optional[str] = Field(None, description='One of disabled, private, or enabled.')
    wiki_enabled: Optional[bool] = Field(None, description='(Deprecated) Enable wiki for this project. Use wiki_access_level instead.')
class ProjectsUserUserid(BaseModel):
    user_id: int
    name: str
    allow_merge_on_skipped_pipeline: Optional[bool] = None
    only_allow_merge_if_all_status_checks_passed: Optional[bool] = None
    analytics_access_level: Optional[str] = None
    approvals_before_merge: Optional[int] = None
    auto_cancel_pending_pipelines: Optional[str] = None
    auto_devops_deploy_strategy: Optional[str] = None
    auto_devops_enabled: Optional[bool] = None
    autoclose_referenced_issues: Optional[bool] = None
    avatar: Optional[Any] = None
    build_git_strategy: Optional[str] = None
    build_timeout: Optional[int] = None
    builds_access_level: Optional[str] = None
    ci_config_path: Optional[str] = None
    container_registry_access_level: Optional[str] = None
    container_registry_enabled: Optional[bool] = None
    default_branch: Optional[str] = None
    description: Optional[str] = None
    emails_disabled: Optional[bool] = None
    enforce_auth_checks_on_uploads: Optional[bool] = None
    external_authorization_classification_label: Optional[str] = None
    forking_access_level: Optional[str] = None
    group_with_project_templates_id: Optional[int] = None
    import_url: Optional[str] = None
    initialize_with_readme: Optional[bool] = None
    issues_access_level: Optional[str] = None
    issues_enabled: Optional[bool] = None
    jobs_enabled: Optional[bool] = None
    lfs_enabled: Optional[bool] = None
    merge_commit_template: Optional[str] = None
    merge_method: Optional[str] = None
    merge_requests_access_level: Optional[str] = None
    merge_requests_enabled: Optional[bool] = None
    mirror_trigger_builds: Optional[bool] = None
    mirror: Optional[bool] = None
    namespace_id: Optional[int] = None
    only_allow_merge_if_all_discussions_are_resolved: Optional[bool] = None
    only_allow_merge_if_pipeline_succeeds: Optional[bool] = None
    packages_enabled: Optional[bool] = None
    pages_access_level: Optional[str] = None
    path: Optional[str] = None
    printing_merge_request_link_enabled: Optional[bool] = None
    public_builds: Optional[bool] = None
    releases_access_level: Optional[str] = None
    environments_access_level: Optional[str] = None
    feature_flags_access_level: Optional[str] = None
    infrastructure_access_level: Optional[str] = None
    monitor_access_level: Optional[str] = None
    remove_source_branch_after_merge: Optional[bool] = None
    repository_access_level: Optional[str] = None
    repository_storage: Optional[str] = None
    request_access_enabled: Optional[bool] = None
    requirements_access_level: Optional[str] = None
    resolve_outdated_diff_discussions: Optional[bool] = None
    security_and_compliance_access_level: Optional[str] = None
    shared_runners_enabled: Optional[bool] = None
    group_runners_enabled: Optional[bool] = None
    snippets_access_level: Optional[str] = None
    snippets_enabled: Optional[bool] = None
    issue_branch_template: Optional[str] = None
    squash_commit_template: Optional[str] = None
    squash_option: Optional[str] = None
    suggestion_commit_message: Optional[str] = None
    tag_list: Optional[List[str]] = None
    template_name: Optional[str] = None
    topics: Optional[List[str]] = None
    use_custom_template: Optional[bool] = None
    visibility: Optional[str] = None
    wiki_access_level: Optional[str] = None
    wiki_enabled: Optional[bool] = None

class ProjectsIdEdit(BaseModel):

    class AccessLevel(str, Enum):
        disabled = 'disabled'
        private = 'private'
        enabled = 'enabled'

    class AutoDevOpsDeployStrategy(str, Enum):
        continuous = 'continuous'
        manual = 'manual'
        timed_incremental = 'timed_incremental'

    class AutoCancelPendingPipelines(str, Enum):
        enabled = 'enabled'
        disabled = 'disabled'

    class GitStrategy(str, Enum):
        fetch = 'fetch'

    class ContainerExpirationPolicyAttributes(BaseModel):
        cadence: Optional[str] = None
        keep_n: Optional[int] = None
        older_than: Optional[str] = None
        name_regex: Optional[str] = None
        name_regex_delete: Optional[str] = None
        name_regex_keep: Optional[str] = None
        enabled: Optional[bool] = None

    class SquashOption(str, Enum):
        never = 'never'
        always = 'always'
        default_on = 'default_on'
        default_off = 'default_off'
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
class ProjectsIdFork(BaseModel):
    id: Union[int, str]
    description: Optional[str] = None
    mr_default_target_self: Optional[bool] = None
    name: Optional[str] = None
    namespace_id: Optional[int] = None
    namespace_path: Optional[str] = None
    namespace: Optional[int] = None
    path: Optional[str] = None
    visibility: Optional[str] = None
class ProjectsIdForks(BaseModel):
    id: Union[int, str]
    archived: Optional[bool] = None
    membership: Optional[bool] = None
    min_access_level: Optional[int] = None
    order_by: Optional[str] = None
    owned: Optional[bool] = None
    search: Optional[str] = None
    simple: Optional[bool] = None
    sort: Optional[str] = None
    starred: Optional[bool] = None
    statistics: Optional[bool] = None
    visibility: Optional[str] = None
    with_custom_attributes: Optional[bool] = None
    with_issues_enabled: Optional[bool] = None
    with_merge_requests_enabled: Optional[bool] = None
    updated_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None
class ProjectsIdStar(BaseModel):
    id: Union[int, str]
class ProjectsIdUnstar(BaseModel):
    id: Union[int, str]
class ProjectsIdStarrers(BaseModel):
    id: Union[int, str]
    search: Optional[str] = None
class ProjectsIdLanguages(BaseModel):
    id: Union[int, str]
class ProjectsIdArchive(BaseModel):
    id: Union[int, str]
class ProjectsIdUnarchive(BaseModel):
    id: Union[int, str]
class ProjectsIdDelete(BaseModel):
    id: Union[int, str]
    permanently_remove: Optional[str] = None
    full_path: Optional[str] = None
class ProjectsIdRestore(BaseModel):
    id: Union[int, str]
class ProjectsIdUploads(BaseModel):
    file: str
    id: Union[int, str]
class ProjectsIdAvatar(BaseModel):
    avatar: str
    id: Union[int, str]
class ProjectsIdShare(BaseModel):
    group_access: int
    group_id: int
    id: Union[int, str]
    expires_at: Optional[str] = None
class ProjectsIdShareGroupid(BaseModel):
    group_id: int
    id: Union[int, str]
class ProjectsIdImportprojectmembersProjectid(BaseModel):
    id: Union[int, str]
    project_id: int
class ProjectsIdHooksList(BaseModel):
    id: Union[int, str]
class ProjectsIdGetProjectHook(BaseModel):
    hook_id: int
    id: Union[int, str]
class ProjectsIdHooks(BaseModel):
    id: Union[int, str]
    url: str
    confidential_issues_events: Optional[bool] = None
    confidential_note_events: Optional[bool] = None
    deployment_events: Optional[bool] = None
    enable_ssl_verification: Optional[bool] = None
    issues_events: Optional[bool] = None
    job_events: Optional[bool] = None
    merge_requests_events: Optional[bool] = None
    note_events: Optional[bool] = None
    pipeline_events: Optional[bool] = None
    push_events_branch_filter: Optional[str] = None
    push_events: Optional[bool] = None
    releases_events: Optional[bool] = None
    tag_push_events: Optional[bool] = None
    token: Optional[str] = None
    wiki_page_events: Optional[bool] = None
class ProjectsIdEditProjectHook(BaseModel):
    hook_id: int
    id: Union[int, str]
    url: str
    confidential_issues_events: Optional[bool] = None
    confidential_note_events: Optional[bool] = None
    deployment_events: Optional[bool] = None
    enable_ssl_verification: Optional[bool] = None
    issues_events: Optional[bool] = None
    job_events: Optional[bool] = None
    merge_requests_events: Optional[bool] = None
    note_events: Optional[bool] = None
    pipeline_events: Optional[bool] = None
    push_events_branch_filter: Optional[str] = None
    push_events: Optional[bool] = None
    releases_events: Optional[bool] = None
    tag_push_events: Optional[bool] = None
    token: Optional[str] = None
    wiki_page_events: Optional[bool] = None
class ProjectsIdDeleteProjectHook(BaseModel):
    hook_id: int
    id: Union[int, str]
class CreatedForkedRelationship(BaseModel):
    forked_from_id: Union[int, str]
    id: Union[int, str]
class DeleteExistingForkedRelationship(BaseModel):
    id: Union[int, str]
class ProjectsByNameRequest(BaseModel):
    search: str
    order_by: Optional[str] = None
    sort: Optional[str] = None
class ProjectsIdHousekeeping(BaseModel):
    id: Union[int, str]
    task: Optional[str] = None
class ProjectsIdPushrule(BaseModel):
    id: Union[int, str]
class ProjectsIdPushruleAdd(BaseModel):
    id: Union[int, str]
    author_email_regex: Optional[str] = None
    branch_name_regex: Optional[str] = None
    commit_committer_check: Optional[bool] = None
    commit_message_negative_regex: Optional[str] = None
    commit_message_regex: Optional[str] = None
    deny_delete_tag: Optional[bool] = None
    file_name_regex: Optional[str] = None
    max_file_size: Optional[int] = None
    member_check: Optional[bool] = None
    prevent_secrets: Optional[bool] = None
    reject_unsigned_commits: Optional[bool] = None
class ProjectsIdPushruleEdit(BaseModel):
    id: Union[int, str]
    author_email_regex: Optional[str] = None
    branch_name_regex: Optional[str] = None
    commit_committer_check: Optional[bool] = None
    commit_message_negative_regex: Optional[str] = None
    commit_message_regex: Optional[str] = None
    deny_delete_tag: Optional[bool] = None
    file_name_regex: Optional[str] = None
    max_file_size: Optional[int] = None
    member_check: Optional[bool] = None
    prevent_secrets: Optional[bool] = None
    reject_unsigned_commits: Optional[bool] = None
class ProjectsIdPushruleDelete(BaseModel):
    id: Union[int, str]
class ProjectsIdTransferlocations(BaseModel):
    id: Union[int, str]
    search: Optional[str] = None
class ProjectsIdTransfer(BaseModel):
    id: Union[int, str]
    namespace: int
class ProjectsIdMirrorPull(BaseModel):
    id: Union[int, str]
class ProjectsIdMirrorPullStart(BaseModel):
    id: Union[int, str]
class ProjectsIdSnapshot(BaseModel):
    id: Union[int, str]
    wiki: Optional[bool] = None
class ProjectsIdStorage(BaseModel):
    id: Union[int, str]