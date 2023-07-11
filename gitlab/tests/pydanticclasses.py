# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/system_hooks.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/user_starred_metrics_dashboards.py
class ProjectsIdMetricsUserstarreddashboardsAdd(BaseModel):
    id: Union[int, str]
    dashboard_path: str
class ProjectsIdMetricsUserstarreddashboardsRemove(BaseModel):
    id: Union[int, str]
    dashboard_path: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/system_hooks.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/user_starred_metrics_dashboards.py
class ProjectsIdMetricsUserstarreddashboardsAdd(BaseModel):
    id: Union[int, str]
    dashboard_path: str
class ProjectsIdMetricsUserstarreddashboardsRemove(BaseModel):
    id: Union[int, str]
    dashboard_path: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/secure_files.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issues.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/labels_(group).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/tags.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/release_links.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/import.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pages_domains.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pipeline_triggers.py
class ListProjectTriggerTokensInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
class GetTriggerTokenDetailsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class CreateTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    description: str = Field(..., description='The trigger name.')
class UpdateProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
    description: Optional[str] = Field(None, description='The trigger name.')
class RemoveProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class TriggerPipelineWithTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    ref: str = Field(..., description=
        'The branch or tag to run the pipeline on.')
    token: str = Field(..., description='The trigger token or CI/CD job token.'
        )
    variables: Optional[Dict[str, str]] = Field(None, description=
        'A map of key-valued strings containing the pipeline variables.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/linked_epics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_state_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_remote_mirrors.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/to_do_lists.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/deploy_tokens.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dashboard_annotations.py
class CreateNewAnnotation(BaseModel):
    id: Union[int, str]
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str] = None
    description: str

    @validator('starting_at', 'ending_at', pre=True)
    def parse_iso8601(cls, v):
        if v is None:
            return v
        try:
            return datetime.fromisoformat(v)
        except ValueError:
            raise ValueError('datetime is not in ISO 8601 format')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/geo_nodes.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/merge_request_approvals.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/conan.py
class RoutePrefix(str, Enum):
    instance_level = '/packages/conan/v1'
    project_level = '/projects/:id/packages/conan/v1`'
class Ping(BaseModel):
    route_prefix: RoutePrefix = Field(description=
        'pick either instance_level or project_level')
class SearchInput(BaseModel):
    route_prefix: RoutePrefix
    q: str = Field(..., description=
        'Search query. You can use * as a wildcard.')
class AuthenticateInput(BaseModel):
    route_prefix: RoutePrefix
class CheckCredentialsInput(BaseModel):
    route_prefix: RoutePrefix
class RecipeSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifest(BaseModel):
    package_name: str = Field(description='Name of a package.')
    package_version: str = Field(description='Version of a package.')
    package_username: str = Field(description=
        'Conan username of a package. This attribute is the +-separated full path of your project.'
        )
    package_channel: str = Field(description='Channel of a package.')
class PackageManifest(RecipeManifest):
    conan_package_reference: str = Field(description=
        'Reference hash of a Conan package. Conan generates this value.')
class UploadUrls(RecipeManifest):
    files: Dict[str, int] = Field(description=
        'Dictionary of file names with their sizes.')
class PackageUploadUrlsInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
    file_sizes: Dict[str, int]
class DownloadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
class UploadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
    file_content: str
class DownloadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
class UploadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
    file_content: str
class DeletePackageInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/custom_attributes.py
class UsersIdCustomattributes(BaseModel):
    id: int
class GroupsIdCustomattributes(BaseModel):
    id: int
class ProjectsIdCustomattributes(BaseModel):
    id: int
class UsersIdCustomattributesKey(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class UsersIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class GroupsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class ProjectsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class UsersIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/epics.py
class NotMatch(BaseModel):
    author_id: Optional[int] = Field(None, description=
        'Can exclude by author ID')
    author_username: Optional[str] = Field(None, description=
        'Can exclude by author username (GitLab 14.7 and later)')
    labels: Optional[str] = Field(None, description='Can exclude by labels')
class GroupsIdEpics(BaseModel):
    id: Union[int, str]
    author_id: Optional[int] = None
    author_username: Optional[str] = None
    labels: Optional[str] = None
    with_labels_details: Optional[bool] = None
    order_by: Optional[str] = None
    sort: Optional[str] = None
    search: Optional[str] = None
    state: Optional[str] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    include_ancestor_groups: Optional[bool] = None
    include_descendant_groups: Optional[bool] = None
    my_reaction_emoji: Optional[str] = None
    not_: Optional[NotMatch] = Field(None, alias='not', description=
        'Return epics that do not match the parameters supplied')
class SingleEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class NewEpicInput(BaseModel):
    id: Union[int, str]
    title: str
    labels: Optional[str]
    description: Optional[str]
    color: Optional[str]
    confidential: Optional[bool]
    created_at: Optional[datetime]
    start_date_is_fixed: Optional[bool]
    start_date_fixed: Optional[str]
    due_date_is_fixed: Optional[bool]
    due_date_fixed: Optional[str]
    parent_id: Optional[Union[int, str]]
class UpdateEpic(BaseModel):
    id: int
    epic_iid: int
    add_labels: Optional[str] = None
    confidential: Optional[bool] = None
    description: Optional[str] = None
    due_date_fixed: Optional[str] = None
    due_date_is_fixed: Optional[bool] = None
    labels: Optional[str] = None
    parent_id: Optional[int] = None
    remove_labels: Optional[str] = None
    start_date_fixed: Optional[str] = None
    start_date_is_fixed: Optional[bool] = None
    state_event: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
class DeleteEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class CreateAToDoItem(BaseModel):
    id: Union[int, str]
    epic_iid: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issues_(epic).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/suggestions.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/product_analytics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/discussions.py
class ListProjectIssueDiscussionItems(BaseModel):
    id: Union[int, str]
    issue_iid: int
class GetSingleIssueDiscussionItem(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
class CreateNewIssueThread(BaseModel):
    body: str
    id: Union[int, str]
    issue_iid: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingIssueThreadPayload(BaseModel):
    body: str = Field(..., description='The content of the note or reply.')
    discussion_id: int = Field(..., description='The ID of a thread.')
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    issue_iid: int = Field(..., description='The IID of an issue.')
    note_id: int = Field(..., description='The ID of a thread note.')
    created_at: Optional[datetime] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyExistingIssueThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    issue_iid: int
    note_id: int
class DeleteIssueThreadNote(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
    note_id: int
class ProjectsIdSnippetsSnippetidDiscussions(BaseModel):
    id: Union[int, str]
    snippet_id: int
class ListProjectSnippetDiscussionItems(BaseModel):
    id: Union[int, str]
    snippet_id: int
class GetSingleSnippetDiscussionItem(BaseModel):
    id: Union[int, str]
    snippet_id: int
    discussion_id: int
class CreateNewSnippetThread(BaseModel):
    body: str
    id: Union[int, str]
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingSnippetThread(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class ModifyExistingSnippetThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class DeleteSnippetThreadNote(BaseModel):
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class GroupsIdEpicsEpicidDiscussions(BaseModel):
    epic_id: int
    id: Union[int, str]
class SingleEpicDiscussionItem(BaseModel):
    discussion_id: int = Field(description='The ID of a discussion item.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
class CreateNewEpicThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    created_at: Optional[Union[str, datetime]] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class AddNoteToEpicThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[Union[str, datetime]] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyEpicThreadNote(BaseModel):
    body: str = Field(description='The content of note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class DeleteEpicThreadNote(BaseModel):
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class ListMergeRequestDiscussionItems(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class SingleMergeRequestDiscussionItem(BaseModel):
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class BasicMergeRequestParams(BaseModel):
    body: str = Field(description='The content of the thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class DiffNoteParams(BaseModel):
    base_sha: str = Field(description='Base commit SHA in the source branch.')
    head_sha: str = Field(description=
        'SHA referencing HEAD of this merge request.')
    start_sha: str = Field(description=
        'SHA referencing commit in target branch.')
    new_path: str = Field(description='File path after change.')
    old_path: str = Field(description='File path before change.')
    position_type: str = Field(description=
        'Type of the position reference. Allowed values: text or image.')
class TextDiffNoteParams(BaseModel):
    new_line: Optional[int] = Field(description=
        'For text diff notes, the line number after change.')
    old_line: Optional[int] = Field(description=
        'For text diff notes, the line number before change.')
class ImageDiffNoteParams(BaseModel):
    width: Optional[int] = Field(description=
        'For image diff notes, width of the image.')
    height: Optional[int] = Field(description=
        'For image diff notes, height of the image.')
    x: Optional[float] = Field(description=
        'For image diff notes, X coordinate.')
    y: Optional[float] = Field(description=
        'For image diff notes, Y coordinate.')
class MultilineCommentsParams(BaseModel):
    line_range: dict = Field(description=
        'Line range for a multi-line diff note.')
class CreateNewMergeRequestThread(BasicMergeRequestParams):
    position: DiffNoteParams = Field(description=
        'Position when creating a diff note.')
    text_position: Optional[TextDiffNoteParams] = Field(description=
        'Position parameters for text diff notes.')
    image_position: Optional[ImageDiffNoteParams] = Field(description=
        'Position parameters for image diff notes.')
    multiline_comments: Optional[MultilineCommentsParams] = Field(description
        ='Parameters for multiline comments.')
    commit_id: Optional[str] = Field(description=
        'SHA referencing commit to start this thread on.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class ResolveMergeRequestThread(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    discussion_id: str = Field(description='The ID of a thread.')
    resolved: bool = Field(description='Resolve or unresolve the discussion.')
class AddNoteToMergeRequestThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    discussion_id: str = Field(description='The ID of a thread.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class ModifyMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description=
        'The content of the note or reply. Exactly one of body or resolved must be set.'
        )
    resolved: Optional[bool] = Field(description=
        'Resolve or unresolve the note. Exactly one of body or resolved must be set.'
        )
class DeleteMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
class ListProjectCommitDiscussionItems(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
class GetSingleCommitDiscussionItem(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
class Position(BaseModel):
    base_sha: str = Field(description='SHA of the parent commit.')
    head_sha: str = Field(description=
        'The SHA of this commit. Same as commit_id.')
    start_sha: str = Field(description='SHA of the parent commit.')
    position_type: str = Field(description=
        'Type of the position reference. Allowed values: text or image.')
    hash: Optional[str] = Field(description=
        'Position when creating a diff note.')
    new_path: Optional[str] = Field(description='File path after change.')
    new_line: Optional[int] = Field(description='Line number after change.')
    old_path: Optional[str] = Field(description='File path before change.')
    old_line: Optional[int] = Field(description='Line number before change.')
    height: Optional[int] = Field(description=
        'For image diff notes, image height.')
    width: Optional[int] = Field(description=
        'For image diff notes, image width.')
    x: Optional[int] = Field(description='For image diff notes, X coordinate.')
    y: Optional[int] = Field(description='For image diff notes, Y coordinate.')
class CreateNewCommitThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    position: Position = Field(description=
        'Position when creating a diff note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class AddNoteToCommitThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyCommitThreadNote(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description='The content of a note.')
class DeleteCommitThreadNote(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    note_id: int = Field(description='The ID of a thread note.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_relations_export.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/snippets_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/branches.py
class ProjectsIdRepositoryBranches(BaseModel):
    id: int
    search: Optional[str] = None
    regex: Optional[str] = None
class ProjectsIdRepositoryBranchesBranchSingle(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryBranchesCreate(BaseModel):
    id: int
    branch: str
    ref: str
class ProjectsIdRepositoryBranchesBranch(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryMergedbranches(BaseModel):
    id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/metadata.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/version.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/protected_tags.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issue_boards_(group).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/repository_submodules.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/milestones_(group).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/members.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/protected_branches.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/commits.py
class ProjectsIdRepositoryCommits(BaseModel):
    id: int
    ref_name: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None
    path: Optional[str] = None
    author: Optional[str] = None
    all: Optional[bool]
    with_stats: Optional[bool]
    first_parent: Optional[bool]
    order: Optional[str]
    trailers: Optional[bool]
class ProjectsIdRepositoryCommitsSha(BaseModel):
    id: int
    sha: str
    stats: Optional[bool] = None
class ProjectsIdRepositoryCommitsShaRefs(BaseModel):
    id: int
    sha: str
    type: Optional[str] = None
class ProjectsIdRepositoryCommitsShaCherrypick(BaseModel):
    id: int
    sha: str
    branch: str
    dry_run: Optional[bool] = None
    message: Optional[str] = None
class ProjectsIdRepositoryCommitsShaRevert(BaseModel):
    id: int
    sha: str
    branch: str
    dry_run: Optional[bool] = None
class ProjectsIdRepositoryCommitsShaDiff(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaComments(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaCommentsPost(BaseModel):
    id: int
    sha: str
    note: str
    path: Optional[str] = None
    line: Optional[int] = None
    line_type: Optional[str] = None
class ProjectsIdRepositoryCommitsShaDiscussions(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaStatuses(BaseModel):
    id: int
    sha: str
    ref: Optional[str] = None
    stage: Optional[str] = None
    name: Optional[str] = None
    all: Optional[bool] = None
class ProjectsIdStatusesSha(BaseModel):
    id: int
    sha: str
    state: str
    ref: Optional[str] = None
    context: Optional[str] = None
    name: Optional[str] = None
    target_url: Optional[str] = None
    description: Optional[str] = None
    coverage: Optional[float] = None
    pipeline_id: Optional[int] = None
class ProjectsIdRepositoryCommitsShaMergerequests(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaSignature(BaseModel):
    id: int
    sha: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/application_appearance.py
class ApplicationAppearance(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    pwa_name: Optional[str] = None
    pwa_short_name: Optional[str] = None
    pwa_description: Optional[str] = None
    pwa_icon: Optional[Any] = None
    logo: Optional[Any] = None
    header_logo: Optional[Any] = None
    favicon: Optional[Any] = None
    new_project_guidelines: Optional[str] = None
    profile_image_guidelines: Optional[str] = None
    header_message: Optional[str] = None
    footer_message: Optional[str] = None
    message_background_color: Optional[str] = None
    message_font_color: Optional[str] = None
    email_header_and_footer_enabled: Optional[bool] = None
class ChangeLogo(BaseModel):
    logo: Any
    pwa_icon: Any

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/users.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_vulnerabilities.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/draft_notes.py
class ProjectsIdMergerequestsMergerequestiidDraftnotes(BaseModel):
    id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidSingle(
    BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesCreate(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    note: str
    commit_id: Optional[str] = None
    in_reply_to_discussion_id: Optional[int] = None
    resolve_discussion: Optional[bool] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidModify(
    BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
    note: Optional[str] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidDelete(
    BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidPublish(
    BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesBulkpublish(BaseModel):
    id: Union[int, str]
    merge_request_iid: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_migration_by_direct_transfer.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_iteration_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/agents_for_kubernetes.py
class ListTheAgentsForAProject(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
class GetDetailsAboutAnAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class RegisterAnAgentWithAProject(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    name: str = Field(description='Name for the agent')
class DeleteARegisteredAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class ListTokensForAnAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class GetSingleAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')
class CreateAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    name: int = Field(description='Name for the token')
    description: Optional[int] = Field(None, description=
        'Description for the token')
class RevokeAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_import_export.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_level_protected_environments.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/composer.py
class GroupIdPackagesComposerPackages(BaseModel):
    id: Union[int, str]
class GroupIdPackagesComposerPSha(BaseModel):
    id: Union[int, str]
    sha: str
class V1PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str
class V2PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
class CreateAPackageInput(BaseModel):
    id: Union[int, str]
    tag: Optional[str] = None
    branch: Optional[str] = None
class ProjectsIdPackagesComposerArchivesPackagename(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/alert_management.py
class ListMetricImages(BaseModel):
    id: int
    alert_iid: int
class UpdateMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int
    url: Optional[str] = None
    url_text: Optional[str] = None
class DeleteMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/sidekiq_queues.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/vulnerability_export.py
class SecurityProjectsIdVulnerabilityexports(BaseModel):
    id: Union[int, str]
class SecurityGroupsIdVulnerabilityexports(BaseModel):
    id: Union[int, str]
class SecurityVulnerabilityexportsId(BaseModel):
    id: Union[int, str]
class SecurityVulnerabilityexportsIdDownload(BaseModel):
    id: Union[int, str]

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/events.py
class Events(BaseModel):
    action: Optional[str] = None
    target_type: Optional[str] = None
    before: Optional[datetime] = Field(None, description=
        'Include only events created before a certain date.')
    after: Optional[datetime] = Field(None, description=
        'Include only events created after a particular date.')
    target_id: Optional[int] = None
    author_id: Optional[int] = None
    search: Optional[str] = None
class AuthenticatedUserEvents(Events):
    scope: Optional[str] = None
    sort: Optional[str] = None
class UserContributionEvents(Events):
    id: int
    sort: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
class ProjectVisibleEvents(Events):
    project_id: int
    sort: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_import_export.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dora4_metrics.py
class ProjectsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None
class GroupsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/plan_limits.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/statistics_(application).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_repository_storage_moves.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/iterations_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/applications.py
class Applications(BaseModel):
    name: str
    redirect_uri: str
    scopes: str
    confidential: Optional[bool] = None
class ApplicationsId(BaseModel):
    id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/saml.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dependency_proxy.py
class GroupsIdDependencyproxyCache(BaseModel):
    id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_relations_export.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/metrics_dashboard_annotations.py
class EnvironmentsIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str
class ClustersIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/personal_access_tokens.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/__init__.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/instance_level_ci_cd_variables.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/geo_sites.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/visual_review_discussions_deprecated.py
class PositionData(BaseModel):
    base_sha: str
    start_sha: str
    head_sha: str
    position_type: str
    new_path: Optional[str] = None
    new_line: Optional[int] = None
    old_path: Optional[str] = None
    old_line: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None
class CreateNewMergeRequestThread(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    body: str
    position: Optional[PositionData] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/feature_flags.py
class StrategyParameters(BaseModel):
    pass
class StrategyScope(BaseModel):
    environment_scope: Optional[str] = None
class Strategy(BaseModel):
    name: Optional[str] = None
    parameters: Optional[StrategyParameters] = None
    scopes: Optional[List[StrategyScope]] = None
class ListFeatureFlagsForProject(BaseModel):
    id: Union[int, str]
    scope: Optional[str] = None
class GetSingleFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
class CreateFeatureFlag(BaseModel):
    id: Union[int, str]
    name: str
    version: str
    description: Optional[str] = None
    active: Optional[bool] = None
    strategies: Optional[List[Strategy]] = None
class UpdateFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
    description: Optional[str] = None
    active: Optional[bool] = None
    name: Optional[str] = None
    strategies: Optional[List[Strategy]] = None
class DeleteFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pipelines_schedules.py
class GetAllPipelineSchedulesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    scope: Optional[str] = Field(None, description=
        'The scope of pipeline schedules, must be one of: active, inactive.')
class GetSinglePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class GetPipelinesTriggeredByScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class CreateNewPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    description: str = Field(..., description=
        'The description of the pipeline schedule.')
    ref: str = Field(..., description=
        'The branch or tag name that is triggered.')
    cron: str = Field(..., description=
        'The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description=
        'The time zone supported by ActiveSupport::TimeZone, for example: Pacific Time (US & Canada) (default: UTC).'
        )
    active: Optional[bool] = Field(None, description=
        'The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated (default: true).'
        )
class EditPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    description: Optional[str] = Field(None, description=
        'The description of the pipeline schedule.')
    ref: Optional[str] = Field(None, description=
        'The branch or tag name that is triggered.')
    cron: Optional[str] = Field(None, description=
        'The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description=
        'The time zone supported by ActiveSupport::TimeZone (for example Pacific Time (US & Canada)), or TZInfo::Timezone (for example America/Los_Angeles).'
        )
    active: Optional[bool] = Field(None, description=
        'The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated.'
        )
class TakeOwnershipOfPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class DeletePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class RunScheduledPipelineImmediatelyInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class CreatePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description=
        'The key of a variable; must have no more than 255 characters; only A-Z, a-z, 0-9, and _ are allowed.'
        )
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description=
        'The type of a variable. Available types are: env_var (default) and file.'
        )
class EditPipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description=
        'The type of a variable. Available types are: env_var (default) and file.'
        )
class DeletePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dockerfile_templates.py
class TemplatesDockerfilesKey(BaseModel):
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_releases.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/keys.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/packages.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/labels_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/freeze_periods.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/broadcast_messages.py
class GetASpecificBroadcastMessage(BaseModel):
    id: int
class CreateABroadcastMessage(BaseModel):
    message: str
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class UpdateABroadcastMessage(BaseModel):
    id: int
    message: Optional[str]
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class DeleteABroadcastMessage(BaseModel):
    id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/groups.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/wikis_project.py
class ProjectsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class ProjectsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class ProjectsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class ProjectsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class ProjectsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/npm.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/avatar.py
class Avatar(BaseModel):
    email: str
    size: Optional[int] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_group.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/error_tracking.py
class GetErrorTrackingSettings(BaseModel):
    id: Union[int, str]
class CreateErrorTrackingSettings(BaseModel):
    id: int
    active: bool
    integrated: bool
class EnableOrDisableTheErrorTrackingProjectSettings(BaseModel):
    id: int
    active: bool
    integrated: Optional[bool] = None
class ListProjectClientKeys(BaseModel):
    id: Union[int, str]
class CreateAClientKey(BaseModel):
    id: Union[int, str]
class DeleteAClientKey(BaseModel):
    id: Union[int, str]
    key_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/debian_project_distributions.py
class ListAllDebianDistributionsInAProject(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class SingleDebianProjectDistributionKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_label_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/repository_files.py
class ProjectIdRepositoryFiles(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    file_path: str = Field(description='URL encoded full path to new file')
    ref: str = Field(description='The name of branch, tag or commit')
class ProjectIdRepositoryFilesBlame(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    file_path: str = Field(description=
        'URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(description='The name of branch, tag or commit.')
    range_start: int = Field(description=
        'The first line of the range to blame.')
    range_end: int = Field(description='The last line of the range to blame.')
    range: Optional[dict] = Field(description='Blame range.')
class ProjectsIdRepositoryFilesFilepathRaw(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    file_path: str = Field(..., description=
        'URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(..., description=
        'The name of branch, tag or commit. Default is the HEAD of the project.'
        )
    lfs: Optional[bool] = Field(None, description=
        'Determines if the response should be Git LFS file contents, rather than the pointer. If the file is not tracked by Git LFS, ignored. Defaults to false.'
        )
class ProjectsIdRepositoryFilesFilepathCreate(BaseModel):
    branch: str = Field(description=
        'Name of the new branch to create. The commit is added to this branch.'
        )
    commit_message: str = Field(description='The commit message.')
    content: str = Field(description='The file’s content.')
    file_path: str = Field(description=
        'URL-encoded full path to new file. For example: lib%2Fclass%2Erb.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    author_email: Optional[str] = Field(None, description=
        'The commit author’s email address.')
    author_name: Optional[str] = Field(None, description=
        'The commit author’s name.')
    encoding: Optional[str] = Field(None, description=
        'Change encoding to base64. Default is text.')
    execute_filemode: Optional[bool] = Field(None, description=
        'Enables or disables the execute flag on the file. Can be true or false.'
        )
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathUpdate(BaseModel):
    branch: str
    commit_message: str
    content: str
    file_path: str
    id: Union[int, str]
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    encoding: Optional[str] = None
    execute_filemode: Optional[bool] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathDelete(BaseModel):
    branch: str
    commit_message: str
    file_path: str
    id: int
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositorySubmodulesSubmodule(BaseModel):
    id: int
    submodule: str
    branch: str
    commit_sha: str
    commit_message: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/nuget.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/container_registry.py
class ContainerRegistryAccessLevelEnum(str, Enum):
    enabled = 'enabled'
    private = 'private'
    disabled = 'disabled'
class ChangeContainerRegistryVisibility(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project accessible by the authenticated user.'
        )
    container_registry_access_level: Optional[ContainerRegistryAccessLevelEnum
        ] = Field(default=None, description=
        'The desired visibility of the Container Registry. One of enabled (default), private, or disabled.'
        )
class ListProjectRegistryRepositories(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
class GroupsIdRegistryRepositories(BaseModel):
    id: Union[int, str]
class RegistryRepositoriesId(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
    size: Optional[bool] = None
class ProjectsIdRegistryRepositoriesRepositoryid(BaseModel):
    id: Union[int, str]
    repository_id: int
class ProjectsIdRegistryRepositoriesRepositoryidTags(BaseModel):
    id: Union[int, str]
    repository_id: int
class GetDetailsOfARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteRegistryRepositoryTagsInBulk(BaseModel):
    id: Union[int, str]
    repository_id: int
    name_regex: Optional[str] = None
    name_regex_delete: str
    name_regex_keep: Optional[str] = None
    keep_n: Optional[int] = None
    older_than: Optional[str] = None
class ObtainTokenInput(BaseModel):
    CI_SERVER_URL: str = Field(description='CI server URL.')
    service: str = Field(default='container_registry', description=
        'The service type.')
    scope: str = Field(description='Scope for the token.')
class DeleteImageTagsByReferenceInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    CI_REGISTRY_IMAGE: str = Field(description='The registry image.')
    CI_COMMIT_SHORT_SHA: str = Field(description='The commit SHA.')
class ListAllContainerRepositoriesInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    admin_username: str = Field(description='The admin username.')
    admin_password: str = Field(description='The admin password.')
    service: str = Field(default='container_registry', description=
        'The service type.')
    scope: str = Field(default='registry:catalog:*', description=
        'Scope for the token.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_milestone_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/templates.py
class TemplatesGitignoresKey(BaseModel):
    key: str
class TemplatesGitlabciymlsKey(BaseModel):
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/jobs.py
class JobScope(str, Enum):
    created = 'created'
    pending = 'pending'
    running = 'running'
    failed = 'failed'
    success = 'success'
    canceled = 'canceled'
    skipped = 'skipped'
    waiting_for_resource = 'waiting_for_resource'
    manual = 'manual'
class ListProjectJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
class ListPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
    include_retried: Optional[bool] = Field(False, description=
        'Include retried jobs in the response.')
class ListPipelineTriggerJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
class GetAllowedAgentsInput(BaseModel):
    CI_JOB_TOKEN: str = Field(..., description=
        'Token value associated with the GitLab-provided CI_JOB_TOKEN variable.'
        )
class GetSingleJobInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='ID of a job.')
class JobInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='The ID of a job.')
class JobVariable(BaseModel):
    key: str = Field(..., description='The key of the job variable.')
    value: str = Field(..., description='The value of the job variable.')
class RunJobInput(JobInput):
    job_variables_attributes: Optional[List[JobVariable]] = Field(None,
        description=
        'An array containing the custom variables available to the job.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/gitignore.py
class ListAllGitignoreTemplates(BaseModel):
    pass
class GetSingleGitignoreTemplate(BaseModel):
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/releases.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/gitlab_ci_yaml.py
class ListAllCICDYamlTemplates(BaseModel):
    pass
class GetSingleCICDYamlTemplate(BaseModel):
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/milestones_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_activity_analytics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/job_artifacts.py
class GetJobArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int
    job_token: Optional[str] = None
class DownloadArtifacts(BaseModel):
    id: Union[int, str]
    ref_name: str
    job: str
    job_token: Optional[str] = None
class DownloadSingleArtifactByJobID(BaseModel):
    id: Union[int, str]
    job_id: int
    artifact_path: str
    job_token: Optional[str] = None
class DownloadSingleArtifactFromSpecificTag(BaseModel):
    id: Union[int, str]
    ref_name: str
    artifact_path: str
    job: str
    job_token: Optional[str] = None
class KeepArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issues_statistics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_statistics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/experiments.py
class ListAllExperiments(BaseModel):
    pass

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/scim.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/feature_flag_user_lists.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/vulnerability_findings.py
class ProjectsIdVulnerabilityfindings(BaseModel):
    id: int
    report_type: Optional[List[str]] = None
    scope: Optional[str] = None
    severity: Optional[List[str]] = None
    confidence: Optional[List[str]] = None
    pipeline_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/licenses_(templates).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/topics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/secrets.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/debian.py
class ProjectsIdPackagesDebianFilename(BaseModel):
    id: str
    file_name: str
    distribution: Optional[str] = None
    component: Optional[str] = None
class ProjectsIdPackagesDebianPoolDistributionLetterPackagenamePackageversionFilename(
    BaseModel):
    distribution: str
    letter: str
    package_name: str
    package_version: str
    file_name: str
class DownloadADistributionReleaseFile(BaseModel):
    distribution: str
class DownloadASignedDistributionReleaseFile(BaseModel):
    distribution: str
class DownloadAReleaseFileSignature(BaseModel):
    distribution: str
class DownloadAPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadAPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadADebianInstallerPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DowloadADebianInstallerPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadASourcePackagesIndex(BaseModel):
    distribution: str
    component: str
class DownloadASourcePackagesIndexByHash(BaseModel):
    distribution: str
    component: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/ruby_gems.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/markdown.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/debian_group_distributions.py
class ListAllDebianDistributionsInAGroup(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class GroupsIdDebiandistributionsCodenameKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/variables_project.py
class Variable(BaseModel):
    key: str
    value: str
    variable_type: Optional[str] = 'env_var'
    protected: Optional[bool] = False
    masked: Optional[bool] = False
    raw: Optional[bool] = False
    environment_scope: Optional[str] = '*'
    description: Optional[str] = None
class VariableFilter(BaseModel):
    environment_scope: Optional[str] = None
class GetProjectVariables(BaseModel):
    id: Union[int, str]
class GetVariable(BaseModel):
    id: Union[int, str]
    key: str
    filter: Optional[VariableFilter] = None
class CreateVariable(GetProjectVariables, Variable):
    pass
class UpdateVariable(GetVariable, Variable):
    pass
class DeleteVariable(GetVariable):
    pass

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/links_(epic).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/wikis_group.py
class GroupsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class GroupsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class GroupsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class GroupsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class GroupsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/audit_events.py
class Auditevents(BaseModel):
    created_after: Optional[str] = None
    created_before: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[int] = None
class AuditeventsId(BaseModel):
    id: int
class GroupsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class GroupsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int
class ProjectsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class ProjectsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_access_tokens.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/runners.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/environments.py
class ProjectsIdEnvironments(BaseModel):
    id: int
    name: Optional[str] = None
    search: Optional[str] = None
    states: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentid(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsCreate(BaseModel):
    id: int
    name: str
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentsid(BaseModel):
    id: int
    environment_id: int
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentidDelete(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsReviewapps(BaseModel):
    id: int
    before: Optional[datetime] = None
    limit: Optional[int] = None
    dry_run: Optional[bool] = None
class ProjectsIdEnvironmentsEnvironmentidStop(BaseModel):
    id: int
    environment_id: int
    force: Optional[bool] = None
class ProjectsIdEnvironmentsStopstale(BaseModel):
    id: int
    before: datetime

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_level_protected_branches.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/http_wrapper.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/gitlab_pages.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/marketplace.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/snippets.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/notes_(comments).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/terraform_registry.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/repositories.py
class ProjectsIdRepositoryTree(BaseModel):
    id: int
    page_token: Optional[str] = None
    pagination: Optional[str] = None
    path: Optional[str] = None
    per_page: Optional[str] = None
    recursive: bool = Field(False)
    ref: Optional[str] = None
class ProjectsIdRepositoryBlobsSha(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryBlobsShaRaw(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryArchive(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    path: Optional[str] = Field(None, description=
        'The subpath of the repository to download. Defaults to the whole repository.'
        )
    sha: Optional[str] = Field(None, description=
        'The commit SHA to download. A tag, branch reference, or SHA can be used. Defaults to the tip of the default branch.'
        )
    format: Optional[str] = Field(None, description=
        "The archive format. Options are: 'bz2', 'tar', 'tar.bz2', 'tar.gz', 'tb2', 'tbz', 'tbz2', 'zip'. Defaults to 'tar.gz'."
        )
class ProjectsIdRepositoryCompare(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    from_commit_or_branch: str = Field(..., alias='from', description=
        'The commit SHA or branch name.')
    to: str = Field(..., description='The commit SHA or branch name.')
    from_project_id: Optional[int] = Field(None, description=
        'The ID to compare from.')
    straight: Optional[bool] = Field(False, description=
        'Comparison method: true for direct comparison between from and to (from..to), false to compare using merge base (from…to)’. Default is false.'
        )
class ProjectsIdRepositoryContributors(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    order_by: Optional[str] = Field(None, description=
        'Return contributors ordered by name, email, or commits (orders by commit date) fields. Default is commits.'
        )
    sort: Optional[str] = Field(None, description=
        'Return contributors sorted in asc or desc order. Default is asc.')
class ProjectsIdRepositoryMergebase(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    refs: List[str] = Field(description=
        'The refs to find the common ancestor of. Accepts multiple refs.')
class ProjectsIdRepositoryChangelog(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    version: str = Field(description=
        'The version to generate the changelog for. The format must follow semantic versioning.'
        )
    branch: Optional[str] = Field(None, description=
        'The branch to commit the changelog changes to. Defaults to the project’s default branch.'
        )
    config_file: Optional[str] = Field(None, description=
        'Path to the changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.'
        )
    date: Optional[datetime] = Field(None, description=
        'The date and time of the release. Defaults to the current time.')
    file: Optional[str] = Field(None, description=
        'The file to commit the changes to. Defaults to CHANGELOG.md.')
    from_: Optional[str] = Field(None, alias='from', description=
        'The SHA of the commit that marks the beginning of the range of commits to include in the changelog. This commit isn’t included in the changelog.'
        )
    message: Optional[str] = Field(None, description=
        'The commit message to use when committing the changes. Defaults to Add changelog for version X, where X is the value of the version argument.'
        )
    to: Optional[str] = Field(None, description=
        'The SHA of the commit that marks the end of the range of commits to include in the changelog. This commit is included in the changelog. Defaults to the branch specified in the branch attribute. Limited to 15000 commits unless the feature flag changelog_commits_limitation is disabled.'
        )
    trailer: Optional[str] = Field(None, description=
        'The Git trailer to use for including commits. Defaults to Changelog. Case-sensitive: Example does not match example or eXaMpLE.'
        )
class GenerateChangelogData(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    version: str = Field(description=
        'The version to generate the changelog for. The format must follow semantic versioning.'
        )
    config_file: Optional[str] = Field(description=
        'The path of changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.'
        )
    date: Optional[datetime] = Field(description=
        'The date and time of the release. Uses ISO 8601 format. Defaults to the current time.'
        )
    from_: Optional[str] = Field(alias='from', description=
        'The start of the range of commits (as a SHA) to use for generating the changelog. This commit itself isn’t included in the list.'
        )
    to: Optional[str] = Field(description=
        'The end of the range of commits (as a SHA) to use for the changelog. This commit is included in the list. Defaults to the HEAD of the default project branch.'
        )
    trailer: Optional[str] = Field(description=
        'The Git trailer to use for including commits. Defaults to Changelog.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/deployments.py
class ListProjectDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class GetASpecificDeployment(BaseModel):
    id: int
    deployment_id: int
class GetDeploymentFrequency(BaseModel):
    id: int
    finished_after: Optional[datetime] = None
class DeploymentDuration(BaseModel):
    created_at: datetime
    finished_at: datetime
class ListProjectDeployment(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsCreate(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsDeploymentid(BaseModel):
    id: int
    deployment_id: int
class CreateADeployment(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeploymentsDeploymentidUpdate(BaseModel):
    id: int
    deployment_id: int
    status: str
class ProjectsIdDeploymentsDeploymentidDelete(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidMergerequests(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidApproval(BaseModel):
    id: int
    deployment_id: int
    status: str
    comment: Optional[str] = None
    represented_as: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/snippet_repository_storage_moves.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/notification_settings.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/iterations_(group).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/search.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_aliases.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/http_wrapper_privatetoken.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_badges.py
class GroupsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class GroupsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesAdd(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class GroupsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class GroupsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/external_status_checks.py
class ProjectsIdExternalstatuschecks(BaseModel):
    id: Union[int, str] = Field(description='ID of a project')
class CreateUpdateExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    name: Optional[str] = Field(description=
        'Display name of external status check service')
    external_url: Optional[str] = Field(description=
        'URL of external status check service')
    protected_branch_ids: Optional[List[int]] = Field(description=
        'IDs of protected branches to scope the rule by')
class UpdateExternalStatusCheckService(BaseModel):
    id: Union[int, str]
    check_id: int
    name: Optional[str] = None
    external_url: Optional[str] = None
    protected_branch_ids: Optional[List[int]] = None
class DeleteExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    check_id: int = Field(description='ID of an external status check service')
class MergeRequestStatusChecks(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
class SetStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    sha: str = Field(description='SHA at HEAD of the source branch')
    external_status_check_id: int = Field(description=
        'ID of an external status check')
    status: Optional[str] = Field(description=
        'Set to passed to pass the check or failed to fail it')
class RetryFailedStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    external_status_check_id: int = Field(description=
        'ID of a failed external status check')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/access_requests.py
class ProjectsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class ProjectsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class GroupsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int
class ProjectsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_templates.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/sidekiq_metrics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_level_protected_environments.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/invitations.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/go_proxy.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/license.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_repository_storage_moves.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/merge_trains.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/vulnerabilities.py
class VulnerabilitiesId(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdConfirm(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdResolve(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdDismiss(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdRevert(BaseModel):
    id: Union[int, str]

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/variables_group.py
class ListGroupVariables(BaseModel):
    id: Union[int, str]
class VariableType(str, Enum):
    env_var = 'env_var'
    file = 'file'
class ShowGroupVariableDetails(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
class CreateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class UpdateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class RemoveGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pypi.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/maven.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_access_tokens.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/projects.py
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
    custom_attributes: Optional[Dict[str, str]] = Field(None, description=
        'A dictionary of custom attributes to filter by')
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
class CreateProjectRequest(BaseModel):
    name: Optional[str] = Field(None, description=
        'The name of the new project. Equals path if not provided.')
    path: Optional[str] = Field(None, description=
        'Repository name for new project. Generated based on name if not provided (generated as lowercase with dashes). Starting with GitLab 14.9, path must not start or end with a special character and must not contain consecutive special characters.'
        )
    allow_merge_on_skipped_pipeline: Optional[bool] = Field(None,
        description=
        'Set whether or not merge requests can be merged with skipped jobs.')
    only_allow_merge_if_all_status_checks_passed: Optional[bool] = Field(None,
        description=
        'Indicates that merges of merge requests should be blocked unless all status checks have passed. Defaults to false. Introduced in GitLab 15.5 with feature flag only_allow_merge_if_all_status_checks_passed disabled by default.'
        )
    analytics_access_level: Optional[str] = Field(None, description=
        'One of disabled, private or enabled.')
    approvals_before_merge: Optional[int] = Field(None, description=
        'How many approvers should approve merge requests by default. To configure approval rules, see Merge request approvals API. Deprecated in GitLab 16.0.'
        )
    auto_cancel_pending_pipelines: Optional[str] = Field(None, description=
        'Auto-cancel pending pipelines. This action toggles between an enabled state and a disabled state; it is not a boolean.'
        )
    auto_devops_deploy_strategy: Optional[str] = Field(None, description=
        'Auto Deploy strategy (continuous, manual or timed_incremental).')
    auto_devops_enabled: Optional[bool] = Field(None, description=
        'Enable Auto DevOps for this project.')
    autoclose_referenced_issues: Optional[bool] = Field(None, description=
        'Set whether auto-closing referenced issues on default branch.')
    avatar: Optional[Union[str, Any]] = Field(None, description=
        'Image file for avatar of the project.')
    build_git_strategy: Optional[str] = Field(None, description=
        'The Git strategy. Defaults to fetch.')
    build_timeout: Optional[int] = Field(None, description=
        'The maximum amount of time, in seconds, that a job can run.')
    builds_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    ci_config_path: Optional[str] = Field(None, description=
        'The path to CI configuration file.')
    container_expiration_policy_attributes: Optional[dict] = Field(None,
        description='Update the image cleanup policy for this project.')
    container_registry_access_level: Optional[str] = Field(None,
        description=
        'Set visibility of container registry, for this project, to one of disabled, private or enabled.'
        )
    container_registry_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable container registry for this project. Use container_registry_access_level instead.'
        )
    default_branch: Optional[str] = Field(None, description=
        'The default branch name. Requires initialize_with_readme to be true.')
    description: Optional[str] = Field(None, description=
        'Short project description.')
    emails_disabled: Optional[bool] = Field(None, description=
        'Disable email notifications.')
    external_authorization_classification_label: Optional[str] = Field(None,
        description='The classification label for the project.')
    forking_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    group_with_project_templates_id: Optional[int] = Field(None,
        description=
        'For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true.'
        )
    import_url: Optional[str] = Field(None, description=
        'URL to import repository from. When the URL value isn’t empty, you must not set initialize_with_readme to true. Doing so might result in the following error: not a git repository.'
        )
    initialize_with_readme: Optional[bool] = Field(None, description=
        'Whether to create a Git repository with just a README.md file. Default is false.'
        )
    issues_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    issues_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable issues for this project. Use issues_access_level instead.'
        )
    jobs_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable jobs for this project. Use builds_access_level instead.'
        )
    lfs_enabled: Optional[bool] = Field(None, description='Enable LFS.')
    merge_method: Optional[str] = Field(None, description=
        'Set the merge method used.')
    merge_pipelines_enabled: Optional[bool] = Field(None, description=
        'Enable or disable merge pipelines.')
    merge_requests_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    merge_requests_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable merge requests for this project. Use merge_requests_access_level instead.'
        )
    merge_trains_enabled: Optional[bool] = Field(None, description=
        'Enable or disable merge trains.')
    mirror_trigger_builds: Optional[bool] = Field(None, description=
        'Pull mirroring triggers builds.')
    mirror: Optional[bool] = Field(None, description=
        'Enables pull mirroring in a project.')
    namespace_id: Optional[int] = Field(None, description=
        'Namespace for the new project (defaults to the current user’s namespace).'
        )
    only_allow_merge_if_all_discussions_are_resolved: Optional[bool] = Field(
        None, description=
        'Set whether merge requests can only be merged when all the discussions are resolved.'
        )
    only_allow_merge_if_pipeline_succeeds: Optional[bool] = Field(None,
        description=
        'Set whether merge requests can only be merged with successful pipelines.'
        )
    packages_enabled: Optional[bool] = Field(None, description=
        'Enable or disable packages repository feature.')
    pages_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, enabled, or public.')
    printing_merge_request_link_enabled: Optional[bool] = Field(None,
        description=
        'Show link to create/view merge request when pushing from the command line.'
        )
    public_builds: Optional[bool] = Field(None, description=
        'If true, jobs can be viewed by non-project members.')
    releases_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    environments_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    feature_flags_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    infrastructure_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    monitor_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    remove_source_branch_after_merge: Optional[bool] = Field(None,
        description=
        'Enable Delete source branch option by default for all new merge requests.'
        )
    repository_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    repository_storage: Optional[str] = Field(None, description=
        'Which storage shard the repository is on. (administrator only)')
    request_access_enabled: Optional[bool] = Field(None, description=
        'Allow users to request member access.')
    requirements_access_level: Optional[str] = Field(None, description=
        'One of disabled, private or enabled')
    resolve_outdated_diff_discussions: Optional[bool] = Field(None,
        description=
        'Automatically resolve merge request diffs discussions on lines changed with a push.'
        )
    security_and_compliance_access_level: Optional[str] = Field(None,
        description=
        '(GitLab 14.9 and later) Security and compliance access level. One of disabled, private, or enabled.'
        )
    shared_runners_enabled: Optional[bool] = Field(None, description=
        'Enable shared runners for this project.')
    group_runners_enabled: Optional[bool] = Field(None, description=
        'Enable group runners for this project.')
    snippets_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    snippets_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable snippets for this project. Use snippets_access_level instead.'
        )
    squash_option: Optional[str] = Field(None, description=
        'One of never, always, default_on, or default_off.')
    tag_list: Optional[list] = Field(None, description=
        '(Deprecated in GitLab 14.0) The list of tags for a project; put array of tags, that should be finally assigned to a project. Use topics instead.'
        )
    template_name: Optional[str] = Field(None, description=
        'When used without use_custom_template, name of a built-in project template.'
        )
    template_project_id: Optional[int] = Field(None, description=
        'When used with use_custom_template, project ID of a custom project template.'
        )
    topics: Optional[list] = Field(None, description=
        'The list of topics for a project; put array of topics, that should be finally assigned to a project. (Introduced in GitLab 14.0.)'
        )
    use_custom_template: Optional[bool] = Field(None, description=
        'Use either custom instance or group (with group_with_project_templates_id) project template.'
        )
    visibility: Optional[str] = Field(None, description=
        'See project visibility level.')
    wiki_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    wiki_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable wiki for this project. Use wiki_access_level instead.'
        )
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
    container_expiration_policy_attributes: Optional[
        ContainerExpirationPolicyAttributes] = None
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

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/merge_requests.py
class ProjectsMergeRequestCreate(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    source_branch: str = Field(description='The source branch name.')
    target_branch: str = Field(description='The target branch name.')
    title: str = Field(description='The title of merge request.')
    allow_collaboration: Optional[bool] = Field(None, description=
        'Allow commits from members who can merge to the target branch.')
    approvals_before_merge: Optional[int] = Field(None, description=
        'The amount of approvals required before merging.')
    allow_maintainer_to_push: Optional[bool] = Field(None, description=
        'Allow users who can merge to the target branch to push to the source branch.'
        )
    assignee_id: Optional[int] = Field(None, description=
        'The ID of a user to assign merge request.')
    assignee_ids: Optional[List[int]] = Field(None, description=
        'The IDs of users to assign merge request.')
    description: Optional[str] = Field(None, description=
        'The description of merge request.')
    labels: Optional[str] = Field(None, description=
        'Comma-separated list of label names.')
    milestone_id: Optional[int] = Field(None, description=
        'The global ID of a milestone to assign merge request.')
    remove_source_branch: Optional[bool] = Field(None, description=
        'Flag indicating if a merge request should remove the source branch when merging.'
        )
    reviewer_ids: Optional[List[int]] = Field(None, description=
        'The IDs of users to request review from when merge request created.')
    squash: Optional[bool] = Field(None, description=
        'Squash commits into a single commit when merging.')
    squash_on_merge: Optional[bool] = Field(None, description=
        'Squash commits into a single commit after merging.')
    target_project_id: Optional[int] = Field(None, description=
        'The target project ID. If the user is a maintainer of the target project, the source project is set as the target_project_id.'
        )

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/member_roles.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_weight_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/search_migrations.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/integrations.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/emoji_reactions.py
class AwardEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
class SingleEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class NewEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    name: str
class DeleteEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class ListCommentEmojiReactionsParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
class GetCommentEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int
class AwardCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    name: str
class DeleteCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/settings_(application).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pipelines.py
class Scope(str, Enum):
    running = 'running'
    pending = 'pending'
    finished = 'finished'
    branches = 'branches'
    tags = 'tags'
class Status(str, Enum):
    created = 'created'
    waiting_for_resource = 'waiting_for_resource'
    preparing = 'preparing'
    pending = 'pending'
    running = 'running'
    success = 'success'
    failed = 'failed'
    canceled = 'canceled'
    skipped = 'skipped'
    manual = 'manual'
    scheduled = 'scheduled'
class Source(str, Enum):
    push = 'push'
    web = 'web'
    trigger = 'trigger'
    schedule = 'schedule'
    api = 'api'
    external = 'external'
    pipeline = 'pipeline'
    chat = 'chat'
    webide = 'webide'
    merge_request_event = 'merge_request_event'
    external_pull_request_event = 'external_pull_request_event'
    parent_pipeline = 'parent_pipeline'
    ondemand_dast_scan = 'ondemand_dast_scan'
    ondemand_dast_validation = 'ondemand_dast_validation'
class OrderBy(str, Enum):
    id = 'id'
    status = 'status'
    ref = 'ref'
    updated_at = 'updated_at'
    user_id = 'user_id'
class Sort(str, Enum):
    asc = 'asc'
    desc = 'desc'
class ListProjectPipelinesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    scope: Optional[Scope]
    status: Optional[Status]
    source: Optional[Source]
    ref: Optional[str]
    sha: Optional[str]
    yaml_errors: Optional[bool]
    username: Optional[str]
    updated_after: Optional[datetime]
    updated_before: Optional[datetime]
    name: Optional[str]
    order_by: Optional[OrderBy]
    sort: Optional[Sort]
class GetPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineVariablesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportSummaryInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetLatestPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    ref: Optional[str] = Field(None, description=
        'The branch or tag to check for the latest pipeline. Defaults to the default branch when not specified.'
        )
class CreatePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    ref: str = Field(..., description=
        'The branch or tag to run the pipeline on.')
    variables: Optional[List[Dict[str, Union[str, Dict[str, str]]]]] = Field(
        None, description=
        'An array of hashes containing the variables available in the pipeline.'
        )
class RetryJobsInPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class CancelPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class DeletePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/lint_.gitlab_ci.yml.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/service_data.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dependencies.py
class ProjectsIdDependencies(BaseModel):
    id: Union[int, str]
    package_manager: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_badges.py
class ProjectsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class ProjectsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesCreate(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/helm.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/namespaces.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/links_(issue).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/deploy_keys.py
class Deploykeys(BaseModel):
    public: Optional[bool] = None
class ProjectsIdDeploykeys(BaseModel):
    id: int
class UsersIdorusernameProjectdeploykeys(BaseModel):
    id_or_username: str
class ProjectsIdDeploykeysKeyidSingle(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysAdd(BaseModel):
    id: int
    key: str
    title: str
    can_push: Optional[bool] = None
    expires_at: Optional[datetime] = None
class ProjectsIdDeploykeysKeyidUpdate(BaseModel):
    id: int
    can_push: Optional[bool] = None
    title: Optional[str] = None
class ProjectsIdDeploykeysKeyidDelete(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysKeyidEnable(BaseModel):
    id: int
    key_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issue_boards_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/job_token_scopes.py
class GetProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
class PatchProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
    enabled: bool
class GetProjectCICDJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
class CreateNewProjectToJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int
class RemoveProjectFromJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/merge_request_context_commits.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/system_hooks.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/user_starred_metrics_dashboards.py
class ProjectsIdMetricsUserstarreddashboardsAdd(BaseModel):
    id: Union[int, str]
    dashboard_path: str
class ProjectsIdMetricsUserstarreddashboardsRemove(BaseModel):
    id: Union[int, str]
    dashboard_path: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/secure_files.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issues.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/labels_(group).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/tags.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/release_links.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/import.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pages_domains.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pipeline_triggers.py
class ListProjectTriggerTokensInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
class GetTriggerTokenDetailsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class CreateTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    description: str = Field(..., description='The trigger name.')
class UpdateProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
    description: Optional[str] = Field(None, description='The trigger name.')
class RemoveProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class TriggerPipelineWithTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    ref: str = Field(..., description=
        'The branch or tag to run the pipeline on.')
    token: str = Field(..., description='The trigger token or CI/CD job token.'
        )
    variables: Optional[Dict[str, str]] = Field(None, description=
        'A map of key-valued strings containing the pipeline variables.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/linked_epics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_state_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_remote_mirrors.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/to_do_lists.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/deploy_tokens.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dashboard_annotations.py
class CreateNewAnnotation(BaseModel):
    id: Union[int, str]
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str] = None
    description: str

    @validator('starting_at', 'ending_at', pre=True)
    def parse_iso8601(cls, v):
        if v is None:
            return v
        try:
            return datetime.fromisoformat(v)
        except ValueError:
            raise ValueError('datetime is not in ISO 8601 format')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/geo_nodes.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/merge_request_approvals.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/conan.py
class RoutePrefix(str, Enum):
    instance_level = '/packages/conan/v1'
    project_level = '/projects/:id/packages/conan/v1`'
class Ping(BaseModel):
    route_prefix: RoutePrefix = Field(description=
        'pick either instance_level or project_level')
class SearchInput(BaseModel):
    route_prefix: RoutePrefix
    q: str = Field(..., description=
        'Search query. You can use * as a wildcard.')
class AuthenticateInput(BaseModel):
    route_prefix: RoutePrefix
class CheckCredentialsInput(BaseModel):
    route_prefix: RoutePrefix
class RecipeSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifest(BaseModel):
    package_name: str = Field(description='Name of a package.')
    package_version: str = Field(description='Version of a package.')
    package_username: str = Field(description=
        'Conan username of a package. This attribute is the +-separated full path of your project.'
        )
    package_channel: str = Field(description='Channel of a package.')
class PackageManifest(RecipeManifest):
    conan_package_reference: str = Field(description=
        'Reference hash of a Conan package. Conan generates this value.')
class UploadUrls(RecipeManifest):
    files: Dict[str, int] = Field(description=
        'Dictionary of file names with their sizes.')
class PackageUploadUrlsInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
    file_sizes: Dict[str, int]
class DownloadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
class UploadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
    file_content: str
class DownloadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
class UploadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
    file_content: str
class DeletePackageInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/custom_attributes.py
class UsersIdCustomattributes(BaseModel):
    id: int
class GroupsIdCustomattributes(BaseModel):
    id: int
class ProjectsIdCustomattributes(BaseModel):
    id: int
class UsersIdCustomattributesKey(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class UsersIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class GroupsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class ProjectsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class UsersIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/epics.py
class NotMatch(BaseModel):
    author_id: Optional[int] = Field(None, description=
        'Can exclude by author ID')
    author_username: Optional[str] = Field(None, description=
        'Can exclude by author username (GitLab 14.7 and later)')
    labels: Optional[str] = Field(None, description='Can exclude by labels')
class GroupsIdEpics(BaseModel):
    id: Union[int, str]
    author_id: Optional[int] = None
    author_username: Optional[str] = None
    labels: Optional[str] = None
    with_labels_details: Optional[bool] = None
    order_by: Optional[str] = None
    sort: Optional[str] = None
    search: Optional[str] = None
    state: Optional[str] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    include_ancestor_groups: Optional[bool] = None
    include_descendant_groups: Optional[bool] = None
    my_reaction_emoji: Optional[str] = None
    not_: Optional[NotMatch] = Field(None, alias='not', description=
        'Return epics that do not match the parameters supplied')
class SingleEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class NewEpicInput(BaseModel):
    id: Union[int, str]
    title: str
    labels: Optional[str]
    description: Optional[str]
    color: Optional[str]
    confidential: Optional[bool]
    created_at: Optional[datetime]
    start_date_is_fixed: Optional[bool]
    start_date_fixed: Optional[str]
    due_date_is_fixed: Optional[bool]
    due_date_fixed: Optional[str]
    parent_id: Optional[Union[int, str]]
class UpdateEpic(BaseModel):
    id: int
    epic_iid: int
    add_labels: Optional[str] = None
    confidential: Optional[bool] = None
    description: Optional[str] = None
    due_date_fixed: Optional[str] = None
    due_date_is_fixed: Optional[bool] = None
    labels: Optional[str] = None
    parent_id: Optional[int] = None
    remove_labels: Optional[str] = None
    start_date_fixed: Optional[str] = None
    start_date_is_fixed: Optional[bool] = None
    state_event: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
class DeleteEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class CreateAToDoItem(BaseModel):
    id: Union[int, str]
    epic_iid: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issues_(epic).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/suggestions.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/product_analytics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/discussions.py
class ListProjectIssueDiscussionItems(BaseModel):
    id: Union[int, str]
    issue_iid: int
class GetSingleIssueDiscussionItem(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
class CreateNewIssueThread(BaseModel):
    body: str
    id: Union[int, str]
    issue_iid: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingIssueThreadPayload(BaseModel):
    body: str = Field(..., description='The content of the note or reply.')
    discussion_id: int = Field(..., description='The ID of a thread.')
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    issue_iid: int = Field(..., description='The IID of an issue.')
    note_id: int = Field(..., description='The ID of a thread note.')
    created_at: Optional[datetime] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyExistingIssueThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    issue_iid: int
    note_id: int
class DeleteIssueThreadNote(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
    note_id: int
class ProjectsIdSnippetsSnippetidDiscussions(BaseModel):
    id: Union[int, str]
    snippet_id: int
class ListProjectSnippetDiscussionItems(BaseModel):
    id: Union[int, str]
    snippet_id: int
class GetSingleSnippetDiscussionItem(BaseModel):
    id: Union[int, str]
    snippet_id: int
    discussion_id: int
class CreateNewSnippetThread(BaseModel):
    body: str
    id: Union[int, str]
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingSnippetThread(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class ModifyExistingSnippetThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class DeleteSnippetThreadNote(BaseModel):
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class GroupsIdEpicsEpicidDiscussions(BaseModel):
    epic_id: int
    id: Union[int, str]
class SingleEpicDiscussionItem(BaseModel):
    discussion_id: int = Field(description='The ID of a discussion item.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
class CreateNewEpicThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    created_at: Optional[Union[str, datetime]] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class AddNoteToEpicThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[Union[str, datetime]] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyEpicThreadNote(BaseModel):
    body: str = Field(description='The content of note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class DeleteEpicThreadNote(BaseModel):
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class ListMergeRequestDiscussionItems(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class SingleMergeRequestDiscussionItem(BaseModel):
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class BasicMergeRequestParams(BaseModel):
    body: str = Field(description='The content of the thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class DiffNoteParams(BaseModel):
    base_sha: str = Field(description='Base commit SHA in the source branch.')
    head_sha: str = Field(description=
        'SHA referencing HEAD of this merge request.')
    start_sha: str = Field(description=
        'SHA referencing commit in target branch.')
    new_path: str = Field(description='File path after change.')
    old_path: str = Field(description='File path before change.')
    position_type: str = Field(description=
        'Type of the position reference. Allowed values: text or image.')
class TextDiffNoteParams(BaseModel):
    new_line: Optional[int] = Field(description=
        'For text diff notes, the line number after change.')
    old_line: Optional[int] = Field(description=
        'For text diff notes, the line number before change.')
class ImageDiffNoteParams(BaseModel):
    width: Optional[int] = Field(description=
        'For image diff notes, width of the image.')
    height: Optional[int] = Field(description=
        'For image diff notes, height of the image.')
    x: Optional[float] = Field(description=
        'For image diff notes, X coordinate.')
    y: Optional[float] = Field(description=
        'For image diff notes, Y coordinate.')
class MultilineCommentsParams(BaseModel):
    line_range: dict = Field(description=
        'Line range for a multi-line diff note.')
class CreateNewMergeRequestThread(BasicMergeRequestParams):
    position: DiffNoteParams = Field(description=
        'Position when creating a diff note.')
    text_position: Optional[TextDiffNoteParams] = Field(description=
        'Position parameters for text diff notes.')
    image_position: Optional[ImageDiffNoteParams] = Field(description=
        'Position parameters for image diff notes.')
    multiline_comments: Optional[MultilineCommentsParams] = Field(description
        ='Parameters for multiline comments.')
    commit_id: Optional[str] = Field(description=
        'SHA referencing commit to start this thread on.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class ResolveMergeRequestThread(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    discussion_id: str = Field(description='The ID of a thread.')
    resolved: bool = Field(description='Resolve or unresolve the discussion.')
class AddNoteToMergeRequestThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    discussion_id: str = Field(description='The ID of a thread.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class ModifyMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description=
        'The content of the note or reply. Exactly one of body or resolved must be set.'
        )
    resolved: Optional[bool] = Field(description=
        'Resolve or unresolve the note. Exactly one of body or resolved must be set.'
        )
class DeleteMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
class ListProjectCommitDiscussionItems(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
class GetSingleCommitDiscussionItem(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
class Position(BaseModel):
    base_sha: str = Field(description='SHA of the parent commit.')
    head_sha: str = Field(description=
        'The SHA of this commit. Same as commit_id.')
    start_sha: str = Field(description='SHA of the parent commit.')
    position_type: str = Field(description=
        'Type of the position reference. Allowed values: text or image.')
    hash: Optional[str] = Field(description=
        'Position when creating a diff note.')
    new_path: Optional[str] = Field(description='File path after change.')
    new_line: Optional[int] = Field(description='Line number after change.')
    old_path: Optional[str] = Field(description='File path before change.')
    old_line: Optional[int] = Field(description='Line number before change.')
    height: Optional[int] = Field(description=
        'For image diff notes, image height.')
    width: Optional[int] = Field(description=
        'For image diff notes, image width.')
    x: Optional[int] = Field(description='For image diff notes, X coordinate.')
    y: Optional[int] = Field(description='For image diff notes, Y coordinate.')
class CreateNewCommitThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    position: Position = Field(description=
        'Position when creating a diff note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class AddNoteToCommitThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyCommitThreadNote(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description='The content of a note.')
class DeleteCommitThreadNote(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    note_id: int = Field(description='The ID of a thread note.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_relations_export.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/snippets_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/branches.py
class ProjectsIdRepositoryBranches(BaseModel):
    id: int
    search: Optional[str] = None
    regex: Optional[str] = None
class ProjectsIdRepositoryBranchesBranchSingle(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryBranchesCreate(BaseModel):
    id: int
    branch: str
    ref: str
class ProjectsIdRepositoryBranchesBranch(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryMergedbranches(BaseModel):
    id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/metadata.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/version.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/protected_tags.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issue_boards_(group).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/repository_submodules.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/milestones_(group).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/members.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/protected_branches.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/commits.py
class ProjectsIdRepositoryCommits(BaseModel):
    id: int
    ref_name: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None
    path: Optional[str] = None
    author: Optional[str] = None
    all: Optional[bool]
    with_stats: Optional[bool]
    first_parent: Optional[bool]
    order: Optional[str]
    trailers: Optional[bool]
class ProjectsIdRepositoryCommitsSha(BaseModel):
    id: int
    sha: str
    stats: Optional[bool] = None
class ProjectsIdRepositoryCommitsShaRefs(BaseModel):
    id: int
    sha: str
    type: Optional[str] = None
class ProjectsIdRepositoryCommitsShaCherrypick(BaseModel):
    id: int
    sha: str
    branch: str
    dry_run: Optional[bool] = None
    message: Optional[str] = None
class ProjectsIdRepositoryCommitsShaRevert(BaseModel):
    id: int
    sha: str
    branch: str
    dry_run: Optional[bool] = None
class ProjectsIdRepositoryCommitsShaDiff(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaComments(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaCommentsPost(BaseModel):
    id: int
    sha: str
    note: str
    path: Optional[str] = None
    line: Optional[int] = None
    line_type: Optional[str] = None
class ProjectsIdRepositoryCommitsShaDiscussions(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaStatuses(BaseModel):
    id: int
    sha: str
    ref: Optional[str] = None
    stage: Optional[str] = None
    name: Optional[str] = None
    all: Optional[bool] = None
class ProjectsIdStatusesSha(BaseModel):
    id: int
    sha: str
    state: str
    ref: Optional[str] = None
    context: Optional[str] = None
    name: Optional[str] = None
    target_url: Optional[str] = None
    description: Optional[str] = None
    coverage: Optional[float] = None
    pipeline_id: Optional[int] = None
class ProjectsIdRepositoryCommitsShaMergerequests(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaSignature(BaseModel):
    id: int
    sha: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/application_appearance.py
class ApplicationAppearance(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    pwa_name: Optional[str] = None
    pwa_short_name: Optional[str] = None
    pwa_description: Optional[str] = None
    pwa_icon: Optional[Any] = None
    logo: Optional[Any] = None
    header_logo: Optional[Any] = None
    favicon: Optional[Any] = None
    new_project_guidelines: Optional[str] = None
    profile_image_guidelines: Optional[str] = None
    header_message: Optional[str] = None
    footer_message: Optional[str] = None
    message_background_color: Optional[str] = None
    message_font_color: Optional[str] = None
    email_header_and_footer_enabled: Optional[bool] = None
class ChangeLogo(BaseModel):
    logo: Any
    pwa_icon: Any

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/users.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_vulnerabilities.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/draft_notes.py
class ProjectsIdMergerequestsMergerequestiidDraftnotes(BaseModel):
    id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidSingle(
    BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesCreate(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    note: str
    commit_id: Optional[str] = None
    in_reply_to_discussion_id: Optional[int] = None
    resolve_discussion: Optional[bool] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidModify(
    BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
    note: Optional[str] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidDelete(
    BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidPublish(
    BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesBulkpublish(BaseModel):
    id: Union[int, str]
    merge_request_iid: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_migration_by_direct_transfer.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_iteration_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/agents_for_kubernetes.py
class ListTheAgentsForAProject(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
class GetDetailsAboutAnAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class RegisterAnAgentWithAProject(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    name: str = Field(description='Name for the agent')
class DeleteARegisteredAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class ListTokensForAnAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class GetSingleAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')
class CreateAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    name: int = Field(description='Name for the token')
    description: Optional[int] = Field(None, description=
        'Description for the token')
class RevokeAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_import_export.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_level_protected_environments.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/composer.py
class GroupIdPackagesComposerPackages(BaseModel):
    id: Union[int, str]
class GroupIdPackagesComposerPSha(BaseModel):
    id: Union[int, str]
    sha: str
class V1PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str
class V2PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
class CreateAPackageInput(BaseModel):
    id: Union[int, str]
    tag: Optional[str] = None
    branch: Optional[str] = None
class ProjectsIdPackagesComposerArchivesPackagename(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/alert_management.py
class ListMetricImages(BaseModel):
    id: int
    alert_iid: int
class UpdateMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int
    url: Optional[str] = None
    url_text: Optional[str] = None
class DeleteMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/sidekiq_queues.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/vulnerability_export.py
class SecurityProjectsIdVulnerabilityexports(BaseModel):
    id: Union[int, str]
class SecurityGroupsIdVulnerabilityexports(BaseModel):
    id: Union[int, str]
class SecurityVulnerabilityexportsId(BaseModel):
    id: Union[int, str]
class SecurityVulnerabilityexportsIdDownload(BaseModel):
    id: Union[int, str]

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/events.py
class Events(BaseModel):
    action: Optional[str] = None
    target_type: Optional[str] = None
    before: Optional[datetime] = Field(None, description=
        'Include only events created before a certain date.')
    after: Optional[datetime] = Field(None, description=
        'Include only events created after a particular date.')
    target_id: Optional[int] = None
    author_id: Optional[int] = None
    search: Optional[str] = None
class AuthenticatedUserEvents(Events):
    scope: Optional[str] = None
    sort: Optional[str] = None
class UserContributionEvents(Events):
    id: int
    sort: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
class ProjectVisibleEvents(Events):
    project_id: int
    sort: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_import_export.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dora4_metrics.py
class ProjectsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None
class GroupsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/plan_limits.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/statistics_(application).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_repository_storage_moves.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/iterations_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/applications.py
class Applications(BaseModel):
    name: str
    redirect_uri: str
    scopes: str
    confidential: Optional[bool] = None
class ApplicationsId(BaseModel):
    id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/saml.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dependency_proxy.py
class GroupsIdDependencyproxyCache(BaseModel):
    id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_relations_export.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/metrics_dashboard_annotations.py
class EnvironmentsIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str
class ClustersIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/personal_access_tokens.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/__init__.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/instance_level_ci_cd_variables.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/geo_sites.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/visual_review_discussions_deprecated.py
class PositionData(BaseModel):
    base_sha: str
    start_sha: str
    head_sha: str
    position_type: str
    new_path: Optional[str] = None
    new_line: Optional[int] = None
    old_path: Optional[str] = None
    old_line: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None
class CreateNewMergeRequestThread(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    body: str
    position: Optional[PositionData] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/feature_flags.py
class StrategyParameters(BaseModel):
    pass
class StrategyScope(BaseModel):
    environment_scope: Optional[str] = None
class Strategy(BaseModel):
    name: Optional[str] = None
    parameters: Optional[StrategyParameters] = None
    scopes: Optional[List[StrategyScope]] = None
class ListFeatureFlagsForProject(BaseModel):
    id: Union[int, str]
    scope: Optional[str] = None
class GetSingleFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
class CreateFeatureFlag(BaseModel):
    id: Union[int, str]
    name: str
    version: str
    description: Optional[str] = None
    active: Optional[bool] = None
    strategies: Optional[List[Strategy]] = None
class UpdateFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
    description: Optional[str] = None
    active: Optional[bool] = None
    name: Optional[str] = None
    strategies: Optional[List[Strategy]] = None
class DeleteFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pipelines_schedules.py
class GetAllPipelineSchedulesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    scope: Optional[str] = Field(None, description=
        'The scope of pipeline schedules, must be one of: active, inactive.')
class GetSinglePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class GetPipelinesTriggeredByScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class CreateNewPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    description: str = Field(..., description=
        'The description of the pipeline schedule.')
    ref: str = Field(..., description=
        'The branch or tag name that is triggered.')
    cron: str = Field(..., description=
        'The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description=
        'The time zone supported by ActiveSupport::TimeZone, for example: Pacific Time (US & Canada) (default: UTC).'
        )
    active: Optional[bool] = Field(None, description=
        'The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated (default: true).'
        )
class EditPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    description: Optional[str] = Field(None, description=
        'The description of the pipeline schedule.')
    ref: Optional[str] = Field(None, description=
        'The branch or tag name that is triggered.')
    cron: Optional[str] = Field(None, description=
        'The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description=
        'The time zone supported by ActiveSupport::TimeZone (for example Pacific Time (US & Canada)), or TZInfo::Timezone (for example America/Los_Angeles).'
        )
    active: Optional[bool] = Field(None, description=
        'The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated.'
        )
class TakeOwnershipOfPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class DeletePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class RunScheduledPipelineImmediatelyInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class CreatePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description=
        'The key of a variable; must have no more than 255 characters; only A-Z, a-z, 0-9, and _ are allowed.'
        )
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description=
        'The type of a variable. Available types are: env_var (default) and file.'
        )
class EditPipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description=
        'The type of a variable. Available types are: env_var (default) and file.'
        )
class DeletePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dockerfile_templates.py
class TemplatesDockerfilesKey(BaseModel):
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_releases.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/keys.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/packages.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/labels_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/freeze_periods.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/broadcast_messages.py
class GetASpecificBroadcastMessage(BaseModel):
    id: int
class CreateABroadcastMessage(BaseModel):
    message: str
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class UpdateABroadcastMessage(BaseModel):
    id: int
    message: Optional[str]
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class DeleteABroadcastMessage(BaseModel):
    id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/groups.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/wikis_project.py
class ProjectsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class ProjectsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class ProjectsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class ProjectsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class ProjectsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/npm.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/avatar.py
class Avatar(BaseModel):
    email: str
    size: Optional[int] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_group.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/error_tracking.py
class GetErrorTrackingSettings(BaseModel):
    id: Union[int, str]
class CreateErrorTrackingSettings(BaseModel):
    id: int
    active: bool
    integrated: bool
class EnableOrDisableTheErrorTrackingProjectSettings(BaseModel):
    id: int
    active: bool
    integrated: Optional[bool] = None
class ListProjectClientKeys(BaseModel):
    id: Union[int, str]
class CreateAClientKey(BaseModel):
    id: Union[int, str]
class DeleteAClientKey(BaseModel):
    id: Union[int, str]
    key_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/debian_project_distributions.py
class ListAllDebianDistributionsInAProject(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class SingleDebianProjectDistributionKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_label_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/repository_files.py
class ProjectIdRepositoryFiles(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    file_path: str = Field(description='URL encoded full path to new file')
    ref: str = Field(description='The name of branch, tag or commit')
class ProjectIdRepositoryFilesBlame(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    file_path: str = Field(description=
        'URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(description='The name of branch, tag or commit.')
    range_start: int = Field(description=
        'The first line of the range to blame.')
    range_end: int = Field(description='The last line of the range to blame.')
    range: Optional[dict] = Field(description='Blame range.')
class ProjectsIdRepositoryFilesFilepathRaw(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    file_path: str = Field(..., description=
        'URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(..., description=
        'The name of branch, tag or commit. Default is the HEAD of the project.'
        )
    lfs: Optional[bool] = Field(None, description=
        'Determines if the response should be Git LFS file contents, rather than the pointer. If the file is not tracked by Git LFS, ignored. Defaults to false.'
        )
class ProjectsIdRepositoryFilesFilepathCreate(BaseModel):
    branch: str = Field(description=
        'Name of the new branch to create. The commit is added to this branch.'
        )
    commit_message: str = Field(description='The commit message.')
    content: str = Field(description='The file’s content.')
    file_path: str = Field(description=
        'URL-encoded full path to new file. For example: lib%2Fclass%2Erb.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    author_email: Optional[str] = Field(None, description=
        'The commit author’s email address.')
    author_name: Optional[str] = Field(None, description=
        'The commit author’s name.')
    encoding: Optional[str] = Field(None, description=
        'Change encoding to base64. Default is text.')
    execute_filemode: Optional[bool] = Field(None, description=
        'Enables or disables the execute flag on the file. Can be true or false.'
        )
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathUpdate(BaseModel):
    branch: str
    commit_message: str
    content: str
    file_path: str
    id: Union[int, str]
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    encoding: Optional[str] = None
    execute_filemode: Optional[bool] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathDelete(BaseModel):
    branch: str
    commit_message: str
    file_path: str
    id: int
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositorySubmodulesSubmodule(BaseModel):
    id: int
    submodule: str
    branch: str
    commit_sha: str
    commit_message: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/nuget.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/container_registry.py
class ContainerRegistryAccessLevelEnum(str, Enum):
    enabled = 'enabled'
    private = 'private'
    disabled = 'disabled'
class ChangeContainerRegistryVisibility(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project accessible by the authenticated user.'
        )
    container_registry_access_level: Optional[ContainerRegistryAccessLevelEnum
        ] = Field(default=None, description=
        'The desired visibility of the Container Registry. One of enabled (default), private, or disabled.'
        )
class ListProjectRegistryRepositories(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
class GroupsIdRegistryRepositories(BaseModel):
    id: Union[int, str]
class RegistryRepositoriesId(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
    size: Optional[bool] = None
class ProjectsIdRegistryRepositoriesRepositoryid(BaseModel):
    id: Union[int, str]
    repository_id: int
class ProjectsIdRegistryRepositoriesRepositoryidTags(BaseModel):
    id: Union[int, str]
    repository_id: int
class GetDetailsOfARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteRegistryRepositoryTagsInBulk(BaseModel):
    id: Union[int, str]
    repository_id: int
    name_regex: Optional[str] = None
    name_regex_delete: str
    name_regex_keep: Optional[str] = None
    keep_n: Optional[int] = None
    older_than: Optional[str] = None
class ObtainTokenInput(BaseModel):
    CI_SERVER_URL: str = Field(description='CI server URL.')
    service: str = Field(default='container_registry', description=
        'The service type.')
    scope: str = Field(description='Scope for the token.')
class DeleteImageTagsByReferenceInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    CI_REGISTRY_IMAGE: str = Field(description='The registry image.')
    CI_COMMIT_SHORT_SHA: str = Field(description='The commit SHA.')
class ListAllContainerRepositoriesInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    admin_username: str = Field(description='The admin username.')
    admin_password: str = Field(description='The admin password.')
    service: str = Field(default='container_registry', description=
        'The service type.')
    scope: str = Field(default='registry:catalog:*', description=
        'Scope for the token.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_milestone_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/templates.py
class TemplatesGitignoresKey(BaseModel):
    key: str
class TemplatesGitlabciymlsKey(BaseModel):
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/jobs.py
class JobScope(str, Enum):
    created = 'created'
    pending = 'pending'
    running = 'running'
    failed = 'failed'
    success = 'success'
    canceled = 'canceled'
    skipped = 'skipped'
    waiting_for_resource = 'waiting_for_resource'
    manual = 'manual'
class ListProjectJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
class ListPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
    include_retried: Optional[bool] = Field(False, description=
        'Include retried jobs in the response.')
class ListPipelineTriggerJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
class GetAllowedAgentsInput(BaseModel):
    CI_JOB_TOKEN: str = Field(..., description=
        'Token value associated with the GitLab-provided CI_JOB_TOKEN variable.'
        )
class GetSingleJobInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='ID of a job.')
class JobInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='The ID of a job.')
class JobVariable(BaseModel):
    key: str = Field(..., description='The key of the job variable.')
    value: str = Field(..., description='The value of the job variable.')
class RunJobInput(JobInput):
    job_variables_attributes: Optional[List[JobVariable]] = Field(None,
        description=
        'An array containing the custom variables available to the job.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/gitignore.py
class ListAllGitignoreTemplates(BaseModel):
    pass
class GetSingleGitignoreTemplate(BaseModel):
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/releases.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/gitlab_ci_yaml.py
class ListAllCICDYamlTemplates(BaseModel):
    pass
class GetSingleCICDYamlTemplate(BaseModel):
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/milestones_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_activity_analytics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/job_artifacts.py
class GetJobArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int
    job_token: Optional[str] = None
class DownloadArtifacts(BaseModel):
    id: Union[int, str]
    ref_name: str
    job: str
    job_token: Optional[str] = None
class DownloadSingleArtifactByJobID(BaseModel):
    id: Union[int, str]
    job_id: int
    artifact_path: str
    job_token: Optional[str] = None
class DownloadSingleArtifactFromSpecificTag(BaseModel):
    id: Union[int, str]
    ref_name: str
    artifact_path: str
    job: str
    job_token: Optional[str] = None
class KeepArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issues_statistics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_statistics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/experiments.py
class ListAllExperiments(BaseModel):
    pass

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/scim.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/feature_flag_user_lists.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/vulnerability_findings.py
class ProjectsIdVulnerabilityfindings(BaseModel):
    id: int
    report_type: Optional[List[str]] = None
    scope: Optional[str] = None
    severity: Optional[List[str]] = None
    confidence: Optional[List[str]] = None
    pipeline_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/licenses_(templates).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/topics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/secrets.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/debian.py
class ProjectsIdPackagesDebianFilename(BaseModel):
    id: str
    file_name: str
    distribution: Optional[str] = None
    component: Optional[str] = None
class ProjectsIdPackagesDebianPoolDistributionLetterPackagenamePackageversionFilename(
    BaseModel):
    distribution: str
    letter: str
    package_name: str
    package_version: str
    file_name: str
class DownloadADistributionReleaseFile(BaseModel):
    distribution: str
class DownloadASignedDistributionReleaseFile(BaseModel):
    distribution: str
class DownloadAReleaseFileSignature(BaseModel):
    distribution: str
class DownloadAPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadAPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadADebianInstallerPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DowloadADebianInstallerPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadASourcePackagesIndex(BaseModel):
    distribution: str
    component: str
class DownloadASourcePackagesIndexByHash(BaseModel):
    distribution: str
    component: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/ruby_gems.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/markdown.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/debian_group_distributions.py
class ListAllDebianDistributionsInAGroup(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class GroupsIdDebiandistributionsCodenameKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/variables_project.py
class Variable(BaseModel):
    key: str
    value: str
    variable_type: Optional[str] = 'env_var'
    protected: Optional[bool] = False
    masked: Optional[bool] = False
    raw: Optional[bool] = False
    environment_scope: Optional[str] = '*'
    description: Optional[str] = None
class VariableFilter(BaseModel):
    environment_scope: Optional[str] = None
class GetProjectVariables(BaseModel):
    id: Union[int, str]
class GetVariable(BaseModel):
    id: Union[int, str]
    key: str
    filter: Optional[VariableFilter] = None
class CreateVariable(GetProjectVariables, Variable):
    pass
class UpdateVariable(GetVariable, Variable):
    pass
class DeleteVariable(GetVariable):
    pass

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/links_(epic).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/wikis_group.py
class GroupsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class GroupsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class GroupsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class GroupsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class GroupsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/audit_events.py
class Auditevents(BaseModel):
    created_after: Optional[str] = None
    created_before: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[int] = None
class AuditeventsId(BaseModel):
    id: int
class GroupsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class GroupsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int
class ProjectsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class ProjectsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_access_tokens.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/runners.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/environments.py
class ProjectsIdEnvironments(BaseModel):
    id: int
    name: Optional[str] = None
    search: Optional[str] = None
    states: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentid(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsCreate(BaseModel):
    id: int
    name: str
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentsid(BaseModel):
    id: int
    environment_id: int
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentidDelete(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsReviewapps(BaseModel):
    id: int
    before: Optional[datetime] = None
    limit: Optional[int] = None
    dry_run: Optional[bool] = None
class ProjectsIdEnvironmentsEnvironmentidStop(BaseModel):
    id: int
    environment_id: int
    force: Optional[bool] = None
class ProjectsIdEnvironmentsStopstale(BaseModel):
    id: int
    before: datetime

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_level_protected_branches.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/http_wrapper.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/gitlab_pages.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/marketplace.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/snippets.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/notes_(comments).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/terraform_registry.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/repositories.py
class ProjectsIdRepositoryTree(BaseModel):
    id: int
    page_token: Optional[str] = None
    pagination: Optional[str] = None
    path: Optional[str] = None
    per_page: Optional[str] = None
    recursive: bool = Field(False)
    ref: Optional[str] = None
class ProjectsIdRepositoryBlobsSha(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryBlobsShaRaw(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryArchive(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    path: Optional[str] = Field(None, description=
        'The subpath of the repository to download. Defaults to the whole repository.'
        )
    sha: Optional[str] = Field(None, description=
        'The commit SHA to download. A tag, branch reference, or SHA can be used. Defaults to the tip of the default branch.'
        )
    format: Optional[str] = Field(None, description=
        "The archive format. Options are: 'bz2', 'tar', 'tar.bz2', 'tar.gz', 'tb2', 'tbz', 'tbz2', 'zip'. Defaults to 'tar.gz'."
        )
class ProjectsIdRepositoryCompare(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    from_commit_or_branch: str = Field(..., alias='from', description=
        'The commit SHA or branch name.')
    to: str = Field(..., description='The commit SHA or branch name.')
    from_project_id: Optional[int] = Field(None, description=
        'The ID to compare from.')
    straight: Optional[bool] = Field(False, description=
        'Comparison method: true for direct comparison between from and to (from..to), false to compare using merge base (from…to)’. Default is false.'
        )
class ProjectsIdRepositoryContributors(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    order_by: Optional[str] = Field(None, description=
        'Return contributors ordered by name, email, or commits (orders by commit date) fields. Default is commits.'
        )
    sort: Optional[str] = Field(None, description=
        'Return contributors sorted in asc or desc order. Default is asc.')
class ProjectsIdRepositoryMergebase(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    refs: List[str] = Field(description=
        'The refs to find the common ancestor of. Accepts multiple refs.')
class ProjectsIdRepositoryChangelog(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    version: str = Field(description=
        'The version to generate the changelog for. The format must follow semantic versioning.'
        )
    branch: Optional[str] = Field(None, description=
        'The branch to commit the changelog changes to. Defaults to the project’s default branch.'
        )
    config_file: Optional[str] = Field(None, description=
        'Path to the changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.'
        )
    date: Optional[datetime] = Field(None, description=
        'The date and time of the release. Defaults to the current time.')
    file: Optional[str] = Field(None, description=
        'The file to commit the changes to. Defaults to CHANGELOG.md.')
    from_: Optional[str] = Field(None, alias='from', description=
        'The SHA of the commit that marks the beginning of the range of commits to include in the changelog. This commit isn’t included in the changelog.'
        )
    message: Optional[str] = Field(None, description=
        'The commit message to use when committing the changes. Defaults to Add changelog for version X, where X is the value of the version argument.'
        )
    to: Optional[str] = Field(None, description=
        'The SHA of the commit that marks the end of the range of commits to include in the changelog. This commit is included in the changelog. Defaults to the branch specified in the branch attribute. Limited to 15000 commits unless the feature flag changelog_commits_limitation is disabled.'
        )
    trailer: Optional[str] = Field(None, description=
        'The Git trailer to use for including commits. Defaults to Changelog. Case-sensitive: Example does not match example or eXaMpLE.'
        )
class GenerateChangelogData(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    version: str = Field(description=
        'The version to generate the changelog for. The format must follow semantic versioning.'
        )
    config_file: Optional[str] = Field(description=
        'The path of changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.'
        )
    date: Optional[datetime] = Field(description=
        'The date and time of the release. Uses ISO 8601 format. Defaults to the current time.'
        )
    from_: Optional[str] = Field(alias='from', description=
        'The start of the range of commits (as a SHA) to use for generating the changelog. This commit itself isn’t included in the list.'
        )
    to: Optional[str] = Field(description=
        'The end of the range of commits (as a SHA) to use for the changelog. This commit is included in the list. Defaults to the HEAD of the default project branch.'
        )
    trailer: Optional[str] = Field(description=
        'The Git trailer to use for including commits. Defaults to Changelog.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/deployments.py
class ListProjectDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class GetASpecificDeployment(BaseModel):
    id: int
    deployment_id: int
class GetDeploymentFrequency(BaseModel):
    id: int
    finished_after: Optional[datetime] = None
class DeploymentDuration(BaseModel):
    created_at: datetime
    finished_at: datetime
class ListProjectDeployment(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsCreate(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsDeploymentid(BaseModel):
    id: int
    deployment_id: int
class CreateADeployment(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeploymentsDeploymentidUpdate(BaseModel):
    id: int
    deployment_id: int
    status: str
class ProjectsIdDeploymentsDeploymentidDelete(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidMergerequests(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidApproval(BaseModel):
    id: int
    deployment_id: int
    status: str
    comment: Optional[str] = None
    represented_as: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/snippet_repository_storage_moves.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/notification_settings.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/iterations_(group).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/search.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_aliases.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/http_wrapper_privatetoken.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_badges.py
class GroupsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class GroupsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesAdd(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class GroupsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class GroupsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/external_status_checks.py
class ProjectsIdExternalstatuschecks(BaseModel):
    id: Union[int, str] = Field(description='ID of a project')
class CreateUpdateExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    name: Optional[str] = Field(description=
        'Display name of external status check service')
    external_url: Optional[str] = Field(description=
        'URL of external status check service')
    protected_branch_ids: Optional[List[int]] = Field(description=
        'IDs of protected branches to scope the rule by')
class UpdateExternalStatusCheckService(BaseModel):
    id: Union[int, str]
    check_id: int
    name: Optional[str] = None
    external_url: Optional[str] = None
    protected_branch_ids: Optional[List[int]] = None
class DeleteExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    check_id: int = Field(description='ID of an external status check service')
class MergeRequestStatusChecks(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
class SetStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    sha: str = Field(description='SHA at HEAD of the source branch')
    external_status_check_id: int = Field(description=
        'ID of an external status check')
    status: Optional[str] = Field(description=
        'Set to passed to pass the check or failed to fail it')
class RetryFailedStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    external_status_check_id: int = Field(description=
        'ID of a failed external status check')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/access_requests.py
class ProjectsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class ProjectsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class GroupsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int
class ProjectsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_templates.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/sidekiq_metrics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_level_protected_environments.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/invitations.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/go_proxy.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/license.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_repository_storage_moves.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/merge_trains.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/vulnerabilities.py
class VulnerabilitiesId(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdConfirm(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdResolve(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdDismiss(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdRevert(BaseModel):
    id: Union[int, str]

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/variables_group.py
class ListGroupVariables(BaseModel):
    id: Union[int, str]
class VariableType(str, Enum):
    env_var = 'env_var'
    file = 'file'
class ShowGroupVariableDetails(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
class CreateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class UpdateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class RemoveGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pypi.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/maven.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_access_tokens.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/projects.py
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
    custom_attributes: Optional[Dict[str, str]] = Field(None, description=
        'A dictionary of custom attributes to filter by')
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
class CreateProjectRequest(BaseModel):
    name: Optional[str] = Field(None, description=
        'The name of the new project. Equals path if not provided.')
    path: Optional[str] = Field(None, description=
        'Repository name for new project. Generated based on name if not provided (generated as lowercase with dashes). Starting with GitLab 14.9, path must not start or end with a special character and must not contain consecutive special characters.'
        )
    allow_merge_on_skipped_pipeline: Optional[bool] = Field(None,
        description=
        'Set whether or not merge requests can be merged with skipped jobs.')
    only_allow_merge_if_all_status_checks_passed: Optional[bool] = Field(None,
        description=
        'Indicates that merges of merge requests should be blocked unless all status checks have passed. Defaults to false. Introduced in GitLab 15.5 with feature flag only_allow_merge_if_all_status_checks_passed disabled by default.'
        )
    analytics_access_level: Optional[str] = Field(None, description=
        'One of disabled, private or enabled.')
    approvals_before_merge: Optional[int] = Field(None, description=
        'How many approvers should approve merge requests by default. To configure approval rules, see Merge request approvals API. Deprecated in GitLab 16.0.'
        )
    auto_cancel_pending_pipelines: Optional[str] = Field(None, description=
        'Auto-cancel pending pipelines. This action toggles between an enabled state and a disabled state; it is not a boolean.'
        )
    auto_devops_deploy_strategy: Optional[str] = Field(None, description=
        'Auto Deploy strategy (continuous, manual or timed_incremental).')
    auto_devops_enabled: Optional[bool] = Field(None, description=
        'Enable Auto DevOps for this project.')
    autoclose_referenced_issues: Optional[bool] = Field(None, description=
        'Set whether auto-closing referenced issues on default branch.')
    avatar: Optional[Union[str, Any]] = Field(None, description=
        'Image file for avatar of the project.')
    build_git_strategy: Optional[str] = Field(None, description=
        'The Git strategy. Defaults to fetch.')
    build_timeout: Optional[int] = Field(None, description=
        'The maximum amount of time, in seconds, that a job can run.')
    builds_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    ci_config_path: Optional[str] = Field(None, description=
        'The path to CI configuration file.')
    container_expiration_policy_attributes: Optional[dict] = Field(None,
        description='Update the image cleanup policy for this project.')
    container_registry_access_level: Optional[str] = Field(None,
        description=
        'Set visibility of container registry, for this project, to one of disabled, private or enabled.'
        )
    container_registry_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable container registry for this project. Use container_registry_access_level instead.'
        )
    default_branch: Optional[str] = Field(None, description=
        'The default branch name. Requires initialize_with_readme to be true.')
    description: Optional[str] = Field(None, description=
        'Short project description.')
    emails_disabled: Optional[bool] = Field(None, description=
        'Disable email notifications.')
    external_authorization_classification_label: Optional[str] = Field(None,
        description='The classification label for the project.')
    forking_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    group_with_project_templates_id: Optional[int] = Field(None,
        description=
        'For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true.'
        )
    import_url: Optional[str] = Field(None, description=
        'URL to import repository from. When the URL value isn’t empty, you must not set initialize_with_readme to true. Doing so might result in the following error: not a git repository.'
        )
    initialize_with_readme: Optional[bool] = Field(None, description=
        'Whether to create a Git repository with just a README.md file. Default is false.'
        )
    issues_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    issues_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable issues for this project. Use issues_access_level instead.'
        )
    jobs_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable jobs for this project. Use builds_access_level instead.'
        )
    lfs_enabled: Optional[bool] = Field(None, description='Enable LFS.')
    merge_method: Optional[str] = Field(None, description=
        'Set the merge method used.')
    merge_pipelines_enabled: Optional[bool] = Field(None, description=
        'Enable or disable merge pipelines.')
    merge_requests_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    merge_requests_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable merge requests for this project. Use merge_requests_access_level instead.'
        )
    merge_trains_enabled: Optional[bool] = Field(None, description=
        'Enable or disable merge trains.')
    mirror_trigger_builds: Optional[bool] = Field(None, description=
        'Pull mirroring triggers builds.')
    mirror: Optional[bool] = Field(None, description=
        'Enables pull mirroring in a project.')
    namespace_id: Optional[int] = Field(None, description=
        'Namespace for the new project (defaults to the current user’s namespace).'
        )
    only_allow_merge_if_all_discussions_are_resolved: Optional[bool] = Field(
        None, description=
        'Set whether merge requests can only be merged when all the discussions are resolved.'
        )
    only_allow_merge_if_pipeline_succeeds: Optional[bool] = Field(None,
        description=
        'Set whether merge requests can only be merged with successful pipelines.'
        )
    packages_enabled: Optional[bool] = Field(None, description=
        'Enable or disable packages repository feature.')
    pages_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, enabled, or public.')
    printing_merge_request_link_enabled: Optional[bool] = Field(None,
        description=
        'Show link to create/view merge request when pushing from the command line.'
        )
    public_builds: Optional[bool] = Field(None, description=
        'If true, jobs can be viewed by non-project members.')
    releases_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    environments_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    feature_flags_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    infrastructure_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    monitor_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    remove_source_branch_after_merge: Optional[bool] = Field(None,
        description=
        'Enable Delete source branch option by default for all new merge requests.'
        )
    repository_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    repository_storage: Optional[str] = Field(None, description=
        'Which storage shard the repository is on. (administrator only)')
    request_access_enabled: Optional[bool] = Field(None, description=
        'Allow users to request member access.')
    requirements_access_level: Optional[str] = Field(None, description=
        'One of disabled, private or enabled')
    resolve_outdated_diff_discussions: Optional[bool] = Field(None,
        description=
        'Automatically resolve merge request diffs discussions on lines changed with a push.'
        )
    security_and_compliance_access_level: Optional[str] = Field(None,
        description=
        '(GitLab 14.9 and later) Security and compliance access level. One of disabled, private, or enabled.'
        )
    shared_runners_enabled: Optional[bool] = Field(None, description=
        'Enable shared runners for this project.')
    group_runners_enabled: Optional[bool] = Field(None, description=
        'Enable group runners for this project.')
    snippets_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    snippets_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable snippets for this project. Use snippets_access_level instead.'
        )
    squash_option: Optional[str] = Field(None, description=
        'One of never, always, default_on, or default_off.')
    tag_list: Optional[list] = Field(None, description=
        '(Deprecated in GitLab 14.0) The list of tags for a project; put array of tags, that should be finally assigned to a project. Use topics instead.'
        )
    template_name: Optional[str] = Field(None, description=
        'When used without use_custom_template, name of a built-in project template.'
        )
    template_project_id: Optional[int] = Field(None, description=
        'When used with use_custom_template, project ID of a custom project template.'
        )
    topics: Optional[list] = Field(None, description=
        'The list of topics for a project; put array of topics, that should be finally assigned to a project. (Introduced in GitLab 14.0.)'
        )
    use_custom_template: Optional[bool] = Field(None, description=
        'Use either custom instance or group (with group_with_project_templates_id) project template.'
        )
    visibility: Optional[str] = Field(None, description=
        'See project visibility level.')
    wiki_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    wiki_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable wiki for this project. Use wiki_access_level instead.'
        )
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
    container_expiration_policy_attributes: Optional[
        ContainerExpirationPolicyAttributes] = None
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

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/merge_requests.py
class ProjectsMergeRequestCreate(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    source_branch: str = Field(description='The source branch name.')
    target_branch: str = Field(description='The target branch name.')
    title: str = Field(description='The title of merge request.')
    allow_collaboration: Optional[bool] = Field(None, description=
        'Allow commits from members who can merge to the target branch.')
    approvals_before_merge: Optional[int] = Field(None, description=
        'The amount of approvals required before merging.')
    allow_maintainer_to_push: Optional[bool] = Field(None, description=
        'Allow users who can merge to the target branch to push to the source branch.'
        )
    assignee_id: Optional[int] = Field(None, description=
        'The ID of a user to assign merge request.')
    assignee_ids: Optional[List[int]] = Field(None, description=
        'The IDs of users to assign merge request.')
    description: Optional[str] = Field(None, description=
        'The description of merge request.')
    labels: Optional[str] = Field(None, description=
        'Comma-separated list of label names.')
    milestone_id: Optional[int] = Field(None, description=
        'The global ID of a milestone to assign merge request.')
    remove_source_branch: Optional[bool] = Field(None, description=
        'Flag indicating if a merge request should remove the source branch when merging.'
        )
    reviewer_ids: Optional[List[int]] = Field(None, description=
        'The IDs of users to request review from when merge request created.')
    squash: Optional[bool] = Field(None, description=
        'Squash commits into a single commit when merging.')
    squash_on_merge: Optional[bool] = Field(None, description=
        'Squash commits into a single commit after merging.')
    target_project_id: Optional[int] = Field(None, description=
        'The target project ID. If the user is a maintainer of the target project, the source project is set as the target_project_id.'
        )

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/member_roles.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_weight_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/search_migrations.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/integrations.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/emoji_reactions.py
class AwardEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
class SingleEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class NewEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    name: str
class DeleteEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class ListCommentEmojiReactionsParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
class GetCommentEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int
class AwardCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    name: str
class DeleteCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/settings_(application).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pipelines.py
class Scope(str, Enum):
    running = 'running'
    pending = 'pending'
    finished = 'finished'
    branches = 'branches'
    tags = 'tags'
class Status(str, Enum):
    created = 'created'
    waiting_for_resource = 'waiting_for_resource'
    preparing = 'preparing'
    pending = 'pending'
    running = 'running'
    success = 'success'
    failed = 'failed'
    canceled = 'canceled'
    skipped = 'skipped'
    manual = 'manual'
    scheduled = 'scheduled'
class Source(str, Enum):
    push = 'push'
    web = 'web'
    trigger = 'trigger'
    schedule = 'schedule'
    api = 'api'
    external = 'external'
    pipeline = 'pipeline'
    chat = 'chat'
    webide = 'webide'
    merge_request_event = 'merge_request_event'
    external_pull_request_event = 'external_pull_request_event'
    parent_pipeline = 'parent_pipeline'
    ondemand_dast_scan = 'ondemand_dast_scan'
    ondemand_dast_validation = 'ondemand_dast_validation'
class OrderBy(str, Enum):
    id = 'id'
    status = 'status'
    ref = 'ref'
    updated_at = 'updated_at'
    user_id = 'user_id'
class Sort(str, Enum):
    asc = 'asc'
    desc = 'desc'
class ListProjectPipelinesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    scope: Optional[Scope]
    status: Optional[Status]
    source: Optional[Source]
    ref: Optional[str]
    sha: Optional[str]
    yaml_errors: Optional[bool]
    username: Optional[str]
    updated_after: Optional[datetime]
    updated_before: Optional[datetime]
    name: Optional[str]
    order_by: Optional[OrderBy]
    sort: Optional[Sort]
class GetPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineVariablesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportSummaryInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetLatestPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    ref: Optional[str] = Field(None, description=
        'The branch or tag to check for the latest pipeline. Defaults to the default branch when not specified.'
        )
class CreatePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    ref: str = Field(..., description=
        'The branch or tag to run the pipeline on.')
    variables: Optional[List[Dict[str, Union[str, Dict[str, str]]]]] = Field(
        None, description=
        'An array of hashes containing the variables available in the pipeline.'
        )
class RetryJobsInPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class CancelPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class DeletePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/lint_.gitlab_ci.yml.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/service_data.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dependencies.py
class ProjectsIdDependencies(BaseModel):
    id: Union[int, str]
    package_manager: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_badges.py
class ProjectsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class ProjectsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesCreate(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/helm.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/namespaces.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/links_(issue).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/deploy_keys.py
class Deploykeys(BaseModel):
    public: Optional[bool] = None
class ProjectsIdDeploykeys(BaseModel):
    id: int
class UsersIdorusernameProjectdeploykeys(BaseModel):
    id_or_username: str
class ProjectsIdDeploykeysKeyidSingle(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysAdd(BaseModel):
    id: int
    key: str
    title: str
    can_push: Optional[bool] = None
    expires_at: Optional[datetime] = None
class ProjectsIdDeploykeysKeyidUpdate(BaseModel):
    id: int
    can_push: Optional[bool] = None
    title: Optional[str] = None
class ProjectsIdDeploykeysKeyidDelete(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysKeyidEnable(BaseModel):
    id: int
    key_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issue_boards_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/job_token_scopes.py
class GetProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
class PatchProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
    enabled: bool
class GetProjectCICDJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
class CreateNewProjectToJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int
class RemoveProjectFromJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/merge_request_context_commits.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/system_hooks.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/user_starred_metrics_dashboards.py
class ProjectsIdMetricsUserstarreddashboardsAdd(BaseModel):
    id: Union[int, str]
    dashboard_path: str
class ProjectsIdMetricsUserstarreddashboardsRemove(BaseModel):
    id: Union[int, str]
    dashboard_path: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/secure_files.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issues.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/labels_(group).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/tags.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/release_links.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/import.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pages_domains.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pipeline_triggers.py
class ListProjectTriggerTokensInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
class GetTriggerTokenDetailsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class CreateTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    description: str = Field(..., description='The trigger name.')
class UpdateProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
    description: Optional[str] = Field(None, description='The trigger name.')
class RemoveProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class TriggerPipelineWithTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    ref: str = Field(..., description=
        'The branch or tag to run the pipeline on.')
    token: str = Field(..., description='The trigger token or CI/CD job token.'
        )
    variables: Optional[Dict[str, str]] = Field(None, description=
        'A map of key-valued strings containing the pipeline variables.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/linked_epics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_state_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_remote_mirrors.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/to_do_lists.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/deploy_tokens.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dashboard_annotations.py
class CreateNewAnnotation(BaseModel):
    id: Union[int, str]
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str] = None
    description: str

    @validator('starting_at', 'ending_at', pre=True)
    def parse_iso8601(cls, v):
        if v is None:
            return v
        try:
            return datetime.fromisoformat(v)
        except ValueError:
            raise ValueError('datetime is not in ISO 8601 format')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/geo_nodes.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/merge_request_approvals.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/conan.py
class RoutePrefix(str, Enum):
    instance_level = '/packages/conan/v1'
    project_level = '/projects/:id/packages/conan/v1`'
class Ping(BaseModel):
    route_prefix: RoutePrefix = Field(description=
        'pick either instance_level or project_level')
class SearchInput(BaseModel):
    route_prefix: RoutePrefix
    q: str = Field(..., description=
        'Search query. You can use * as a wildcard.')
class AuthenticateInput(BaseModel):
    route_prefix: RoutePrefix
class CheckCredentialsInput(BaseModel):
    route_prefix: RoutePrefix
class RecipeSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifest(BaseModel):
    package_name: str = Field(description='Name of a package.')
    package_version: str = Field(description='Version of a package.')
    package_username: str = Field(description=
        'Conan username of a package. This attribute is the +-separated full path of your project.'
        )
    package_channel: str = Field(description='Channel of a package.')
class PackageManifest(RecipeManifest):
    conan_package_reference: str = Field(description=
        'Reference hash of a Conan package. Conan generates this value.')
class UploadUrls(RecipeManifest):
    files: Dict[str, int] = Field(description=
        'Dictionary of file names with their sizes.')
class PackageUploadUrlsInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
    file_sizes: Dict[str, int]
class DownloadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
class UploadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
    file_content: str
class DownloadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
class UploadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
    file_content: str
class DeletePackageInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/custom_attributes.py
class UsersIdCustomattributes(BaseModel):
    id: int
class GroupsIdCustomattributes(BaseModel):
    id: int
class ProjectsIdCustomattributes(BaseModel):
    id: int
class UsersIdCustomattributesKey(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class UsersIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class GroupsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class ProjectsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class UsersIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/epics.py
class NotMatch(BaseModel):
    author_id: Optional[int] = Field(None, description=
        'Can exclude by author ID')
    author_username: Optional[str] = Field(None, description=
        'Can exclude by author username (GitLab 14.7 and later)')
    labels: Optional[str] = Field(None, description='Can exclude by labels')
class GroupsIdEpics(BaseModel):
    id: Union[int, str]
    author_id: Optional[int] = None
    author_username: Optional[str] = None
    labels: Optional[str] = None
    with_labels_details: Optional[bool] = None
    order_by: Optional[str] = None
    sort: Optional[str] = None
    search: Optional[str] = None
    state: Optional[str] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    include_ancestor_groups: Optional[bool] = None
    include_descendant_groups: Optional[bool] = None
    my_reaction_emoji: Optional[str] = None
    not_: Optional[NotMatch] = Field(None, alias='not', description=
        'Return epics that do not match the parameters supplied')
class SingleEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class NewEpicInput(BaseModel):
    id: Union[int, str]
    title: str
    labels: Optional[str]
    description: Optional[str]
    color: Optional[str]
    confidential: Optional[bool]
    created_at: Optional[datetime]
    start_date_is_fixed: Optional[bool]
    start_date_fixed: Optional[str]
    due_date_is_fixed: Optional[bool]
    due_date_fixed: Optional[str]
    parent_id: Optional[Union[int, str]]
class UpdateEpic(BaseModel):
    id: int
    epic_iid: int
    add_labels: Optional[str] = None
    confidential: Optional[bool] = None
    description: Optional[str] = None
    due_date_fixed: Optional[str] = None
    due_date_is_fixed: Optional[bool] = None
    labels: Optional[str] = None
    parent_id: Optional[int] = None
    remove_labels: Optional[str] = None
    start_date_fixed: Optional[str] = None
    start_date_is_fixed: Optional[bool] = None
    state_event: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
class DeleteEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class CreateAToDoItem(BaseModel):
    id: Union[int, str]
    epic_iid: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issues_(epic).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/suggestions.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/product_analytics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/discussions.py
class ListProjectIssueDiscussionItems(BaseModel):
    id: Union[int, str]
    issue_iid: int
class GetSingleIssueDiscussionItem(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
class CreateNewIssueThread(BaseModel):
    body: str
    id: Union[int, str]
    issue_iid: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingIssueThreadPayload(BaseModel):
    body: str = Field(..., description='The content of the note or reply.')
    discussion_id: int = Field(..., description='The ID of a thread.')
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    issue_iid: int = Field(..., description='The IID of an issue.')
    note_id: int = Field(..., description='The ID of a thread note.')
    created_at: Optional[datetime] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyExistingIssueThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    issue_iid: int
    note_id: int
class DeleteIssueThreadNote(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
    note_id: int
class ProjectsIdSnippetsSnippetidDiscussions(BaseModel):
    id: Union[int, str]
    snippet_id: int
class ListProjectSnippetDiscussionItems(BaseModel):
    id: Union[int, str]
    snippet_id: int
class GetSingleSnippetDiscussionItem(BaseModel):
    id: Union[int, str]
    snippet_id: int
    discussion_id: int
class CreateNewSnippetThread(BaseModel):
    body: str
    id: Union[int, str]
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingSnippetThread(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class ModifyExistingSnippetThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class DeleteSnippetThreadNote(BaseModel):
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class GroupsIdEpicsEpicidDiscussions(BaseModel):
    epic_id: int
    id: Union[int, str]
class SingleEpicDiscussionItem(BaseModel):
    discussion_id: int = Field(description='The ID of a discussion item.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
class CreateNewEpicThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    created_at: Optional[Union[str, datetime]] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class AddNoteToEpicThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[Union[str, datetime]] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyEpicThreadNote(BaseModel):
    body: str = Field(description='The content of note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class DeleteEpicThreadNote(BaseModel):
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class ListMergeRequestDiscussionItems(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class SingleMergeRequestDiscussionItem(BaseModel):
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class BasicMergeRequestParams(BaseModel):
    body: str = Field(description='The content of the thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class DiffNoteParams(BaseModel):
    base_sha: str = Field(description='Base commit SHA in the source branch.')
    head_sha: str = Field(description=
        'SHA referencing HEAD of this merge request.')
    start_sha: str = Field(description=
        'SHA referencing commit in target branch.')
    new_path: str = Field(description='File path after change.')
    old_path: str = Field(description='File path before change.')
    position_type: str = Field(description=
        'Type of the position reference. Allowed values: text or image.')
class TextDiffNoteParams(BaseModel):
    new_line: Optional[int] = Field(description=
        'For text diff notes, the line number after change.')
    old_line: Optional[int] = Field(description=
        'For text diff notes, the line number before change.')
class ImageDiffNoteParams(BaseModel):
    width: Optional[int] = Field(description=
        'For image diff notes, width of the image.')
    height: Optional[int] = Field(description=
        'For image diff notes, height of the image.')
    x: Optional[float] = Field(description=
        'For image diff notes, X coordinate.')
    y: Optional[float] = Field(description=
        'For image diff notes, Y coordinate.')
class MultilineCommentsParams(BaseModel):
    line_range: dict = Field(description=
        'Line range for a multi-line diff note.')
class CreateNewMergeRequestThread(BasicMergeRequestParams):
    position: DiffNoteParams = Field(description=
        'Position when creating a diff note.')
    text_position: Optional[TextDiffNoteParams] = Field(description=
        'Position parameters for text diff notes.')
    image_position: Optional[ImageDiffNoteParams] = Field(description=
        'Position parameters for image diff notes.')
    multiline_comments: Optional[MultilineCommentsParams] = Field(description
        ='Parameters for multiline comments.')
    commit_id: Optional[str] = Field(description=
        'SHA referencing commit to start this thread on.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class ResolveMergeRequestThread(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    discussion_id: str = Field(description='The ID of a thread.')
    resolved: bool = Field(description='Resolve or unresolve the discussion.')
class AddNoteToMergeRequestThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    discussion_id: str = Field(description='The ID of a thread.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class ModifyMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description=
        'The content of the note or reply. Exactly one of body or resolved must be set.'
        )
    resolved: Optional[bool] = Field(description=
        'Resolve or unresolve the note. Exactly one of body or resolved must be set.'
        )
class DeleteMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
class ListProjectCommitDiscussionItems(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
class GetSingleCommitDiscussionItem(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
class Position(BaseModel):
    base_sha: str = Field(description='SHA of the parent commit.')
    head_sha: str = Field(description=
        'The SHA of this commit. Same as commit_id.')
    start_sha: str = Field(description='SHA of the parent commit.')
    position_type: str = Field(description=
        'Type of the position reference. Allowed values: text or image.')
    hash: Optional[str] = Field(description=
        'Position when creating a diff note.')
    new_path: Optional[str] = Field(description='File path after change.')
    new_line: Optional[int] = Field(description='Line number after change.')
    old_path: Optional[str] = Field(description='File path before change.')
    old_line: Optional[int] = Field(description='Line number before change.')
    height: Optional[int] = Field(description=
        'For image diff notes, image height.')
    width: Optional[int] = Field(description=
        'For image diff notes, image width.')
    x: Optional[int] = Field(description='For image diff notes, X coordinate.')
    y: Optional[int] = Field(description='For image diff notes, Y coordinate.')
class CreateNewCommitThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    position: Position = Field(description=
        'Position when creating a diff note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class AddNoteToCommitThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyCommitThreadNote(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description='The content of a note.')
class DeleteCommitThreadNote(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    note_id: int = Field(description='The ID of a thread note.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_relations_export.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/snippets_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/branches.py
class ProjectsIdRepositoryBranches(BaseModel):
    id: int
    search: Optional[str] = None
    regex: Optional[str] = None
class ProjectsIdRepositoryBranchesBranchSingle(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryBranchesCreate(BaseModel):
    id: int
    branch: str
    ref: str
class ProjectsIdRepositoryBranchesBranch(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryMergedbranches(BaseModel):
    id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/metadata.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/version.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/protected_tags.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issue_boards_(group).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/repository_submodules.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/milestones_(group).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/members.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/protected_branches.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/commits.py
class ProjectsIdRepositoryCommits(BaseModel):
    id: int
    ref_name: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None
    path: Optional[str] = None
    author: Optional[str] = None
    all: Optional[bool]
    with_stats: Optional[bool]
    first_parent: Optional[bool]
    order: Optional[str]
    trailers: Optional[bool]
class ProjectsIdRepositoryCommitsSha(BaseModel):
    id: int
    sha: str
    stats: Optional[bool] = None
class ProjectsIdRepositoryCommitsShaRefs(BaseModel):
    id: int
    sha: str
    type: Optional[str] = None
class ProjectsIdRepositoryCommitsShaCherrypick(BaseModel):
    id: int
    sha: str
    branch: str
    dry_run: Optional[bool] = None
    message: Optional[str] = None
class ProjectsIdRepositoryCommitsShaRevert(BaseModel):
    id: int
    sha: str
    branch: str
    dry_run: Optional[bool] = None
class ProjectsIdRepositoryCommitsShaDiff(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaComments(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaCommentsPost(BaseModel):
    id: int
    sha: str
    note: str
    path: Optional[str] = None
    line: Optional[int] = None
    line_type: Optional[str] = None
class ProjectsIdRepositoryCommitsShaDiscussions(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaStatuses(BaseModel):
    id: int
    sha: str
    ref: Optional[str] = None
    stage: Optional[str] = None
    name: Optional[str] = None
    all: Optional[bool] = None
class ProjectsIdStatusesSha(BaseModel):
    id: int
    sha: str
    state: str
    ref: Optional[str] = None
    context: Optional[str] = None
    name: Optional[str] = None
    target_url: Optional[str] = None
    description: Optional[str] = None
    coverage: Optional[float] = None
    pipeline_id: Optional[int] = None
class ProjectsIdRepositoryCommitsShaMergerequests(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaSignature(BaseModel):
    id: int
    sha: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/application_appearance.py
class ApplicationAppearance(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    pwa_name: Optional[str] = None
    pwa_short_name: Optional[str] = None
    pwa_description: Optional[str] = None
    pwa_icon: Optional[Any] = None
    logo: Optional[Any] = None
    header_logo: Optional[Any] = None
    favicon: Optional[Any] = None
    new_project_guidelines: Optional[str] = None
    profile_image_guidelines: Optional[str] = None
    header_message: Optional[str] = None
    footer_message: Optional[str] = None
    message_background_color: Optional[str] = None
    message_font_color: Optional[str] = None
    email_header_and_footer_enabled: Optional[bool] = None
class ChangeLogo(BaseModel):
    logo: Any
    pwa_icon: Any

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/users.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_vulnerabilities.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/draft_notes.py
class ProjectsIdMergerequestsMergerequestiidDraftnotes(BaseModel):
    id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidSingle(
    BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesCreate(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    note: str
    commit_id: Optional[str] = None
    in_reply_to_discussion_id: Optional[int] = None
    resolve_discussion: Optional[bool] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidModify(
    BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
    note: Optional[str] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidDelete(
    BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidPublish(
    BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesBulkpublish(BaseModel):
    id: Union[int, str]
    merge_request_iid: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_migration_by_direct_transfer.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_iteration_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/agents_for_kubernetes.py
class ListTheAgentsForAProject(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
class GetDetailsAboutAnAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class RegisterAnAgentWithAProject(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    name: str = Field(description='Name for the agent')
class DeleteARegisteredAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class ListTokensForAnAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class GetSingleAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')
class CreateAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    name: int = Field(description='Name for the token')
    description: Optional[int] = Field(None, description=
        'Description for the token')
class RevokeAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_import_export.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_level_protected_environments.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/composer.py
class GroupIdPackagesComposerPackages(BaseModel):
    id: Union[int, str]
class GroupIdPackagesComposerPSha(BaseModel):
    id: Union[int, str]
    sha: str
class V1PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str
class V2PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
class CreateAPackageInput(BaseModel):
    id: Union[int, str]
    tag: Optional[str] = None
    branch: Optional[str] = None
class ProjectsIdPackagesComposerArchivesPackagename(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/alert_management.py
class ListMetricImages(BaseModel):
    id: int
    alert_iid: int
class UpdateMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int
    url: Optional[str] = None
    url_text: Optional[str] = None
class DeleteMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/sidekiq_queues.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/vulnerability_export.py
class SecurityProjectsIdVulnerabilityexports(BaseModel):
    id: Union[int, str]
class SecurityGroupsIdVulnerabilityexports(BaseModel):
    id: Union[int, str]
class SecurityVulnerabilityexportsId(BaseModel):
    id: Union[int, str]
class SecurityVulnerabilityexportsIdDownload(BaseModel):
    id: Union[int, str]

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/events.py
class Events(BaseModel):
    action: Optional[str] = None
    target_type: Optional[str] = None
    before: Optional[datetime] = Field(None, description=
        'Include only events created before a certain date.')
    after: Optional[datetime] = Field(None, description=
        'Include only events created after a particular date.')
    target_id: Optional[int] = None
    author_id: Optional[int] = None
    search: Optional[str] = None
class AuthenticatedUserEvents(Events):
    scope: Optional[str] = None
    sort: Optional[str] = None
class UserContributionEvents(Events):
    id: int
    sort: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
class ProjectVisibleEvents(Events):
    project_id: int
    sort: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_import_export.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dora4_metrics.py
class ProjectsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None
class GroupsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/plan_limits.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/statistics_(application).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_repository_storage_moves.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/iterations_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/applications.py
class Applications(BaseModel):
    name: str
    redirect_uri: str
    scopes: str
    confidential: Optional[bool] = None
class ApplicationsId(BaseModel):
    id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/saml.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dependency_proxy.py
class GroupsIdDependencyproxyCache(BaseModel):
    id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_relations_export.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/metrics_dashboard_annotations.py
class EnvironmentsIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str
class ClustersIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/personal_access_tokens.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/__init__.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/instance_level_ci_cd_variables.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/geo_sites.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/visual_review_discussions_deprecated.py
class PositionData(BaseModel):
    base_sha: str
    start_sha: str
    head_sha: str
    position_type: str
    new_path: Optional[str] = None
    new_line: Optional[int] = None
    old_path: Optional[str] = None
    old_line: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None
class CreateNewMergeRequestThread(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    body: str
    position: Optional[PositionData] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/feature_flags.py
class StrategyParameters(BaseModel):
    pass
class StrategyScope(BaseModel):
    environment_scope: Optional[str] = None
class Strategy(BaseModel):
    name: Optional[str] = None
    parameters: Optional[StrategyParameters] = None
    scopes: Optional[List[StrategyScope]] = None
class ListFeatureFlagsForProject(BaseModel):
    id: Union[int, str]
    scope: Optional[str] = None
class GetSingleFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
class CreateFeatureFlag(BaseModel):
    id: Union[int, str]
    name: str
    version: str
    description: Optional[str] = None
    active: Optional[bool] = None
    strategies: Optional[List[Strategy]] = None
class UpdateFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
    description: Optional[str] = None
    active: Optional[bool] = None
    name: Optional[str] = None
    strategies: Optional[List[Strategy]] = None
class DeleteFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pipelines_schedules.py
class GetAllPipelineSchedulesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    scope: Optional[str] = Field(None, description=
        'The scope of pipeline schedules, must be one of: active, inactive.')
class GetSinglePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class GetPipelinesTriggeredByScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class CreateNewPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    description: str = Field(..., description=
        'The description of the pipeline schedule.')
    ref: str = Field(..., description=
        'The branch or tag name that is triggered.')
    cron: str = Field(..., description=
        'The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description=
        'The time zone supported by ActiveSupport::TimeZone, for example: Pacific Time (US & Canada) (default: UTC).'
        )
    active: Optional[bool] = Field(None, description=
        'The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated (default: true).'
        )
class EditPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    description: Optional[str] = Field(None, description=
        'The description of the pipeline schedule.')
    ref: Optional[str] = Field(None, description=
        'The branch or tag name that is triggered.')
    cron: Optional[str] = Field(None, description=
        'The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description=
        'The time zone supported by ActiveSupport::TimeZone (for example Pacific Time (US & Canada)), or TZInfo::Timezone (for example America/Los_Angeles).'
        )
    active: Optional[bool] = Field(None, description=
        'The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated.'
        )
class TakeOwnershipOfPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class DeletePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class RunScheduledPipelineImmediatelyInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class CreatePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description=
        'The key of a variable; must have no more than 255 characters; only A-Z, a-z, 0-9, and _ are allowed.'
        )
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description=
        'The type of a variable. Available types are: env_var (default) and file.'
        )
class EditPipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description=
        'The type of a variable. Available types are: env_var (default) and file.'
        )
class DeletePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dockerfile_templates.py
class TemplatesDockerfilesKey(BaseModel):
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_releases.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/keys.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/packages.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/labels_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/freeze_periods.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/broadcast_messages.py
class GetASpecificBroadcastMessage(BaseModel):
    id: int
class CreateABroadcastMessage(BaseModel):
    message: str
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class UpdateABroadcastMessage(BaseModel):
    id: int
    message: Optional[str]
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class DeleteABroadcastMessage(BaseModel):
    id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/groups.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/wikis_project.py
class ProjectsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class ProjectsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class ProjectsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class ProjectsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class ProjectsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/npm.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/avatar.py
class Avatar(BaseModel):
    email: str
    size: Optional[int] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_group.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/error_tracking.py
class GetErrorTrackingSettings(BaseModel):
    id: Union[int, str]
class CreateErrorTrackingSettings(BaseModel):
    id: int
    active: bool
    integrated: bool
class EnableOrDisableTheErrorTrackingProjectSettings(BaseModel):
    id: int
    active: bool
    integrated: Optional[bool] = None
class ListProjectClientKeys(BaseModel):
    id: Union[int, str]
class CreateAClientKey(BaseModel):
    id: Union[int, str]
class DeleteAClientKey(BaseModel):
    id: Union[int, str]
    key_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/debian_project_distributions.py
class ListAllDebianDistributionsInAProject(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class SingleDebianProjectDistributionKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_label_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/repository_files.py
class ProjectIdRepositoryFiles(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    file_path: str = Field(description='URL encoded full path to new file')
    ref: str = Field(description='The name of branch, tag or commit')
class ProjectIdRepositoryFilesBlame(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    file_path: str = Field(description=
        'URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(description='The name of branch, tag or commit.')
    range_start: int = Field(description=
        'The first line of the range to blame.')
    range_end: int = Field(description='The last line of the range to blame.')
    range: Optional[dict] = Field(description='Blame range.')
class ProjectsIdRepositoryFilesFilepathRaw(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    file_path: str = Field(..., description=
        'URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(..., description=
        'The name of branch, tag or commit. Default is the HEAD of the project.'
        )
    lfs: Optional[bool] = Field(None, description=
        'Determines if the response should be Git LFS file contents, rather than the pointer. If the file is not tracked by Git LFS, ignored. Defaults to false.'
        )
class ProjectsIdRepositoryFilesFilepathCreate(BaseModel):
    branch: str = Field(description=
        'Name of the new branch to create. The commit is added to this branch.'
        )
    commit_message: str = Field(description='The commit message.')
    content: str = Field(description='The file’s content.')
    file_path: str = Field(description=
        'URL-encoded full path to new file. For example: lib%2Fclass%2Erb.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    author_email: Optional[str] = Field(None, description=
        'The commit author’s email address.')
    author_name: Optional[str] = Field(None, description=
        'The commit author’s name.')
    encoding: Optional[str] = Field(None, description=
        'Change encoding to base64. Default is text.')
    execute_filemode: Optional[bool] = Field(None, description=
        'Enables or disables the execute flag on the file. Can be true or false.'
        )
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathUpdate(BaseModel):
    branch: str
    commit_message: str
    content: str
    file_path: str
    id: Union[int, str]
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    encoding: Optional[str] = None
    execute_filemode: Optional[bool] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathDelete(BaseModel):
    branch: str
    commit_message: str
    file_path: str
    id: int
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositorySubmodulesSubmodule(BaseModel):
    id: int
    submodule: str
    branch: str
    commit_sha: str
    commit_message: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/nuget.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/container_registry.py
class ContainerRegistryAccessLevelEnum(str, Enum):
    enabled = 'enabled'
    private = 'private'
    disabled = 'disabled'
class ChangeContainerRegistryVisibility(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project accessible by the authenticated user.'
        )
    container_registry_access_level: Optional[ContainerRegistryAccessLevelEnum
        ] = Field(default=None, description=
        'The desired visibility of the Container Registry. One of enabled (default), private, or disabled.'
        )
class ListProjectRegistryRepositories(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
class GroupsIdRegistryRepositories(BaseModel):
    id: Union[int, str]
class RegistryRepositoriesId(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
    size: Optional[bool] = None
class ProjectsIdRegistryRepositoriesRepositoryid(BaseModel):
    id: Union[int, str]
    repository_id: int
class ProjectsIdRegistryRepositoriesRepositoryidTags(BaseModel):
    id: Union[int, str]
    repository_id: int
class GetDetailsOfARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteRegistryRepositoryTagsInBulk(BaseModel):
    id: Union[int, str]
    repository_id: int
    name_regex: Optional[str] = None
    name_regex_delete: str
    name_regex_keep: Optional[str] = None
    keep_n: Optional[int] = None
    older_than: Optional[str] = None
class ObtainTokenInput(BaseModel):
    CI_SERVER_URL: str = Field(description='CI server URL.')
    service: str = Field(default='container_registry', description=
        'The service type.')
    scope: str = Field(description='Scope for the token.')
class DeleteImageTagsByReferenceInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    CI_REGISTRY_IMAGE: str = Field(description='The registry image.')
    CI_COMMIT_SHORT_SHA: str = Field(description='The commit SHA.')
class ListAllContainerRepositoriesInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    admin_username: str = Field(description='The admin username.')
    admin_password: str = Field(description='The admin password.')
    service: str = Field(default='container_registry', description=
        'The service type.')
    scope: str = Field(default='registry:catalog:*', description=
        'Scope for the token.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_milestone_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/templates.py
class TemplatesGitignoresKey(BaseModel):
    key: str
class TemplatesGitlabciymlsKey(BaseModel):
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/jobs.py
class JobScope(str, Enum):
    created = 'created'
    pending = 'pending'
    running = 'running'
    failed = 'failed'
    success = 'success'
    canceled = 'canceled'
    skipped = 'skipped'
    waiting_for_resource = 'waiting_for_resource'
    manual = 'manual'
class ListProjectJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
class ListPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
    include_retried: Optional[bool] = Field(False, description=
        'Include retried jobs in the response.')
class ListPipelineTriggerJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
class GetAllowedAgentsInput(BaseModel):
    CI_JOB_TOKEN: str = Field(..., description=
        'Token value associated with the GitLab-provided CI_JOB_TOKEN variable.'
        )
class GetSingleJobInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='ID of a job.')
class JobInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='The ID of a job.')
class JobVariable(BaseModel):
    key: str = Field(..., description='The key of the job variable.')
    value: str = Field(..., description='The value of the job variable.')
class RunJobInput(JobInput):
    job_variables_attributes: Optional[List[JobVariable]] = Field(None,
        description=
        'An array containing the custom variables available to the job.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/gitignore.py
class ListAllGitignoreTemplates(BaseModel):
    pass
class GetSingleGitignoreTemplate(BaseModel):
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/releases.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/gitlab_ci_yaml.py
class ListAllCICDYamlTemplates(BaseModel):
    pass
class GetSingleCICDYamlTemplate(BaseModel):
    key: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/milestones_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_activity_analytics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/job_artifacts.py
class GetJobArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int
    job_token: Optional[str] = None
class DownloadArtifacts(BaseModel):
    id: Union[int, str]
    ref_name: str
    job: str
    job_token: Optional[str] = None
class DownloadSingleArtifactByJobID(BaseModel):
    id: Union[int, str]
    job_id: int
    artifact_path: str
    job_token: Optional[str] = None
class DownloadSingleArtifactFromSpecificTag(BaseModel):
    id: Union[int, str]
    ref_name: str
    artifact_path: str
    job: str
    job_token: Optional[str] = None
class KeepArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issues_statistics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_statistics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/experiments.py
class ListAllExperiments(BaseModel):
    pass

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/scim.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/feature_flag_user_lists.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/vulnerability_findings.py
class ProjectsIdVulnerabilityfindings(BaseModel):
    id: int
    report_type: Optional[List[str]] = None
    scope: Optional[str] = None
    severity: Optional[List[str]] = None
    confidence: Optional[List[str]] = None
    pipeline_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/licenses_(templates).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/topics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/secrets.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/debian.py
class ProjectsIdPackagesDebianFilename(BaseModel):
    id: str
    file_name: str
    distribution: Optional[str] = None
    component: Optional[str] = None
class ProjectsIdPackagesDebianPoolDistributionLetterPackagenamePackageversionFilename(
    BaseModel):
    distribution: str
    letter: str
    package_name: str
    package_version: str
    file_name: str
class DownloadADistributionReleaseFile(BaseModel):
    distribution: str
class DownloadASignedDistributionReleaseFile(BaseModel):
    distribution: str
class DownloadAReleaseFileSignature(BaseModel):
    distribution: str
class DownloadAPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadAPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadADebianInstallerPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DowloadADebianInstallerPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadASourcePackagesIndex(BaseModel):
    distribution: str
    component: str
class DownloadASourcePackagesIndexByHash(BaseModel):
    distribution: str
    component: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/ruby_gems.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/markdown.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/debian_group_distributions.py
class ListAllDebianDistributionsInAGroup(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class GroupsIdDebiandistributionsCodenameKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/variables_project.py
class Variable(BaseModel):
    key: str
    value: str
    variable_type: Optional[str] = 'env_var'
    protected: Optional[bool] = False
    masked: Optional[bool] = False
    raw: Optional[bool] = False
    environment_scope: Optional[str] = '*'
    description: Optional[str] = None
class VariableFilter(BaseModel):
    environment_scope: Optional[str] = None
class GetProjectVariables(BaseModel):
    id: Union[int, str]
class GetVariable(BaseModel):
    id: Union[int, str]
    key: str
    filter: Optional[VariableFilter] = None
class CreateVariable(GetProjectVariables, Variable):
    pass
class UpdateVariable(GetVariable, Variable):
    pass
class DeleteVariable(GetVariable):
    pass

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/links_(epic).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/wikis_group.py
class GroupsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class GroupsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class GroupsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class GroupsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class GroupsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/audit_events.py
class Auditevents(BaseModel):
    created_after: Optional[str] = None
    created_before: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[int] = None
class AuditeventsId(BaseModel):
    id: int
class GroupsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class GroupsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int
class ProjectsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class ProjectsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_access_tokens.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/runners.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/environments.py
class ProjectsIdEnvironments(BaseModel):
    id: int
    name: Optional[str] = None
    search: Optional[str] = None
    states: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentid(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsCreate(BaseModel):
    id: int
    name: str
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentsid(BaseModel):
    id: int
    environment_id: int
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentidDelete(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsReviewapps(BaseModel):
    id: int
    before: Optional[datetime] = None
    limit: Optional[int] = None
    dry_run: Optional[bool] = None
class ProjectsIdEnvironmentsEnvironmentidStop(BaseModel):
    id: int
    environment_id: int
    force: Optional[bool] = None
class ProjectsIdEnvironmentsStopstale(BaseModel):
    id: int
    before: datetime

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_level_protected_branches.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/http_wrapper.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/gitlab_pages.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/marketplace.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/snippets.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/notes_(comments).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/terraform_registry.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/repositories.py
class ProjectsIdRepositoryTree(BaseModel):
    id: int
    page_token: Optional[str] = None
    pagination: Optional[str] = None
    path: Optional[str] = None
    per_page: Optional[str] = None
    recursive: bool = Field(False)
    ref: Optional[str] = None
class ProjectsIdRepositoryBlobsSha(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryBlobsShaRaw(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryArchive(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    path: Optional[str] = Field(None, description=
        'The subpath of the repository to download. Defaults to the whole repository.'
        )
    sha: Optional[str] = Field(None, description=
        'The commit SHA to download. A tag, branch reference, or SHA can be used. Defaults to the tip of the default branch.'
        )
    format: Optional[str] = Field(None, description=
        "The archive format. Options are: 'bz2', 'tar', 'tar.bz2', 'tar.gz', 'tb2', 'tbz', 'tbz2', 'zip'. Defaults to 'tar.gz'."
        )
class ProjectsIdRepositoryCompare(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    from_commit_or_branch: str = Field(..., alias='from', description=
        'The commit SHA or branch name.')
    to: str = Field(..., description='The commit SHA or branch name.')
    from_project_id: Optional[int] = Field(None, description=
        'The ID to compare from.')
    straight: Optional[bool] = Field(False, description=
        'Comparison method: true for direct comparison between from and to (from..to), false to compare using merge base (from…to)’. Default is false.'
        )
class ProjectsIdRepositoryContributors(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    order_by: Optional[str] = Field(None, description=
        'Return contributors ordered by name, email, or commits (orders by commit date) fields. Default is commits.'
        )
    sort: Optional[str] = Field(None, description=
        'Return contributors sorted in asc or desc order. Default is asc.')
class ProjectsIdRepositoryMergebase(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    refs: List[str] = Field(description=
        'The refs to find the common ancestor of. Accepts multiple refs.')
class ProjectsIdRepositoryChangelog(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    version: str = Field(description=
        'The version to generate the changelog for. The format must follow semantic versioning.'
        )
    branch: Optional[str] = Field(None, description=
        'The branch to commit the changelog changes to. Defaults to the project’s default branch.'
        )
    config_file: Optional[str] = Field(None, description=
        'Path to the changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.'
        )
    date: Optional[datetime] = Field(None, description=
        'The date and time of the release. Defaults to the current time.')
    file: Optional[str] = Field(None, description=
        'The file to commit the changes to. Defaults to CHANGELOG.md.')
    from_: Optional[str] = Field(None, alias='from', description=
        'The SHA of the commit that marks the beginning of the range of commits to include in the changelog. This commit isn’t included in the changelog.'
        )
    message: Optional[str] = Field(None, description=
        'The commit message to use when committing the changes. Defaults to Add changelog for version X, where X is the value of the version argument.'
        )
    to: Optional[str] = Field(None, description=
        'The SHA of the commit that marks the end of the range of commits to include in the changelog. This commit is included in the changelog. Defaults to the branch specified in the branch attribute. Limited to 15000 commits unless the feature flag changelog_commits_limitation is disabled.'
        )
    trailer: Optional[str] = Field(None, description=
        'The Git trailer to use for including commits. Defaults to Changelog. Case-sensitive: Example does not match example or eXaMpLE.'
        )
class GenerateChangelogData(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    version: str = Field(description=
        'The version to generate the changelog for. The format must follow semantic versioning.'
        )
    config_file: Optional[str] = Field(description=
        'The path of changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.'
        )
    date: Optional[datetime] = Field(description=
        'The date and time of the release. Uses ISO 8601 format. Defaults to the current time.'
        )
    from_: Optional[str] = Field(alias='from', description=
        'The start of the range of commits (as a SHA) to use for generating the changelog. This commit itself isn’t included in the list.'
        )
    to: Optional[str] = Field(description=
        'The end of the range of commits (as a SHA) to use for the changelog. This commit is included in the list. Defaults to the HEAD of the default project branch.'
        )
    trailer: Optional[str] = Field(description=
        'The Git trailer to use for including commits. Defaults to Changelog.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/deployments.py
class ListProjectDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class GetASpecificDeployment(BaseModel):
    id: int
    deployment_id: int
class GetDeploymentFrequency(BaseModel):
    id: int
    finished_after: Optional[datetime] = None
class DeploymentDuration(BaseModel):
    created_at: datetime
    finished_at: datetime
class ListProjectDeployment(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsCreate(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsDeploymentid(BaseModel):
    id: int
    deployment_id: int
class CreateADeployment(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeploymentsDeploymentidUpdate(BaseModel):
    id: int
    deployment_id: int
    status: str
class ProjectsIdDeploymentsDeploymentidDelete(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidMergerequests(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidApproval(BaseModel):
    id: int
    deployment_id: int
    status: str
    comment: Optional[str] = None
    represented_as: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/snippet_repository_storage_moves.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/notification_settings.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/iterations_(group).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/search.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_aliases.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/http_wrapper_privatetoken.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_badges.py
class GroupsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class GroupsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesAdd(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class GroupsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class GroupsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/external_status_checks.py
class ProjectsIdExternalstatuschecks(BaseModel):
    id: Union[int, str] = Field(description='ID of a project')
class CreateUpdateExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    name: Optional[str] = Field(description=
        'Display name of external status check service')
    external_url: Optional[str] = Field(description=
        'URL of external status check service')
    protected_branch_ids: Optional[List[int]] = Field(description=
        'IDs of protected branches to scope the rule by')
class UpdateExternalStatusCheckService(BaseModel):
    id: Union[int, str]
    check_id: int
    name: Optional[str] = None
    external_url: Optional[str] = None
    protected_branch_ids: Optional[List[int]] = None
class DeleteExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    check_id: int = Field(description='ID of an external status check service')
class MergeRequestStatusChecks(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
class SetStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    sha: str = Field(description='SHA at HEAD of the source branch')
    external_status_check_id: int = Field(description=
        'ID of an external status check')
    status: Optional[str] = Field(description=
        'Set to passed to pass the check or failed to fail it')
class RetryFailedStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    external_status_check_id: int = Field(description=
        'ID of a failed external status check')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/access_requests.py
class ProjectsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class ProjectsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class GroupsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int
class ProjectsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_templates.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/sidekiq_metrics.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_level_protected_environments.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/invitations.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/go_proxy.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/license.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_repository_storage_moves.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/merge_trains.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/vulnerabilities.py
class VulnerabilitiesId(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdConfirm(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdResolve(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdDismiss(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdRevert(BaseModel):
    id: Union[int, str]

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/variables_group.py
class ListGroupVariables(BaseModel):
    id: Union[int, str]
class VariableType(str, Enum):
    env_var = 'env_var'
    file = 'file'
class ShowGroupVariableDetails(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
class CreateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class UpdateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class RemoveGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pypi.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/maven.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/group_access_tokens.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/projects.py
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
    custom_attributes: Optional[Dict[str, str]] = Field(None, description=
        'A dictionary of custom attributes to filter by')
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
class CreateProjectRequest(BaseModel):
    name: Optional[str] = Field(None, description=
        'The name of the new project. Equals path if not provided.')
    path: Optional[str] = Field(None, description=
        'Repository name for new project. Generated based on name if not provided (generated as lowercase with dashes). Starting with GitLab 14.9, path must not start or end with a special character and must not contain consecutive special characters.'
        )
    allow_merge_on_skipped_pipeline: Optional[bool] = Field(None,
        description=
        'Set whether or not merge requests can be merged with skipped jobs.')
    only_allow_merge_if_all_status_checks_passed: Optional[bool] = Field(None,
        description=
        'Indicates that merges of merge requests should be blocked unless all status checks have passed. Defaults to false. Introduced in GitLab 15.5 with feature flag only_allow_merge_if_all_status_checks_passed disabled by default.'
        )
    analytics_access_level: Optional[str] = Field(None, description=
        'One of disabled, private or enabled.')
    approvals_before_merge: Optional[int] = Field(None, description=
        'How many approvers should approve merge requests by default. To configure approval rules, see Merge request approvals API. Deprecated in GitLab 16.0.'
        )
    auto_cancel_pending_pipelines: Optional[str] = Field(None, description=
        'Auto-cancel pending pipelines. This action toggles between an enabled state and a disabled state; it is not a boolean.'
        )
    auto_devops_deploy_strategy: Optional[str] = Field(None, description=
        'Auto Deploy strategy (continuous, manual or timed_incremental).')
    auto_devops_enabled: Optional[bool] = Field(None, description=
        'Enable Auto DevOps for this project.')
    autoclose_referenced_issues: Optional[bool] = Field(None, description=
        'Set whether auto-closing referenced issues on default branch.')
    avatar: Optional[Union[str, Any]] = Field(None, description=
        'Image file for avatar of the project.')
    build_git_strategy: Optional[str] = Field(None, description=
        'The Git strategy. Defaults to fetch.')
    build_timeout: Optional[int] = Field(None, description=
        'The maximum amount of time, in seconds, that a job can run.')
    builds_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    ci_config_path: Optional[str] = Field(None, description=
        'The path to CI configuration file.')
    container_expiration_policy_attributes: Optional[dict] = Field(None,
        description='Update the image cleanup policy for this project.')
    container_registry_access_level: Optional[str] = Field(None,
        description=
        'Set visibility of container registry, for this project, to one of disabled, private or enabled.'
        )
    container_registry_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable container registry for this project. Use container_registry_access_level instead.'
        )
    default_branch: Optional[str] = Field(None, description=
        'The default branch name. Requires initialize_with_readme to be true.')
    description: Optional[str] = Field(None, description=
        'Short project description.')
    emails_disabled: Optional[bool] = Field(None, description=
        'Disable email notifications.')
    external_authorization_classification_label: Optional[str] = Field(None,
        description='The classification label for the project.')
    forking_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    group_with_project_templates_id: Optional[int] = Field(None,
        description=
        'For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true.'
        )
    import_url: Optional[str] = Field(None, description=
        'URL to import repository from. When the URL value isn’t empty, you must not set initialize_with_readme to true. Doing so might result in the following error: not a git repository.'
        )
    initialize_with_readme: Optional[bool] = Field(None, description=
        'Whether to create a Git repository with just a README.md file. Default is false.'
        )
    issues_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    issues_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable issues for this project. Use issues_access_level instead.'
        )
    jobs_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable jobs for this project. Use builds_access_level instead.'
        )
    lfs_enabled: Optional[bool] = Field(None, description='Enable LFS.')
    merge_method: Optional[str] = Field(None, description=
        'Set the merge method used.')
    merge_pipelines_enabled: Optional[bool] = Field(None, description=
        'Enable or disable merge pipelines.')
    merge_requests_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    merge_requests_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable merge requests for this project. Use merge_requests_access_level instead.'
        )
    merge_trains_enabled: Optional[bool] = Field(None, description=
        'Enable or disable merge trains.')
    mirror_trigger_builds: Optional[bool] = Field(None, description=
        'Pull mirroring triggers builds.')
    mirror: Optional[bool] = Field(None, description=
        'Enables pull mirroring in a project.')
    namespace_id: Optional[int] = Field(None, description=
        'Namespace for the new project (defaults to the current user’s namespace).'
        )
    only_allow_merge_if_all_discussions_are_resolved: Optional[bool] = Field(
        None, description=
        'Set whether merge requests can only be merged when all the discussions are resolved.'
        )
    only_allow_merge_if_pipeline_succeeds: Optional[bool] = Field(None,
        description=
        'Set whether merge requests can only be merged with successful pipelines.'
        )
    packages_enabled: Optional[bool] = Field(None, description=
        'Enable or disable packages repository feature.')
    pages_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, enabled, or public.')
    printing_merge_request_link_enabled: Optional[bool] = Field(None,
        description=
        'Show link to create/view merge request when pushing from the command line.'
        )
    public_builds: Optional[bool] = Field(None, description=
        'If true, jobs can be viewed by non-project members.')
    releases_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    environments_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    feature_flags_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    infrastructure_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    monitor_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    remove_source_branch_after_merge: Optional[bool] = Field(None,
        description=
        'Enable Delete source branch option by default for all new merge requests.'
        )
    repository_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    repository_storage: Optional[str] = Field(None, description=
        'Which storage shard the repository is on. (administrator only)')
    request_access_enabled: Optional[bool] = Field(None, description=
        'Allow users to request member access.')
    requirements_access_level: Optional[str] = Field(None, description=
        'One of disabled, private or enabled')
    resolve_outdated_diff_discussions: Optional[bool] = Field(None,
        description=
        'Automatically resolve merge request diffs discussions on lines changed with a push.'
        )
    security_and_compliance_access_level: Optional[str] = Field(None,
        description=
        '(GitLab 14.9 and later) Security and compliance access level. One of disabled, private, or enabled.'
        )
    shared_runners_enabled: Optional[bool] = Field(None, description=
        'Enable shared runners for this project.')
    group_runners_enabled: Optional[bool] = Field(None, description=
        'Enable group runners for this project.')
    snippets_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    snippets_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable snippets for this project. Use snippets_access_level instead.'
        )
    squash_option: Optional[str] = Field(None, description=
        'One of never, always, default_on, or default_off.')
    tag_list: Optional[list] = Field(None, description=
        '(Deprecated in GitLab 14.0) The list of tags for a project; put array of tags, that should be finally assigned to a project. Use topics instead.'
        )
    template_name: Optional[str] = Field(None, description=
        'When used without use_custom_template, name of a built-in project template.'
        )
    template_project_id: Optional[int] = Field(None, description=
        'When used with use_custom_template, project ID of a custom project template.'
        )
    topics: Optional[list] = Field(None, description=
        'The list of topics for a project; put array of topics, that should be finally assigned to a project. (Introduced in GitLab 14.0.)'
        )
    use_custom_template: Optional[bool] = Field(None, description=
        'Use either custom instance or group (with group_with_project_templates_id) project template.'
        )
    visibility: Optional[str] = Field(None, description=
        'See project visibility level.')
    wiki_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    wiki_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable wiki for this project. Use wiki_access_level instead.'
        )
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
    container_expiration_policy_attributes: Optional[
        ContainerExpirationPolicyAttributes] = None
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

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/merge_requests.py
class ProjectsMergeRequestCreate(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    source_branch: str = Field(description='The source branch name.')
    target_branch: str = Field(description='The target branch name.')
    title: str = Field(description='The title of merge request.')
    allow_collaboration: Optional[bool] = Field(None, description=
        'Allow commits from members who can merge to the target branch.')
    approvals_before_merge: Optional[int] = Field(None, description=
        'The amount of approvals required before merging.')
    allow_maintainer_to_push: Optional[bool] = Field(None, description=
        'Allow users who can merge to the target branch to push to the source branch.'
        )
    assignee_id: Optional[int] = Field(None, description=
        'The ID of a user to assign merge request.')
    assignee_ids: Optional[List[int]] = Field(None, description=
        'The IDs of users to assign merge request.')
    description: Optional[str] = Field(None, description=
        'The description of merge request.')
    labels: Optional[str] = Field(None, description=
        'Comma-separated list of label names.')
    milestone_id: Optional[int] = Field(None, description=
        'The global ID of a milestone to assign merge request.')
    remove_source_branch: Optional[bool] = Field(None, description=
        'Flag indicating if a merge request should remove the source branch when merging.'
        )
    reviewer_ids: Optional[List[int]] = Field(None, description=
        'The IDs of users to request review from when merge request created.')
    squash: Optional[bool] = Field(None, description=
        'Squash commits into a single commit when merging.')
    squash_on_merge: Optional[bool] = Field(None, description=
        'Squash commits into a single commit after merging.')
    target_project_id: Optional[int] = Field(None, description=
        'The target project ID. If the user is a maintainer of the target project, the source project is set as the target_project_id.'
        )

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/member_roles.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/resource_weight_events.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/search_migrations.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/integrations.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/emoji_reactions.py
class AwardEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
class SingleEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class NewEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    name: str
class DeleteEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class ListCommentEmojiReactionsParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
class GetCommentEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int
class AwardCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    name: str
class DeleteCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/settings_(application).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/pipelines.py
class Scope(str, Enum):
    running = 'running'
    pending = 'pending'
    finished = 'finished'
    branches = 'branches'
    tags = 'tags'
class Status(str, Enum):
    created = 'created'
    waiting_for_resource = 'waiting_for_resource'
    preparing = 'preparing'
    pending = 'pending'
    running = 'running'
    success = 'success'
    failed = 'failed'
    canceled = 'canceled'
    skipped = 'skipped'
    manual = 'manual'
    scheduled = 'scheduled'
class Source(str, Enum):
    push = 'push'
    web = 'web'
    trigger = 'trigger'
    schedule = 'schedule'
    api = 'api'
    external = 'external'
    pipeline = 'pipeline'
    chat = 'chat'
    webide = 'webide'
    merge_request_event = 'merge_request_event'
    external_pull_request_event = 'external_pull_request_event'
    parent_pipeline = 'parent_pipeline'
    ondemand_dast_scan = 'ondemand_dast_scan'
    ondemand_dast_validation = 'ondemand_dast_validation'
class OrderBy(str, Enum):
    id = 'id'
    status = 'status'
    ref = 'ref'
    updated_at = 'updated_at'
    user_id = 'user_id'
class Sort(str, Enum):
    asc = 'asc'
    desc = 'desc'
class ListProjectPipelinesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    scope: Optional[Scope]
    status: Optional[Status]
    source: Optional[Source]
    ref: Optional[str]
    sha: Optional[str]
    yaml_errors: Optional[bool]
    username: Optional[str]
    updated_after: Optional[datetime]
    updated_before: Optional[datetime]
    name: Optional[str]
    order_by: Optional[OrderBy]
    sort: Optional[Sort]
class GetPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineVariablesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportSummaryInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetLatestPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    ref: Optional[str] = Field(None, description=
        'The branch or tag to check for the latest pipeline. Defaults to the default branch when not specified.'
        )
class CreatePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    ref: str = Field(..., description=
        'The branch or tag to run the pipeline on.')
    variables: Optional[List[Dict[str, Union[str, Dict[str, str]]]]] = Field(
        None, description=
        'An array of hashes containing the variables available in the pipeline.'
        )
class RetryJobsInPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class CancelPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class DeletePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/lint_.gitlab_ci.yml.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/service_data.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/dependencies.py
class ProjectsIdDependencies(BaseModel):
    id: Union[int, str]
    package_manager: Optional[str] = None

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/project_badges.py
class ProjectsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class ProjectsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesCreate(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/helm.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/namespaces.py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/links_(issue).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/deploy_keys.py
class Deploykeys(BaseModel):
    public: Optional[bool] = None
class ProjectsIdDeploykeys(BaseModel):
    id: int
class UsersIdorusernameProjectdeploykeys(BaseModel):
    id_or_username: str
class ProjectsIdDeploykeysKeyidSingle(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysAdd(BaseModel):
    id: int
    key: str
    title: str
    can_push: Optional[bool] = None
    expires_at: Optional[datetime] = None
class ProjectsIdDeploykeysKeyidUpdate(BaseModel):
    id: int
    can_push: Optional[bool] = None
    title: Optional[str] = None
class ProjectsIdDeploykeysKeyidDelete(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysKeyidEnable(BaseModel):
    id: int
    key_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/issue_boards_(project).py

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/job_token_scopes.py
class GetProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
class PatchProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
    enabled: bool
class GetProjectCICDJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
class CreateNewProjectToJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int
class RemoveProjectFromJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int

# Classes from file: /Users/andrewkuang/Code/Kubiya/solution-engineering/action-store-gitlab/actions/merge_request_context_commits.py

# Classes from file: system_hooks.py

# Classes from file: user_starred_metrics_dashboards.py
class ProjectsIdMetricsUserstarreddashboardsAdd(BaseModel):
    id: Union[int, str]
    dashboard_path: str
class ProjectsIdMetricsUserstarreddashboardsRemove(BaseModel):
    id: Union[int, str]
    dashboard_path: Optional[str] = None

# Classes from file: secure_files.py

# Classes from file: issues.py

# Classes from file: labels_(group).py

# Classes from file: tags.py

# Classes from file: release_links.py

# Classes from file: import.py

# Classes from file: pages_domains.py

# Classes from file: pipeline_triggers.py
class ListProjectTriggerTokensInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
class GetTriggerTokenDetailsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class CreateTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    description: str = Field(..., description='The trigger name.')
class UpdateProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
    description: Optional[str] = Field(None, description='The trigger name.')
class RemoveProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class TriggerPipelineWithTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    ref: str = Field(..., description=
        'The branch or tag to run the pipeline on.')
    token: str = Field(..., description='The trigger token or CI/CD job token.'
        )
    variables: Optional[Dict[str, str]] = Field(None, description=
        'A map of key-valued strings containing the pipeline variables.')

# Classes from file: linked_epics.py

# Classes from file: resource_state_events.py

# Classes from file: project_remote_mirrors.py

# Classes from file: to_do_lists.py

# Classes from file: deploy_tokens.py

# Classes from file: dashboard_annotations.py
class CreateNewAnnotation(BaseModel):
    id: Union[int, str]
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str] = None
    description: str

    @validator('starting_at', 'ending_at', pre=True)
    def parse_iso8601(cls, v):
        if v is None:
            return v
        try:
            return datetime.fromisoformat(v)
        except ValueError:
            raise ValueError('datetime is not in ISO 8601 format')

# Classes from file: geo_nodes.py

# Classes from file: merge_request_approvals.py

# Classes from file: conan.py
class RoutePrefix(str, Enum):
    instance_level = '/packages/conan/v1'
    project_level = '/projects/:id/packages/conan/v1`'
class Ping(BaseModel):
    route_prefix: RoutePrefix = Field(description=
        'pick either instance_level or project_level')
class SearchInput(BaseModel):
    route_prefix: RoutePrefix
    q: str = Field(..., description=
        'Search query. You can use * as a wildcard.')
class AuthenticateInput(BaseModel):
    route_prefix: RoutePrefix
class CheckCredentialsInput(BaseModel):
    route_prefix: RoutePrefix
class RecipeSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifest(BaseModel):
    package_name: str = Field(description='Name of a package.')
    package_version: str = Field(description='Version of a package.')
    package_username: str = Field(description=
        'Conan username of a package. This attribute is the +-separated full path of your project.'
        )
    package_channel: str = Field(description='Channel of a package.')
class PackageManifest(RecipeManifest):
    conan_package_reference: str = Field(description=
        'Reference hash of a Conan package. Conan generates this value.')
class UploadUrls(RecipeManifest):
    files: Dict[str, int] = Field(description=
        'Dictionary of file names with their sizes.')
class PackageUploadUrlsInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
    file_sizes: Dict[str, int]
class DownloadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
class UploadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
    file_content: str
class DownloadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
class UploadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
    file_content: str
class DeletePackageInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str

# Classes from file: custom_attributes.py
class UsersIdCustomattributes(BaseModel):
    id: int
class GroupsIdCustomattributes(BaseModel):
    id: int
class ProjectsIdCustomattributes(BaseModel):
    id: int
class UsersIdCustomattributesKey(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class UsersIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class GroupsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class ProjectsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class UsersIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str

# Classes from file: epics.py
class NotMatch(BaseModel):
    author_id: Optional[int] = Field(None, description=
        'Can exclude by author ID')
    author_username: Optional[str] = Field(None, description=
        'Can exclude by author username (GitLab 14.7 and later)')
    labels: Optional[str] = Field(None, description='Can exclude by labels')
class GroupsIdEpics(BaseModel):
    id: Union[int, str]
    author_id: Optional[int] = None
    author_username: Optional[str] = None
    labels: Optional[str] = None
    with_labels_details: Optional[bool] = None
    order_by: Optional[str] = None
    sort: Optional[str] = None
    search: Optional[str] = None
    state: Optional[str] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    include_ancestor_groups: Optional[bool] = None
    include_descendant_groups: Optional[bool] = None
    my_reaction_emoji: Optional[str] = None
    not_: Optional[NotMatch] = Field(None, alias='not', description=
        'Return epics that do not match the parameters supplied')
class SingleEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class NewEpicInput(BaseModel):
    id: Union[int, str]
    title: str
    labels: Optional[str]
    description: Optional[str]
    color: Optional[str]
    confidential: Optional[bool]
    created_at: Optional[datetime]
    start_date_is_fixed: Optional[bool]
    start_date_fixed: Optional[str]
    due_date_is_fixed: Optional[bool]
    due_date_fixed: Optional[str]
    parent_id: Optional[Union[int, str]]
class UpdateEpic(BaseModel):
    id: int
    epic_iid: int
    add_labels: Optional[str] = None
    confidential: Optional[bool] = None
    description: Optional[str] = None
    due_date_fixed: Optional[str] = None
    due_date_is_fixed: Optional[bool] = None
    labels: Optional[str] = None
    parent_id: Optional[int] = None
    remove_labels: Optional[str] = None
    start_date_fixed: Optional[str] = None
    start_date_is_fixed: Optional[bool] = None
    state_event: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
class DeleteEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class CreateAToDoItem(BaseModel):
    id: Union[int, str]
    epic_iid: int

# Classes from file: issues_(epic).py

# Classes from file: suggestions.py

# Classes from file: product_analytics.py

# Classes from file: discussions.py
class ListProjectIssueDiscussionItems(BaseModel):
    id: Union[int, str]
    issue_iid: int
class GetSingleIssueDiscussionItem(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
class CreateNewIssueThread(BaseModel):
    body: str
    id: Union[int, str]
    issue_iid: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingIssueThreadPayload(BaseModel):
    body: str = Field(..., description='The content of the note or reply.')
    discussion_id: int = Field(..., description='The ID of a thread.')
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    issue_iid: int = Field(..., description='The IID of an issue.')
    note_id: int = Field(..., description='The ID of a thread note.')
    created_at: Optional[datetime] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyExistingIssueThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    issue_iid: int
    note_id: int
class DeleteIssueThreadNote(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
    note_id: int
class ProjectsIdSnippetsSnippetidDiscussions(BaseModel):
    id: Union[int, str]
    snippet_id: int
class ListProjectSnippetDiscussionItems(BaseModel):
    id: Union[int, str]
    snippet_id: int
class GetSingleSnippetDiscussionItem(BaseModel):
    id: Union[int, str]
    snippet_id: int
    discussion_id: int
class CreateNewSnippetThread(BaseModel):
    body: str
    id: Union[int, str]
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingSnippetThread(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class ModifyExistingSnippetThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class DeleteSnippetThreadNote(BaseModel):
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class GroupsIdEpicsEpicidDiscussions(BaseModel):
    epic_id: int
    id: Union[int, str]
class SingleEpicDiscussionItem(BaseModel):
    discussion_id: int = Field(description='The ID of a discussion item.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
class CreateNewEpicThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    created_at: Optional[Union[str, datetime]] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class AddNoteToEpicThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[Union[str, datetime]] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyEpicThreadNote(BaseModel):
    body: str = Field(description='The content of note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class DeleteEpicThreadNote(BaseModel):
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class ListMergeRequestDiscussionItems(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class SingleMergeRequestDiscussionItem(BaseModel):
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class BasicMergeRequestParams(BaseModel):
    body: str = Field(description='The content of the thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class DiffNoteParams(BaseModel):
    base_sha: str = Field(description='Base commit SHA in the source branch.')
    head_sha: str = Field(description=
        'SHA referencing HEAD of this merge request.')
    start_sha: str = Field(description=
        'SHA referencing commit in target branch.')
    new_path: str = Field(description='File path after change.')
    old_path: str = Field(description='File path before change.')
    position_type: str = Field(description=
        'Type of the position reference. Allowed values: text or image.')
class TextDiffNoteParams(BaseModel):
    new_line: Optional[int] = Field(description=
        'For text diff notes, the line number after change.')
    old_line: Optional[int] = Field(description=
        'For text diff notes, the line number before change.')
class ImageDiffNoteParams(BaseModel):
    width: Optional[int] = Field(description=
        'For image diff notes, width of the image.')
    height: Optional[int] = Field(description=
        'For image diff notes, height of the image.')
    x: Optional[float] = Field(description=
        'For image diff notes, X coordinate.')
    y: Optional[float] = Field(description=
        'For image diff notes, Y coordinate.')
class MultilineCommentsParams(BaseModel):
    line_range: dict = Field(description=
        'Line range for a multi-line diff note.')
class CreateNewMergeRequestThread(BasicMergeRequestParams):
    position: DiffNoteParams = Field(description=
        'Position when creating a diff note.')
    text_position: Optional[TextDiffNoteParams] = Field(description=
        'Position parameters for text diff notes.')
    image_position: Optional[ImageDiffNoteParams] = Field(description=
        'Position parameters for image diff notes.')
    multiline_comments: Optional[MultilineCommentsParams] = Field(description
        ='Parameters for multiline comments.')
    commit_id: Optional[str] = Field(description=
        'SHA referencing commit to start this thread on.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class ResolveMergeRequestThread(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    discussion_id: str = Field(description='The ID of a thread.')
    resolved: bool = Field(description='Resolve or unresolve the discussion.')
class AddNoteToMergeRequestThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    discussion_id: str = Field(description='The ID of a thread.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class ModifyMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description=
        'The content of the note or reply. Exactly one of body or resolved must be set.'
        )
    resolved: Optional[bool] = Field(description=
        'Resolve or unresolve the note. Exactly one of body or resolved must be set.'
        )
class DeleteMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
class ListProjectCommitDiscussionItems(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
class GetSingleCommitDiscussionItem(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
class Position(BaseModel):
    base_sha: str = Field(description='SHA of the parent commit.')
    head_sha: str = Field(description=
        'The SHA of this commit. Same as commit_id.')
    start_sha: str = Field(description='SHA of the parent commit.')
    position_type: str = Field(description=
        'Type of the position reference. Allowed values: text or image.')
    hash: Optional[str] = Field(description=
        'Position when creating a diff note.')
    new_path: Optional[str] = Field(description='File path after change.')
    new_line: Optional[int] = Field(description='Line number after change.')
    old_path: Optional[str] = Field(description='File path before change.')
    old_line: Optional[int] = Field(description='Line number before change.')
    height: Optional[int] = Field(description=
        'For image diff notes, image height.')
    width: Optional[int] = Field(description=
        'For image diff notes, image width.')
    x: Optional[int] = Field(description='For image diff notes, X coordinate.')
    y: Optional[int] = Field(description='For image diff notes, Y coordinate.')
class CreateNewCommitThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    position: Position = Field(description=
        'Position when creating a diff note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class AddNoteToCommitThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyCommitThreadNote(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description='The content of a note.')
class DeleteCommitThreadNote(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    note_id: int = Field(description='The ID of a thread note.')

# Classes from file: project_relations_export.py

# Classes from file: snippets_(project).py

# Classes from file: branches.py
class ProjectsIdRepositoryBranches(BaseModel):
    id: int
    search: Optional[str] = None
    regex: Optional[str] = None
class ProjectsIdRepositoryBranchesBranchSingle(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryBranchesCreate(BaseModel):
    id: int
    branch: str
    ref: str
class ProjectsIdRepositoryBranchesBranch(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryMergedbranches(BaseModel):
    id: int

# Classes from file: metadata.py

# Classes from file: version.py

# Classes from file: protected_tags.py

# Classes from file: issue_boards_(group).py

# Classes from file: repository_submodules.py

# Classes from file: milestones_(group).py

# Classes from file: members.py

# Classes from file: protected_branches.py

# Classes from file: commits.py
class ProjectsIdRepositoryCommits(BaseModel):
    id: int
    ref_name: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None
    path: Optional[str] = None
    author: Optional[str] = None
    all: Optional[bool]
    with_stats: Optional[bool]
    first_parent: Optional[bool]
    order: Optional[str]
    trailers: Optional[bool]
class ProjectsIdRepositoryCommitsSha(BaseModel):
    id: int
    sha: str
    stats: Optional[bool] = None
class ProjectsIdRepositoryCommitsShaRefs(BaseModel):
    id: int
    sha: str
    type: Optional[str] = None
class ProjectsIdRepositoryCommitsShaCherrypick(BaseModel):
    id: int
    sha: str
    branch: str
    dry_run: Optional[bool] = None
    message: Optional[str] = None
class ProjectsIdRepositoryCommitsShaRevert(BaseModel):
    id: int
    sha: str
    branch: str
    dry_run: Optional[bool] = None
class ProjectsIdRepositoryCommitsShaDiff(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaComments(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaCommentsPost(BaseModel):
    id: int
    sha: str
    note: str
    path: Optional[str] = None
    line: Optional[int] = None
    line_type: Optional[str] = None
class ProjectsIdRepositoryCommitsShaDiscussions(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaStatuses(BaseModel):
    id: int
    sha: str
    ref: Optional[str] = None
    stage: Optional[str] = None
    name: Optional[str] = None
    all: Optional[bool] = None
class ProjectsIdStatusesSha(BaseModel):
    id: int
    sha: str
    state: str
    ref: Optional[str] = None
    context: Optional[str] = None
    name: Optional[str] = None
    target_url: Optional[str] = None
    description: Optional[str] = None
    coverage: Optional[float] = None
    pipeline_id: Optional[int] = None
class ProjectsIdRepositoryCommitsShaMergerequests(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaSignature(BaseModel):
    id: int
    sha: str

# Classes from file: application_appearance.py
class ApplicationAppearance(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    pwa_name: Optional[str] = None
    pwa_short_name: Optional[str] = None
    pwa_description: Optional[str] = None
    pwa_icon: Optional[Any] = None
    logo: Optional[Any] = None
    header_logo: Optional[Any] = None
    favicon: Optional[Any] = None
    new_project_guidelines: Optional[str] = None
    profile_image_guidelines: Optional[str] = None
    header_message: Optional[str] = None
    footer_message: Optional[str] = None
    message_background_color: Optional[str] = None
    message_font_color: Optional[str] = None
    email_header_and_footer_enabled: Optional[bool] = None
class ChangeLogo(BaseModel):
    logo: Any
    pwa_icon: Any

# Classes from file: users.py

# Classes from file: project_vulnerabilities.py

# Classes from file: draft_notes.py
class ProjectsIdMergerequestsMergerequestiidDraftnotes(BaseModel):
    id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidSingle(
    BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesCreate(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    note: str
    commit_id: Optional[str] = None
    in_reply_to_discussion_id: Optional[int] = None
    resolve_discussion: Optional[bool] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidModify(
    BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
    note: Optional[str] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidDelete(
    BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidPublish(
    BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesBulkpublish(BaseModel):
    id: Union[int, str]
    merge_request_iid: int

# Classes from file: group_migration_by_direct_transfer.py

# Classes from file: resource_iteration_events.py

# Classes from file: agents_for_kubernetes.py
class ListTheAgentsForAProject(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
class GetDetailsAboutAnAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class RegisterAnAgentWithAProject(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    name: str = Field(description='Name for the agent')
class DeleteARegisteredAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class ListTokensForAnAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class GetSingleAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')
class CreateAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    name: int = Field(description='Name for the token')
    description: Optional[int] = Field(None, description=
        'Description for the token')
class RevokeAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')

# Classes from file: project_import_export.py

# Classes from file: project_level_protected_environments.py

# Classes from file: composer.py
class GroupIdPackagesComposerPackages(BaseModel):
    id: Union[int, str]
class GroupIdPackagesComposerPSha(BaseModel):
    id: Union[int, str]
    sha: str
class V1PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str
class V2PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
class CreateAPackageInput(BaseModel):
    id: Union[int, str]
    tag: Optional[str] = None
    branch: Optional[str] = None
class ProjectsIdPackagesComposerArchivesPackagename(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str

# Classes from file: alert_management.py
class ListMetricImages(BaseModel):
    id: int
    alert_iid: int
class UpdateMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int
    url: Optional[str] = None
    url_text: Optional[str] = None
class DeleteMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int

# Classes from file: sidekiq_queues.py

# Classes from file: vulnerability_export.py
class SecurityProjectsIdVulnerabilityexports(BaseModel):
    id: Union[int, str]
class SecurityGroupsIdVulnerabilityexports(BaseModel):
    id: Union[int, str]
class SecurityVulnerabilityexportsId(BaseModel):
    id: Union[int, str]
class SecurityVulnerabilityexportsIdDownload(BaseModel):
    id: Union[int, str]

# Classes from file: events.py
class Events(BaseModel):
    action: Optional[str] = None
    target_type: Optional[str] = None
    before: Optional[datetime] = Field(None, description=
        'Include only events created before a certain date.')
    after: Optional[datetime] = Field(None, description=
        'Include only events created after a particular date.')
    target_id: Optional[int] = None
    author_id: Optional[int] = None
    search: Optional[str] = None
class AuthenticatedUserEvents(Events):
    scope: Optional[str] = None
    sort: Optional[str] = None
class UserContributionEvents(Events):
    id: int
    sort: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
class ProjectVisibleEvents(Events):
    project_id: int
    sort: Optional[str] = None

# Classes from file: group_import_export.py

# Classes from file: dora4_metrics.py
class ProjectsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None
class GroupsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None

# Classes from file: plan_limits.py

# Classes from file: statistics_(application).py

# Classes from file: group_repository_storage_moves.py

# Classes from file: iterations_(project).py

# Classes from file: applications.py
class Applications(BaseModel):
    name: str
    redirect_uri: str
    scopes: str
    confidential: Optional[bool] = None
class ApplicationsId(BaseModel):
    id: int

# Classes from file: saml.py

# Classes from file: dependency_proxy.py
class GroupsIdDependencyproxyCache(BaseModel):
    id: int

# Classes from file: group_relations_export.py

# Classes from file: metrics_dashboard_annotations.py
class EnvironmentsIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str
class ClustersIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str

# Classes from file: personal_access_tokens.py

# Classes from file: __init__.py

# Classes from file: instance_level_ci_cd_variables.py

# Classes from file: geo_sites.py

# Classes from file: visual_review_discussions_deprecated.py
class PositionData(BaseModel):
    base_sha: str
    start_sha: str
    head_sha: str
    position_type: str
    new_path: Optional[str] = None
    new_line: Optional[int] = None
    old_path: Optional[str] = None
    old_line: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None
class CreateNewMergeRequestThread(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    body: str
    position: Optional[PositionData] = None

# Classes from file: feature_flags.py
class StrategyParameters(BaseModel):
    pass
class StrategyScope(BaseModel):
    environment_scope: Optional[str] = None
class Strategy(BaseModel):
    name: Optional[str] = None
    parameters: Optional[StrategyParameters] = None
    scopes: Optional[List[StrategyScope]] = None
class ListFeatureFlagsForProject(BaseModel):
    id: Union[int, str]
    scope: Optional[str] = None
class GetSingleFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
class CreateFeatureFlag(BaseModel):
    id: Union[int, str]
    name: str
    version: str
    description: Optional[str] = None
    active: Optional[bool] = None
    strategies: Optional[List[Strategy]] = None
class UpdateFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
    description: Optional[str] = None
    active: Optional[bool] = None
    name: Optional[str] = None
    strategies: Optional[List[Strategy]] = None
class DeleteFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str

# Classes from file: pipelines_schedules.py
class GetAllPipelineSchedulesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    scope: Optional[str] = Field(None, description=
        'The scope of pipeline schedules, must be one of: active, inactive.')
class GetSinglePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class GetPipelinesTriggeredByScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class CreateNewPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    description: str = Field(..., description=
        'The description of the pipeline schedule.')
    ref: str = Field(..., description=
        'The branch or tag name that is triggered.')
    cron: str = Field(..., description=
        'The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description=
        'The time zone supported by ActiveSupport::TimeZone, for example: Pacific Time (US & Canada) (default: UTC).'
        )
    active: Optional[bool] = Field(None, description=
        'The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated (default: true).'
        )
class EditPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    description: Optional[str] = Field(None, description=
        'The description of the pipeline schedule.')
    ref: Optional[str] = Field(None, description=
        'The branch or tag name that is triggered.')
    cron: Optional[str] = Field(None, description=
        'The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description=
        'The time zone supported by ActiveSupport::TimeZone (for example Pacific Time (US & Canada)), or TZInfo::Timezone (for example America/Los_Angeles).'
        )
    active: Optional[bool] = Field(None, description=
        'The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated.'
        )
class TakeOwnershipOfPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class DeletePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class RunScheduledPipelineImmediatelyInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class CreatePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description=
        'The key of a variable; must have no more than 255 characters; only A-Z, a-z, 0-9, and _ are allowed.'
        )
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description=
        'The type of a variable. Available types are: env_var (default) and file.'
        )
class EditPipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description=
        'The type of a variable. Available types are: env_var (default) and file.'
        )
class DeletePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')

# Classes from file: dockerfile_templates.py
class TemplatesDockerfilesKey(BaseModel):
    key: str

# Classes from file: group_releases.py

# Classes from file: keys.py

# Classes from file: packages.py

# Classes from file: labels_(project).py

# Classes from file: freeze_periods.py

# Classes from file: broadcast_messages.py
class GetASpecificBroadcastMessage(BaseModel):
    id: int
class CreateABroadcastMessage(BaseModel):
    message: str
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class UpdateABroadcastMessage(BaseModel):
    id: int
    message: Optional[str]
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class DeleteABroadcastMessage(BaseModel):
    id: int

# Classes from file: groups.py

# Classes from file: wikis_project.py
class ProjectsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class ProjectsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class ProjectsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class ProjectsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class ProjectsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None

# Classes from file: npm.py

# Classes from file: avatar.py
class Avatar(BaseModel):
    email: str
    size: Optional[int] = None

# Classes from file: resource_group.py

# Classes from file: error_tracking.py
class GetErrorTrackingSettings(BaseModel):
    id: Union[int, str]
class CreateErrorTrackingSettings(BaseModel):
    id: int
    active: bool
    integrated: bool
class EnableOrDisableTheErrorTrackingProjectSettings(BaseModel):
    id: int
    active: bool
    integrated: Optional[bool] = None
class ListProjectClientKeys(BaseModel):
    id: Union[int, str]
class CreateAClientKey(BaseModel):
    id: Union[int, str]
class DeleteAClientKey(BaseModel):
    id: Union[int, str]
    key_id: int

# Classes from file: debian_project_distributions.py
class ListAllDebianDistributionsInAProject(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class SingleDebianProjectDistributionKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int

# Classes from file: resource_label_events.py

# Classes from file: repository_files.py
class ProjectIdRepositoryFiles(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    file_path: str = Field(description='URL encoded full path to new file')
    ref: str = Field(description='The name of branch, tag or commit')
class ProjectIdRepositoryFilesBlame(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    file_path: str = Field(description=
        'URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(description='The name of branch, tag or commit.')
    range_start: int = Field(description=
        'The first line of the range to blame.')
    range_end: int = Field(description='The last line of the range to blame.')
    range: Optional[dict] = Field(description='Blame range.')
class ProjectsIdRepositoryFilesFilepathRaw(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    file_path: str = Field(..., description=
        'URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(..., description=
        'The name of branch, tag or commit. Default is the HEAD of the project.'
        )
    lfs: Optional[bool] = Field(None, description=
        'Determines if the response should be Git LFS file contents, rather than the pointer. If the file is not tracked by Git LFS, ignored. Defaults to false.'
        )
class ProjectsIdRepositoryFilesFilepathCreate(BaseModel):
    branch: str = Field(description=
        'Name of the new branch to create. The commit is added to this branch.'
        )
    commit_message: str = Field(description='The commit message.')
    content: str = Field(description='The file’s content.')
    file_path: str = Field(description=
        'URL-encoded full path to new file. For example: lib%2Fclass%2Erb.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    author_email: Optional[str] = Field(None, description=
        'The commit author’s email address.')
    author_name: Optional[str] = Field(None, description=
        'The commit author’s name.')
    encoding: Optional[str] = Field(None, description=
        'Change encoding to base64. Default is text.')
    execute_filemode: Optional[bool] = Field(None, description=
        'Enables or disables the execute flag on the file. Can be true or false.'
        )
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathUpdate(BaseModel):
    branch: str
    commit_message: str
    content: str
    file_path: str
    id: Union[int, str]
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    encoding: Optional[str] = None
    execute_filemode: Optional[bool] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathDelete(BaseModel):
    branch: str
    commit_message: str
    file_path: str
    id: int
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositorySubmodulesSubmodule(BaseModel):
    id: int
    submodule: str
    branch: str
    commit_sha: str
    commit_message: Optional[str] = None

# Classes from file: nuget.py

# Classes from file: container_registry.py
class ContainerRegistryAccessLevelEnum(str, Enum):
    enabled = 'enabled'
    private = 'private'
    disabled = 'disabled'
class ChangeContainerRegistryVisibility(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project accessible by the authenticated user.'
        )
    container_registry_access_level: Optional[ContainerRegistryAccessLevelEnum
        ] = Field(default=None, description=
        'The desired visibility of the Container Registry. One of enabled (default), private, or disabled.'
        )
class ListProjectRegistryRepositories(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
class GroupsIdRegistryRepositories(BaseModel):
    id: Union[int, str]
class RegistryRepositoriesId(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
    size: Optional[bool] = None
class ProjectsIdRegistryRepositoriesRepositoryid(BaseModel):
    id: Union[int, str]
    repository_id: int
class ProjectsIdRegistryRepositoriesRepositoryidTags(BaseModel):
    id: Union[int, str]
    repository_id: int
class GetDetailsOfARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteRegistryRepositoryTagsInBulk(BaseModel):
    id: Union[int, str]
    repository_id: int
    name_regex: Optional[str] = None
    name_regex_delete: str
    name_regex_keep: Optional[str] = None
    keep_n: Optional[int] = None
    older_than: Optional[str] = None
class ObtainTokenInput(BaseModel):
    CI_SERVER_URL: str = Field(description='CI server URL.')
    service: str = Field(default='container_registry', description=
        'The service type.')
    scope: str = Field(description='Scope for the token.')
class DeleteImageTagsByReferenceInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    CI_REGISTRY_IMAGE: str = Field(description='The registry image.')
    CI_COMMIT_SHORT_SHA: str = Field(description='The commit SHA.')
class ListAllContainerRepositoriesInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    admin_username: str = Field(description='The admin username.')
    admin_password: str = Field(description='The admin password.')
    service: str = Field(default='container_registry', description=
        'The service type.')
    scope: str = Field(default='registry:catalog:*', description=
        'Scope for the token.')

# Classes from file: resource_milestone_events.py

# Classes from file: templates.py
class TemplatesGitignoresKey(BaseModel):
    key: str
class TemplatesGitlabciymlsKey(BaseModel):
    key: str

# Classes from file: jobs.py
class JobScope(str, Enum):
    created = 'created'
    pending = 'pending'
    running = 'running'
    failed = 'failed'
    success = 'success'
    canceled = 'canceled'
    skipped = 'skipped'
    waiting_for_resource = 'waiting_for_resource'
    manual = 'manual'
class ListProjectJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
class ListPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
    include_retried: Optional[bool] = Field(False, description=
        'Include retried jobs in the response.')
class ListPipelineTriggerJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
class GetAllowedAgentsInput(BaseModel):
    CI_JOB_TOKEN: str = Field(..., description=
        'Token value associated with the GitLab-provided CI_JOB_TOKEN variable.'
        )
class GetSingleJobInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='ID of a job.')
class JobInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='The ID of a job.')
class JobVariable(BaseModel):
    key: str = Field(..., description='The key of the job variable.')
    value: str = Field(..., description='The value of the job variable.')
class RunJobInput(JobInput):
    job_variables_attributes: Optional[List[JobVariable]] = Field(None,
        description=
        'An array containing the custom variables available to the job.')

# Classes from file: gitignore.py
class ListAllGitignoreTemplates(BaseModel):
    pass
class GetSingleGitignoreTemplate(BaseModel):
    key: str

# Classes from file: releases.py

# Classes from file: gitlab_ci_yaml.py
class ListAllCICDYamlTemplates(BaseModel):
    pass
class GetSingleCICDYamlTemplate(BaseModel):
    key: str

# Classes from file: milestones_(project).py

# Classes from file: group_activity_analytics.py

# Classes from file: job_artifacts.py
class GetJobArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int
    job_token: Optional[str] = None
class DownloadArtifacts(BaseModel):
    id: Union[int, str]
    ref_name: str
    job: str
    job_token: Optional[str] = None
class DownloadSingleArtifactByJobID(BaseModel):
    id: Union[int, str]
    job_id: int
    artifact_path: str
    job_token: Optional[str] = None
class DownloadSingleArtifactFromSpecificTag(BaseModel):
    id: Union[int, str]
    ref_name: str
    artifact_path: str
    job: str
    job_token: Optional[str] = None
class KeepArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int

# Classes from file: issues_statistics.py

# Classes from file: project_statistics.py

# Classes from file: experiments.py
class ListAllExperiments(BaseModel):
    pass

# Classes from file: scim.py

# Classes from file: feature_flag_user_lists.py

# Classes from file: vulnerability_findings.py
class ProjectsIdVulnerabilityfindings(BaseModel):
    id: int
    report_type: Optional[List[str]] = None
    scope: Optional[str] = None
    severity: Optional[List[str]] = None
    confidence: Optional[List[str]] = None
    pipeline_id: int

# Classes from file: licenses_(templates).py

# Classes from file: topics.py

# Classes from file: secrets.py

# Classes from file: debian.py
class ProjectsIdPackagesDebianFilename(BaseModel):
    id: str
    file_name: str
    distribution: Optional[str] = None
    component: Optional[str] = None
class ProjectsIdPackagesDebianPoolDistributionLetterPackagenamePackageversionFilename(
    BaseModel):
    distribution: str
    letter: str
    package_name: str
    package_version: str
    file_name: str
class DownloadADistributionReleaseFile(BaseModel):
    distribution: str
class DownloadASignedDistributionReleaseFile(BaseModel):
    distribution: str
class DownloadAReleaseFileSignature(BaseModel):
    distribution: str
class DownloadAPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadAPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadADebianInstallerPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DowloadADebianInstallerPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadASourcePackagesIndex(BaseModel):
    distribution: str
    component: str
class DownloadASourcePackagesIndexByHash(BaseModel):
    distribution: str
    component: str

# Classes from file: ruby_gems.py

# Classes from file: markdown.py

# Classes from file: debian_group_distributions.py
class ListAllDebianDistributionsInAGroup(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class GroupsIdDebiandistributionsCodenameKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int

# Classes from file: variables_project.py
class Variable(BaseModel):
    key: str
    value: str
    variable_type: Optional[str] = 'env_var'
    protected: Optional[bool] = False
    masked: Optional[bool] = False
    raw: Optional[bool] = False
    environment_scope: Optional[str] = '*'
    description: Optional[str] = None
class VariableFilter(BaseModel):
    environment_scope: Optional[str] = None
class GetProjectVariables(BaseModel):
    id: Union[int, str]
class GetVariable(BaseModel):
    id: Union[int, str]
    key: str
    filter: Optional[VariableFilter] = None
class CreateVariable(GetProjectVariables, Variable):
    pass
class UpdateVariable(GetVariable, Variable):
    pass
class DeleteVariable(GetVariable):
    pass

# Classes from file: links_(epic).py

# Classes from file: wikis_group.py
class GroupsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class GroupsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class GroupsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class GroupsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class GroupsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None

# Classes from file: audit_events.py
class Auditevents(BaseModel):
    created_after: Optional[str] = None
    created_before: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[int] = None
class AuditeventsId(BaseModel):
    id: int
class GroupsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class GroupsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int
class ProjectsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class ProjectsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int

# Classes from file: project_access_tokens.py

# Classes from file: runners.py

# Classes from file: environments.py
class ProjectsIdEnvironments(BaseModel):
    id: int
    name: Optional[str] = None
    search: Optional[str] = None
    states: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentid(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsCreate(BaseModel):
    id: int
    name: str
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentsid(BaseModel):
    id: int
    environment_id: int
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentidDelete(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsReviewapps(BaseModel):
    id: int
    before: Optional[datetime] = None
    limit: Optional[int] = None
    dry_run: Optional[bool] = None
class ProjectsIdEnvironmentsEnvironmentidStop(BaseModel):
    id: int
    environment_id: int
    force: Optional[bool] = None
class ProjectsIdEnvironmentsStopstale(BaseModel):
    id: int
    before: datetime

# Classes from file: group_level_protected_branches.py

# Classes from file: http_wrapper.py

# Classes from file: gitlab_pages.py

# Classes from file: marketplace.py

# Classes from file: snippets.py

# Classes from file: notes_(comments).py

# Classes from file: terraform_registry.py

# Classes from file: repositories.py
class ProjectsIdRepositoryTree(BaseModel):
    id: int
    page_token: Optional[str] = None
    pagination: Optional[str] = None
    path: Optional[str] = None
    per_page: Optional[str] = None
    recursive: bool = Field(False)
    ref: Optional[str] = None
class ProjectsIdRepositoryBlobsSha(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryBlobsShaRaw(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryArchive(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    path: Optional[str] = Field(None, description=
        'The subpath of the repository to download. Defaults to the whole repository.'
        )
    sha: Optional[str] = Field(None, description=
        'The commit SHA to download. A tag, branch reference, or SHA can be used. Defaults to the tip of the default branch.'
        )
    format: Optional[str] = Field(None, description=
        "The archive format. Options are: 'bz2', 'tar', 'tar.bz2', 'tar.gz', 'tb2', 'tbz', 'tbz2', 'zip'. Defaults to 'tar.gz'."
        )
class ProjectsIdRepositoryCompare(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    from_commit_or_branch: str = Field(..., alias='from', description=
        'The commit SHA or branch name.')
    to: str = Field(..., description='The commit SHA or branch name.')
    from_project_id: Optional[int] = Field(None, description=
        'The ID to compare from.')
    straight: Optional[bool] = Field(False, description=
        'Comparison method: true for direct comparison between from and to (from..to), false to compare using merge base (from…to)’. Default is false.'
        )
class ProjectsIdRepositoryContributors(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    order_by: Optional[str] = Field(None, description=
        'Return contributors ordered by name, email, or commits (orders by commit date) fields. Default is commits.'
        )
    sort: Optional[str] = Field(None, description=
        'Return contributors sorted in asc or desc order. Default is asc.')
class ProjectsIdRepositoryMergebase(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    refs: List[str] = Field(description=
        'The refs to find the common ancestor of. Accepts multiple refs.')
class ProjectsIdRepositoryChangelog(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    version: str = Field(description=
        'The version to generate the changelog for. The format must follow semantic versioning.'
        )
    branch: Optional[str] = Field(None, description=
        'The branch to commit the changelog changes to. Defaults to the project’s default branch.'
        )
    config_file: Optional[str] = Field(None, description=
        'Path to the changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.'
        )
    date: Optional[datetime] = Field(None, description=
        'The date and time of the release. Defaults to the current time.')
    file: Optional[str] = Field(None, description=
        'The file to commit the changes to. Defaults to CHANGELOG.md.')
    from_: Optional[str] = Field(None, alias='from', description=
        'The SHA of the commit that marks the beginning of the range of commits to include in the changelog. This commit isn’t included in the changelog.'
        )
    message: Optional[str] = Field(None, description=
        'The commit message to use when committing the changes. Defaults to Add changelog for version X, where X is the value of the version argument.'
        )
    to: Optional[str] = Field(None, description=
        'The SHA of the commit that marks the end of the range of commits to include in the changelog. This commit is included in the changelog. Defaults to the branch specified in the branch attribute. Limited to 15000 commits unless the feature flag changelog_commits_limitation is disabled.'
        )
    trailer: Optional[str] = Field(None, description=
        'The Git trailer to use for including commits. Defaults to Changelog. Case-sensitive: Example does not match example or eXaMpLE.'
        )
class GenerateChangelogData(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    version: str = Field(description=
        'The version to generate the changelog for. The format must follow semantic versioning.'
        )
    config_file: Optional[str] = Field(description=
        'The path of changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.'
        )
    date: Optional[datetime] = Field(description=
        'The date and time of the release. Uses ISO 8601 format. Defaults to the current time.'
        )
    from_: Optional[str] = Field(alias='from', description=
        'The start of the range of commits (as a SHA) to use for generating the changelog. This commit itself isn’t included in the list.'
        )
    to: Optional[str] = Field(description=
        'The end of the range of commits (as a SHA) to use for the changelog. This commit is included in the list. Defaults to the HEAD of the default project branch.'
        )
    trailer: Optional[str] = Field(description=
        'The Git trailer to use for including commits. Defaults to Changelog.')

# Classes from file: deployments.py
class ListProjectDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class GetASpecificDeployment(BaseModel):
    id: int
    deployment_id: int
class GetDeploymentFrequency(BaseModel):
    id: int
    finished_after: Optional[datetime] = None
class DeploymentDuration(BaseModel):
    created_at: datetime
    finished_at: datetime
class ListProjectDeployment(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsCreate(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsDeploymentid(BaseModel):
    id: int
    deployment_id: int
class CreateADeployment(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeploymentsDeploymentidUpdate(BaseModel):
    id: int
    deployment_id: int
    status: str
class ProjectsIdDeploymentsDeploymentidDelete(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidMergerequests(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidApproval(BaseModel):
    id: int
    deployment_id: int
    status: str
    comment: Optional[str] = None
    represented_as: Optional[str] = None

# Classes from file: snippet_repository_storage_moves.py

# Classes from file: notification_settings.py

# Classes from file: iterations_(group).py

# Classes from file: search.py

# Classes from file: project_aliases.py

# Classes from file: http_wrapper_privatetoken.py

# Classes from file: group_badges.py
class GroupsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class GroupsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesAdd(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class GroupsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class GroupsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str

# Classes from file: external_status_checks.py
class ProjectsIdExternalstatuschecks(BaseModel):
    id: Union[int, str] = Field(description='ID of a project')
class CreateUpdateExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    name: Optional[str] = Field(description=
        'Display name of external status check service')
    external_url: Optional[str] = Field(description=
        'URL of external status check service')
    protected_branch_ids: Optional[List[int]] = Field(description=
        'IDs of protected branches to scope the rule by')
class UpdateExternalStatusCheckService(BaseModel):
    id: Union[int, str]
    check_id: int
    name: Optional[str] = None
    external_url: Optional[str] = None
    protected_branch_ids: Optional[List[int]] = None
class DeleteExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    check_id: int = Field(description='ID of an external status check service')
class MergeRequestStatusChecks(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
class SetStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    sha: str = Field(description='SHA at HEAD of the source branch')
    external_status_check_id: int = Field(description=
        'ID of an external status check')
    status: Optional[str] = Field(description=
        'Set to passed to pass the check or failed to fail it')
class RetryFailedStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    external_status_check_id: int = Field(description=
        'ID of a failed external status check')

# Classes from file: access_requests.py
class ProjectsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class ProjectsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class GroupsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int
class ProjectsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int

# Classes from file: project_templates.py

# Classes from file: sidekiq_metrics.py

# Classes from file: group_level_protected_environments.py

# Classes from file: invitations.py

# Classes from file: go_proxy.py

# Classes from file: license.py

# Classes from file: project_repository_storage_moves.py

# Classes from file: merge_trains.py

# Classes from file: vulnerabilities.py
class VulnerabilitiesId(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdConfirm(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdResolve(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdDismiss(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdRevert(BaseModel):
    id: Union[int, str]

# Classes from file: variables_group.py
class ListGroupVariables(BaseModel):
    id: Union[int, str]
class VariableType(str, Enum):
    env_var = 'env_var'
    file = 'file'
class ShowGroupVariableDetails(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
class CreateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class UpdateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class RemoveGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')

# Classes from file: pypi.py

# Classes from file: maven.py

# Classes from file: group_access_tokens.py

# Classes from file: projects.py
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
    custom_attributes: Optional[Dict[str, str]] = Field(None, description=
        'A dictionary of custom attributes to filter by')
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
class CreateProjectRequest(BaseModel):
    name: Optional[str] = Field(None, description=
        'The name of the new project. Equals path if not provided.')
    path: Optional[str] = Field(None, description=
        'Repository name for new project. Generated based on name if not provided (generated as lowercase with dashes). Starting with GitLab 14.9, path must not start or end with a special character and must not contain consecutive special characters.'
        )
    allow_merge_on_skipped_pipeline: Optional[bool] = Field(None,
        description=
        'Set whether or not merge requests can be merged with skipped jobs.')
    only_allow_merge_if_all_status_checks_passed: Optional[bool] = Field(None,
        description=
        'Indicates that merges of merge requests should be blocked unless all status checks have passed. Defaults to false. Introduced in GitLab 15.5 with feature flag only_allow_merge_if_all_status_checks_passed disabled by default.'
        )
    analytics_access_level: Optional[str] = Field(None, description=
        'One of disabled, private or enabled.')
    approvals_before_merge: Optional[int] = Field(None, description=
        'How many approvers should approve merge requests by default. To configure approval rules, see Merge request approvals API. Deprecated in GitLab 16.0.'
        )
    auto_cancel_pending_pipelines: Optional[str] = Field(None, description=
        'Auto-cancel pending pipelines. This action toggles between an enabled state and a disabled state; it is not a boolean.'
        )
    auto_devops_deploy_strategy: Optional[str] = Field(None, description=
        'Auto Deploy strategy (continuous, manual or timed_incremental).')
    auto_devops_enabled: Optional[bool] = Field(None, description=
        'Enable Auto DevOps for this project.')
    autoclose_referenced_issues: Optional[bool] = Field(None, description=
        'Set whether auto-closing referenced issues on default branch.')
    avatar: Optional[Union[str, Any]] = Field(None, description=
        'Image file for avatar of the project.')
    build_git_strategy: Optional[str] = Field(None, description=
        'The Git strategy. Defaults to fetch.')
    build_timeout: Optional[int] = Field(None, description=
        'The maximum amount of time, in seconds, that a job can run.')
    builds_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    ci_config_path: Optional[str] = Field(None, description=
        'The path to CI configuration file.')
    container_expiration_policy_attributes: Optional[dict] = Field(None,
        description='Update the image cleanup policy for this project.')
    container_registry_access_level: Optional[str] = Field(None,
        description=
        'Set visibility of container registry, for this project, to one of disabled, private or enabled.'
        )
    container_registry_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable container registry for this project. Use container_registry_access_level instead.'
        )
    default_branch: Optional[str] = Field(None, description=
        'The default branch name. Requires initialize_with_readme to be true.')
    description: Optional[str] = Field(None, description=
        'Short project description.')
    emails_disabled: Optional[bool] = Field(None, description=
        'Disable email notifications.')
    external_authorization_classification_label: Optional[str] = Field(None,
        description='The classification label for the project.')
    forking_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    group_with_project_templates_id: Optional[int] = Field(None,
        description=
        'For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true.'
        )
    import_url: Optional[str] = Field(None, description=
        'URL to import repository from. When the URL value isn’t empty, you must not set initialize_with_readme to true. Doing so might result in the following error: not a git repository.'
        )
    initialize_with_readme: Optional[bool] = Field(None, description=
        'Whether to create a Git repository with just a README.md file. Default is false.'
        )
    issues_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    issues_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable issues for this project. Use issues_access_level instead.'
        )
    jobs_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable jobs for this project. Use builds_access_level instead.'
        )
    lfs_enabled: Optional[bool] = Field(None, description='Enable LFS.')
    merge_method: Optional[str] = Field(None, description=
        'Set the merge method used.')
    merge_pipelines_enabled: Optional[bool] = Field(None, description=
        'Enable or disable merge pipelines.')
    merge_requests_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    merge_requests_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable merge requests for this project. Use merge_requests_access_level instead.'
        )
    merge_trains_enabled: Optional[bool] = Field(None, description=
        'Enable or disable merge trains.')
    mirror_trigger_builds: Optional[bool] = Field(None, description=
        'Pull mirroring triggers builds.')
    mirror: Optional[bool] = Field(None, description=
        'Enables pull mirroring in a project.')
    namespace_id: Optional[int] = Field(None, description=
        'Namespace for the new project (defaults to the current user’s namespace).'
        )
    only_allow_merge_if_all_discussions_are_resolved: Optional[bool] = Field(
        None, description=
        'Set whether merge requests can only be merged when all the discussions are resolved.'
        )
    only_allow_merge_if_pipeline_succeeds: Optional[bool] = Field(None,
        description=
        'Set whether merge requests can only be merged with successful pipelines.'
        )
    packages_enabled: Optional[bool] = Field(None, description=
        'Enable or disable packages repository feature.')
    pages_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, enabled, or public.')
    printing_merge_request_link_enabled: Optional[bool] = Field(None,
        description=
        'Show link to create/view merge request when pushing from the command line.'
        )
    public_builds: Optional[bool] = Field(None, description=
        'If true, jobs can be viewed by non-project members.')
    releases_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    environments_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    feature_flags_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    infrastructure_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    monitor_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    remove_source_branch_after_merge: Optional[bool] = Field(None,
        description=
        'Enable Delete source branch option by default for all new merge requests.'
        )
    repository_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    repository_storage: Optional[str] = Field(None, description=
        'Which storage shard the repository is on. (administrator only)')
    request_access_enabled: Optional[bool] = Field(None, description=
        'Allow users to request member access.')
    requirements_access_level: Optional[str] = Field(None, description=
        'One of disabled, private or enabled')
    resolve_outdated_diff_discussions: Optional[bool] = Field(None,
        description=
        'Automatically resolve merge request diffs discussions on lines changed with a push.'
        )
    security_and_compliance_access_level: Optional[str] = Field(None,
        description=
        '(GitLab 14.9 and later) Security and compliance access level. One of disabled, private, or enabled.'
        )
    shared_runners_enabled: Optional[bool] = Field(None, description=
        'Enable shared runners for this project.')
    group_runners_enabled: Optional[bool] = Field(None, description=
        'Enable group runners for this project.')
    snippets_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    snippets_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable snippets for this project. Use snippets_access_level instead.'
        )
    squash_option: Optional[str] = Field(None, description=
        'One of never, always, default_on, or default_off.')
    tag_list: Optional[list] = Field(None, description=
        '(Deprecated in GitLab 14.0) The list of tags for a project; put array of tags, that should be finally assigned to a project. Use topics instead.'
        )
    template_name: Optional[str] = Field(None, description=
        'When used without use_custom_template, name of a built-in project template.'
        )
    template_project_id: Optional[int] = Field(None, description=
        'When used with use_custom_template, project ID of a custom project template.'
        )
    topics: Optional[list] = Field(None, description=
        'The list of topics for a project; put array of topics, that should be finally assigned to a project. (Introduced in GitLab 14.0.)'
        )
    use_custom_template: Optional[bool] = Field(None, description=
        'Use either custom instance or group (with group_with_project_templates_id) project template.'
        )
    visibility: Optional[str] = Field(None, description=
        'See project visibility level.')
    wiki_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    wiki_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable wiki for this project. Use wiki_access_level instead.'
        )
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
    container_expiration_policy_attributes: Optional[
        ContainerExpirationPolicyAttributes] = None
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

# Classes from file: merge_requests.py
class ProjectsMergeRequestCreate(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    source_branch: str = Field(description='The source branch name.')
    target_branch: str = Field(description='The target branch name.')
    title: str = Field(description='The title of merge request.')
    allow_collaboration: Optional[bool] = Field(None, description=
        'Allow commits from members who can merge to the target branch.')
    approvals_before_merge: Optional[int] = Field(None, description=
        'The amount of approvals required before merging.')
    allow_maintainer_to_push: Optional[bool] = Field(None, description=
        'Allow users who can merge to the target branch to push to the source branch.'
        )
    assignee_id: Optional[int] = Field(None, description=
        'The ID of a user to assign merge request.')
    assignee_ids: Optional[List[int]] = Field(None, description=
        'The IDs of users to assign merge request.')
    description: Optional[str] = Field(None, description=
        'The description of merge request.')
    labels: Optional[str] = Field(None, description=
        'Comma-separated list of label names.')
    milestone_id: Optional[int] = Field(None, description=
        'The global ID of a milestone to assign merge request.')
    remove_source_branch: Optional[bool] = Field(None, description=
        'Flag indicating if a merge request should remove the source branch when merging.'
        )
    reviewer_ids: Optional[List[int]] = Field(None, description=
        'The IDs of users to request review from when merge request created.')
    squash: Optional[bool] = Field(None, description=
        'Squash commits into a single commit when merging.')
    squash_on_merge: Optional[bool] = Field(None, description=
        'Squash commits into a single commit after merging.')
    target_project_id: Optional[int] = Field(None, description=
        'The target project ID. If the user is a maintainer of the target project, the source project is set as the target_project_id.'
        )

# Classes from file: member_roles.py

# Classes from file: resource_weight_events.py

# Classes from file: search_migrations.py

# Classes from file: integrations.py

# Classes from file: emoji_reactions.py
class AwardEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
class SingleEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class NewEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    name: str
class DeleteEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class ListCommentEmojiReactionsParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
class GetCommentEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int
class AwardCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    name: str
class DeleteCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int

# Classes from file: settings_(application).py

# Classes from file: pipelines.py
class Scope(str, Enum):
    running = 'running'
    pending = 'pending'
    finished = 'finished'
    branches = 'branches'
    tags = 'tags'
class Status(str, Enum):
    created = 'created'
    waiting_for_resource = 'waiting_for_resource'
    preparing = 'preparing'
    pending = 'pending'
    running = 'running'
    success = 'success'
    failed = 'failed'
    canceled = 'canceled'
    skipped = 'skipped'
    manual = 'manual'
    scheduled = 'scheduled'
class Source(str, Enum):
    push = 'push'
    web = 'web'
    trigger = 'trigger'
    schedule = 'schedule'
    api = 'api'
    external = 'external'
    pipeline = 'pipeline'
    chat = 'chat'
    webide = 'webide'
    merge_request_event = 'merge_request_event'
    external_pull_request_event = 'external_pull_request_event'
    parent_pipeline = 'parent_pipeline'
    ondemand_dast_scan = 'ondemand_dast_scan'
    ondemand_dast_validation = 'ondemand_dast_validation'
class OrderBy(str, Enum):
    id = 'id'
    status = 'status'
    ref = 'ref'
    updated_at = 'updated_at'
    user_id = 'user_id'
class Sort(str, Enum):
    asc = 'asc'
    desc = 'desc'
class ListProjectPipelinesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    scope: Optional[Scope]
    status: Optional[Status]
    source: Optional[Source]
    ref: Optional[str]
    sha: Optional[str]
    yaml_errors: Optional[bool]
    username: Optional[str]
    updated_after: Optional[datetime]
    updated_before: Optional[datetime]
    name: Optional[str]
    order_by: Optional[OrderBy]
    sort: Optional[Sort]
class GetPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineVariablesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportSummaryInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetLatestPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    ref: Optional[str] = Field(None, description=
        'The branch or tag to check for the latest pipeline. Defaults to the default branch when not specified.'
        )
class CreatePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    ref: str = Field(..., description=
        'The branch or tag to run the pipeline on.')
    variables: Optional[List[Dict[str, Union[str, Dict[str, str]]]]] = Field(
        None, description=
        'An array of hashes containing the variables available in the pipeline.'
        )
class RetryJobsInPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class CancelPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class DeletePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')

# Classes from file: lint_.gitlab_ci.yml.py

# Classes from file: service_data.py

# Classes from file: dependencies.py
class ProjectsIdDependencies(BaseModel):
    id: Union[int, str]
    package_manager: Optional[str] = None

# Classes from file: project_badges.py
class ProjectsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class ProjectsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesCreate(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str

# Classes from file: helm.py

# Classes from file: namespaces.py

# Classes from file: links_(issue).py

# Classes from file: deploy_keys.py
class Deploykeys(BaseModel):
    public: Optional[bool] = None
class ProjectsIdDeploykeys(BaseModel):
    id: int
class UsersIdorusernameProjectdeploykeys(BaseModel):
    id_or_username: str
class ProjectsIdDeploykeysKeyidSingle(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysAdd(BaseModel):
    id: int
    key: str
    title: str
    can_push: Optional[bool] = None
    expires_at: Optional[datetime] = None
class ProjectsIdDeploykeysKeyidUpdate(BaseModel):
    id: int
    can_push: Optional[bool] = None
    title: Optional[str] = None
class ProjectsIdDeploykeysKeyidDelete(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysKeyidEnable(BaseModel):
    id: int
    key_id: int

# Classes from file: issue_boards_(project).py

# Classes from file: job_token_scopes.py
class GetProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
class PatchProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
    enabled: bool
class GetProjectCICDJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
class CreateNewProjectToJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int
class RemoveProjectFromJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int

# Classes from file: merge_request_context_commits.py

# Classes from file: system_hooks.py

# Classes from file: user_starred_metrics_dashboards.py
class ProjectsIdMetricsUserstarreddashboardsAdd(BaseModel):
    id: Union[int, str]
    dashboard_path: str
class ProjectsIdMetricsUserstarreddashboardsRemove(BaseModel):
    id: Union[int, str]
    dashboard_path: Optional[str] = None

# Classes from file: secure_files.py

# Classes from file: issues.py

# Classes from file: labels_(group).py

# Classes from file: tags.py

# Classes from file: release_links.py

# Classes from file: import.py

# Classes from file: pages_domains.py

# Classes from file: pipeline_triggers.py
class ListProjectTriggerTokensInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
class GetTriggerTokenDetailsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class CreateTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    description: str = Field(..., description='The trigger name.')
class UpdateProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
    description: Optional[str] = Field(None, description='The trigger name.')
class RemoveProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class TriggerPipelineWithTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    ref: str = Field(..., description=
        'The branch or tag to run the pipeline on.')
    token: str = Field(..., description='The trigger token or CI/CD job token.'
        )
    variables: Optional[Dict[str, str]] = Field(None, description=
        'A map of key-valued strings containing the pipeline variables.')

# Classes from file: linked_epics.py

# Classes from file: resource_state_events.py

# Classes from file: project_remote_mirrors.py

# Classes from file: to_do_lists.py

# Classes from file: deploy_tokens.py

# Classes from file: dashboard_annotations.py
class CreateNewAnnotation(BaseModel):
    id: Union[int, str]
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str] = None
    description: str

    @validator('starting_at', 'ending_at', pre=True)
    def parse_iso8601(cls, v):
        if v is None:
            return v
        try:
            return datetime.fromisoformat(v)
        except ValueError:
            raise ValueError('datetime is not in ISO 8601 format')

# Classes from file: geo_nodes.py

# Classes from file: merge_request_approvals.py

# Classes from file: conan.py
class RoutePrefix(str, Enum):
    instance_level = '/packages/conan/v1'
    project_level = '/projects/:id/packages/conan/v1`'
class Ping(BaseModel):
    route_prefix: RoutePrefix = Field(description=
        'pick either instance_level or project_level')
class SearchInput(BaseModel):
    route_prefix: RoutePrefix
    q: str = Field(..., description=
        'Search query. You can use * as a wildcard.')
class AuthenticateInput(BaseModel):
    route_prefix: RoutePrefix
class CheckCredentialsInput(BaseModel):
    route_prefix: RoutePrefix
class RecipeSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifest(BaseModel):
    package_name: str = Field(description='Name of a package.')
    package_version: str = Field(description='Version of a package.')
    package_username: str = Field(description=
        'Conan username of a package. This attribute is the +-separated full path of your project.'
        )
    package_channel: str = Field(description='Channel of a package.')
class PackageManifest(RecipeManifest):
    conan_package_reference: str = Field(description=
        'Reference hash of a Conan package. Conan generates this value.')
class UploadUrls(RecipeManifest):
    files: Dict[str, int] = Field(description=
        'Dictionary of file names with their sizes.')
class PackageUploadUrlsInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
    file_sizes: Dict[str, int]
class DownloadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
class UploadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
    file_content: str
class DownloadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
class UploadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
    file_content: str
class DeletePackageInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str

# Classes from file: custom_attributes.py
class UsersIdCustomattributes(BaseModel):
    id: int
class GroupsIdCustomattributes(BaseModel):
    id: int
class ProjectsIdCustomattributes(BaseModel):
    id: int
class UsersIdCustomattributesKey(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class UsersIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class GroupsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class ProjectsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class UsersIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str

# Classes from file: epics.py
class NotMatch(BaseModel):
    author_id: Optional[int] = Field(None, description=
        'Can exclude by author ID')
    author_username: Optional[str] = Field(None, description=
        'Can exclude by author username (GitLab 14.7 and later)')
    labels: Optional[str] = Field(None, description='Can exclude by labels')
class GroupsIdEpics(BaseModel):
    id: Union[int, str]
    author_id: Optional[int] = None
    author_username: Optional[str] = None
    labels: Optional[str] = None
    with_labels_details: Optional[bool] = None
    order_by: Optional[str] = None
    sort: Optional[str] = None
    search: Optional[str] = None
    state: Optional[str] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    include_ancestor_groups: Optional[bool] = None
    include_descendant_groups: Optional[bool] = None
    my_reaction_emoji: Optional[str] = None
    not_: Optional[NotMatch] = Field(None, alias='not', description=
        'Return epics that do not match the parameters supplied')
class SingleEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class NewEpicInput(BaseModel):
    id: Union[int, str]
    title: str
    labels: Optional[str]
    description: Optional[str]
    color: Optional[str]
    confidential: Optional[bool]
    created_at: Optional[datetime]
    start_date_is_fixed: Optional[bool]
    start_date_fixed: Optional[str]
    due_date_is_fixed: Optional[bool]
    due_date_fixed: Optional[str]
    parent_id: Optional[Union[int, str]]
class UpdateEpic(BaseModel):
    id: int
    epic_iid: int
    add_labels: Optional[str] = None
    confidential: Optional[bool] = None
    description: Optional[str] = None
    due_date_fixed: Optional[str] = None
    due_date_is_fixed: Optional[bool] = None
    labels: Optional[str] = None
    parent_id: Optional[int] = None
    remove_labels: Optional[str] = None
    start_date_fixed: Optional[str] = None
    start_date_is_fixed: Optional[bool] = None
    state_event: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
class DeleteEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class CreateAToDoItem(BaseModel):
    id: Union[int, str]
    epic_iid: int

# Classes from file: issues_(epic).py

# Classes from file: suggestions.py

# Classes from file: product_analytics.py

# Classes from file: discussions.py
class ListProjectIssueDiscussionItems(BaseModel):
    id: Union[int, str]
    issue_iid: int
class GetSingleIssueDiscussionItem(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
class CreateNewIssueThread(BaseModel):
    body: str
    id: Union[int, str]
    issue_iid: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingIssueThreadPayload(BaseModel):
    body: str = Field(..., description='The content of the note or reply.')
    discussion_id: int = Field(..., description='The ID of a thread.')
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    issue_iid: int = Field(..., description='The IID of an issue.')
    note_id: int = Field(..., description='The ID of a thread note.')
    created_at: Optional[datetime] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyExistingIssueThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    issue_iid: int
    note_id: int
class DeleteIssueThreadNote(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
    note_id: int
class ProjectsIdSnippetsSnippetidDiscussions(BaseModel):
    id: Union[int, str]
    snippet_id: int
class ListProjectSnippetDiscussionItems(BaseModel):
    id: Union[int, str]
    snippet_id: int
class GetSingleSnippetDiscussionItem(BaseModel):
    id: Union[int, str]
    snippet_id: int
    discussion_id: int
class CreateNewSnippetThread(BaseModel):
    body: str
    id: Union[int, str]
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingSnippetThread(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class ModifyExistingSnippetThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class DeleteSnippetThreadNote(BaseModel):
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class GroupsIdEpicsEpicidDiscussions(BaseModel):
    epic_id: int
    id: Union[int, str]
class SingleEpicDiscussionItem(BaseModel):
    discussion_id: int = Field(description='The ID of a discussion item.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
class CreateNewEpicThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    created_at: Optional[Union[str, datetime]] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class AddNoteToEpicThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[Union[str, datetime]] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyEpicThreadNote(BaseModel):
    body: str = Field(description='The content of note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class DeleteEpicThreadNote(BaseModel):
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class ListMergeRequestDiscussionItems(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class SingleMergeRequestDiscussionItem(BaseModel):
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class BasicMergeRequestParams(BaseModel):
    body: str = Field(description='The content of the thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class DiffNoteParams(BaseModel):
    base_sha: str = Field(description='Base commit SHA in the source branch.')
    head_sha: str = Field(description=
        'SHA referencing HEAD of this merge request.')
    start_sha: str = Field(description=
        'SHA referencing commit in target branch.')
    new_path: str = Field(description='File path after change.')
    old_path: str = Field(description='File path before change.')
    position_type: str = Field(description=
        'Type of the position reference. Allowed values: text or image.')
class TextDiffNoteParams(BaseModel):
    new_line: Optional[int] = Field(description=
        'For text diff notes, the line number after change.')
    old_line: Optional[int] = Field(description=
        'For text diff notes, the line number before change.')
class ImageDiffNoteParams(BaseModel):
    width: Optional[int] = Field(description=
        'For image diff notes, width of the image.')
    height: Optional[int] = Field(description=
        'For image diff notes, height of the image.')
    x: Optional[float] = Field(description=
        'For image diff notes, X coordinate.')
    y: Optional[float] = Field(description=
        'For image diff notes, Y coordinate.')
class MultilineCommentsParams(BaseModel):
    line_range: dict = Field(description=
        'Line range for a multi-line diff note.')
class CreateNewMergeRequestThread(BasicMergeRequestParams):
    position: DiffNoteParams = Field(description=
        'Position when creating a diff note.')
    text_position: Optional[TextDiffNoteParams] = Field(description=
        'Position parameters for text diff notes.')
    image_position: Optional[ImageDiffNoteParams] = Field(description=
        'Position parameters for image diff notes.')
    multiline_comments: Optional[MultilineCommentsParams] = Field(description
        ='Parameters for multiline comments.')
    commit_id: Optional[str] = Field(description=
        'SHA referencing commit to start this thread on.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class ResolveMergeRequestThread(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    discussion_id: str = Field(description='The ID of a thread.')
    resolved: bool = Field(description='Resolve or unresolve the discussion.')
class AddNoteToMergeRequestThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    discussion_id: str = Field(description='The ID of a thread.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class ModifyMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description=
        'The content of the note or reply. Exactly one of body or resolved must be set.'
        )
    resolved: Optional[bool] = Field(description=
        'Resolve or unresolve the note. Exactly one of body or resolved must be set.'
        )
class DeleteMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
class ListProjectCommitDiscussionItems(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
class GetSingleCommitDiscussionItem(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
class Position(BaseModel):
    base_sha: str = Field(description='SHA of the parent commit.')
    head_sha: str = Field(description=
        'The SHA of this commit. Same as commit_id.')
    start_sha: str = Field(description='SHA of the parent commit.')
    position_type: str = Field(description=
        'Type of the position reference. Allowed values: text or image.')
    hash: Optional[str] = Field(description=
        'Position when creating a diff note.')
    new_path: Optional[str] = Field(description='File path after change.')
    new_line: Optional[int] = Field(description='Line number after change.')
    old_path: Optional[str] = Field(description='File path before change.')
    old_line: Optional[int] = Field(description='Line number before change.')
    height: Optional[int] = Field(description=
        'For image diff notes, image height.')
    width: Optional[int] = Field(description=
        'For image diff notes, image width.')
    x: Optional[int] = Field(description='For image diff notes, X coordinate.')
    y: Optional[int] = Field(description='For image diff notes, Y coordinate.')
class CreateNewCommitThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    position: Position = Field(description=
        'Position when creating a diff note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class AddNoteToCommitThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyCommitThreadNote(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description='The content of a note.')
class DeleteCommitThreadNote(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    note_id: int = Field(description='The ID of a thread note.')

# Classes from file: project_relations_export.py

# Classes from file: snippets_(project).py

# Classes from file: branches.py
class ProjectsIdRepositoryBranches(BaseModel):
    id: int
    search: Optional[str] = None
    regex: Optional[str] = None
class ProjectsIdRepositoryBranchesBranchSingle(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryBranchesCreate(BaseModel):
    id: int
    branch: str
    ref: str
class ProjectsIdRepositoryBranchesBranch(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryMergedbranches(BaseModel):
    id: int

# Classes from file: metadata.py

# Classes from file: version.py

# Classes from file: protected_tags.py

# Classes from file: issue_boards_(group).py

# Classes from file: repository_submodules.py

# Classes from file: milestones_(group).py

# Classes from file: members.py

# Classes from file: protected_branches.py

# Classes from file: commits.py
class ProjectsIdRepositoryCommits(BaseModel):
    id: int
    ref_name: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None
    path: Optional[str] = None
    author: Optional[str] = None
    all: Optional[bool]
    with_stats: Optional[bool]
    first_parent: Optional[bool]
    order: Optional[str]
    trailers: Optional[bool]
class ProjectsIdRepositoryCommitsSha(BaseModel):
    id: int
    sha: str
    stats: Optional[bool] = None
class ProjectsIdRepositoryCommitsShaRefs(BaseModel):
    id: int
    sha: str
    type: Optional[str] = None
class ProjectsIdRepositoryCommitsShaCherrypick(BaseModel):
    id: int
    sha: str
    branch: str
    dry_run: Optional[bool] = None
    message: Optional[str] = None
class ProjectsIdRepositoryCommitsShaRevert(BaseModel):
    id: int
    sha: str
    branch: str
    dry_run: Optional[bool] = None
class ProjectsIdRepositoryCommitsShaDiff(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaComments(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaCommentsPost(BaseModel):
    id: int
    sha: str
    note: str
    path: Optional[str] = None
    line: Optional[int] = None
    line_type: Optional[str] = None
class ProjectsIdRepositoryCommitsShaDiscussions(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaStatuses(BaseModel):
    id: int
    sha: str
    ref: Optional[str] = None
    stage: Optional[str] = None
    name: Optional[str] = None
    all: Optional[bool] = None
class ProjectsIdStatusesSha(BaseModel):
    id: int
    sha: str
    state: str
    ref: Optional[str] = None
    context: Optional[str] = None
    name: Optional[str] = None
    target_url: Optional[str] = None
    description: Optional[str] = None
    coverage: Optional[float] = None
    pipeline_id: Optional[int] = None
class ProjectsIdRepositoryCommitsShaMergerequests(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaSignature(BaseModel):
    id: int
    sha: str

# Classes from file: application_appearance.py
class ApplicationAppearance(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    pwa_name: Optional[str] = None
    pwa_short_name: Optional[str] = None
    pwa_description: Optional[str] = None
    pwa_icon: Optional[Any] = None
    logo: Optional[Any] = None
    header_logo: Optional[Any] = None
    favicon: Optional[Any] = None
    new_project_guidelines: Optional[str] = None
    profile_image_guidelines: Optional[str] = None
    header_message: Optional[str] = None
    footer_message: Optional[str] = None
    message_background_color: Optional[str] = None
    message_font_color: Optional[str] = None
    email_header_and_footer_enabled: Optional[bool] = None
class ChangeLogo(BaseModel):
    logo: Any
    pwa_icon: Any

# Classes from file: users.py

# Classes from file: project_vulnerabilities.py

# Classes from file: draft_notes.py
class ProjectsIdMergerequestsMergerequestiidDraftnotes(BaseModel):
    id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidSingle(
    BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesCreate(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    note: str
    commit_id: Optional[str] = None
    in_reply_to_discussion_id: Optional[int] = None
    resolve_discussion: Optional[bool] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidModify(
    BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
    note: Optional[str] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidDelete(
    BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidPublish(
    BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesBulkpublish(BaseModel):
    id: Union[int, str]
    merge_request_iid: int

# Classes from file: group_migration_by_direct_transfer.py

# Classes from file: resource_iteration_events.py

# Classes from file: agents_for_kubernetes.py
class ListTheAgentsForAProject(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
class GetDetailsAboutAnAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class RegisterAnAgentWithAProject(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    name: str = Field(description='Name for the agent')
class DeleteARegisteredAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class ListTokensForAnAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class GetSingleAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')
class CreateAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    name: int = Field(description='Name for the token')
    description: Optional[int] = Field(None, description=
        'Description for the token')
class RevokeAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')

# Classes from file: project_import_export.py

# Classes from file: project_level_protected_environments.py

# Classes from file: composer.py
class GroupIdPackagesComposerPackages(BaseModel):
    id: Union[int, str]
class GroupIdPackagesComposerPSha(BaseModel):
    id: Union[int, str]
    sha: str
class V1PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str
class V2PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
class CreateAPackageInput(BaseModel):
    id: Union[int, str]
    tag: Optional[str] = None
    branch: Optional[str] = None
class ProjectsIdPackagesComposerArchivesPackagename(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str

# Classes from file: alert_management.py
class ListMetricImages(BaseModel):
    id: int
    alert_iid: int
class UpdateMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int
    url: Optional[str] = None
    url_text: Optional[str] = None
class DeleteMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int

# Classes from file: sidekiq_queues.py

# Classes from file: vulnerability_export.py
class SecurityProjectsIdVulnerabilityexports(BaseModel):
    id: Union[int, str]
class SecurityGroupsIdVulnerabilityexports(BaseModel):
    id: Union[int, str]
class SecurityVulnerabilityexportsId(BaseModel):
    id: Union[int, str]
class SecurityVulnerabilityexportsIdDownload(BaseModel):
    id: Union[int, str]

# Classes from file: events.py
class Events(BaseModel):
    action: Optional[str] = None
    target_type: Optional[str] = None
    before: Optional[datetime] = Field(None, description=
        'Include only events created before a certain date.')
    after: Optional[datetime] = Field(None, description=
        'Include only events created after a particular date.')
    target_id: Optional[int] = None
    author_id: Optional[int] = None
    search: Optional[str] = None
class AuthenticatedUserEvents(Events):
    scope: Optional[str] = None
    sort: Optional[str] = None
class UserContributionEvents(Events):
    id: int
    sort: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
class ProjectVisibleEvents(Events):
    project_id: int
    sort: Optional[str] = None

# Classes from file: group_import_export.py

# Classes from file: dora4_metrics.py
class ProjectsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None
class GroupsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None

# Classes from file: plan_limits.py

# Classes from file: statistics_(application).py

# Classes from file: group_repository_storage_moves.py

# Classes from file: iterations_(project).py

# Classes from file: applications.py
class Applications(BaseModel):
    name: str
    redirect_uri: str
    scopes: str
    confidential: Optional[bool] = None
class ApplicationsId(BaseModel):
    id: int

# Classes from file: saml.py

# Classes from file: dependency_proxy.py
class GroupsIdDependencyproxyCache(BaseModel):
    id: int

# Classes from file: group_relations_export.py

# Classes from file: metrics_dashboard_annotations.py
class EnvironmentsIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str
class ClustersIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str

# Classes from file: personal_access_tokens.py

# Classes from file: __init__.py

# Classes from file: instance_level_ci_cd_variables.py

# Classes from file: geo_sites.py

# Classes from file: visual_review_discussions_deprecated.py
class PositionData(BaseModel):
    base_sha: str
    start_sha: str
    head_sha: str
    position_type: str
    new_path: Optional[str] = None
    new_line: Optional[int] = None
    old_path: Optional[str] = None
    old_line: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None
class CreateNewMergeRequestThread(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    body: str
    position: Optional[PositionData] = None

# Classes from file: feature_flags.py
class StrategyParameters(BaseModel):
    pass
class StrategyScope(BaseModel):
    environment_scope: Optional[str] = None
class Strategy(BaseModel):
    name: Optional[str] = None
    parameters: Optional[StrategyParameters] = None
    scopes: Optional[List[StrategyScope]] = None
class ListFeatureFlagsForProject(BaseModel):
    id: Union[int, str]
    scope: Optional[str] = None
class GetSingleFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
class CreateFeatureFlag(BaseModel):
    id: Union[int, str]
    name: str
    version: str
    description: Optional[str] = None
    active: Optional[bool] = None
    strategies: Optional[List[Strategy]] = None
class UpdateFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
    description: Optional[str] = None
    active: Optional[bool] = None
    name: Optional[str] = None
    strategies: Optional[List[Strategy]] = None
class DeleteFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str

# Classes from file: pipelines_schedules.py
class GetAllPipelineSchedulesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    scope: Optional[str] = Field(None, description=
        'The scope of pipeline schedules, must be one of: active, inactive.')
class GetSinglePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class GetPipelinesTriggeredByScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class CreateNewPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    description: str = Field(..., description=
        'The description of the pipeline schedule.')
    ref: str = Field(..., description=
        'The branch or tag name that is triggered.')
    cron: str = Field(..., description=
        'The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description=
        'The time zone supported by ActiveSupport::TimeZone, for example: Pacific Time (US & Canada) (default: UTC).'
        )
    active: Optional[bool] = Field(None, description=
        'The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated (default: true).'
        )
class EditPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    description: Optional[str] = Field(None, description=
        'The description of the pipeline schedule.')
    ref: Optional[str] = Field(None, description=
        'The branch or tag name that is triggered.')
    cron: Optional[str] = Field(None, description=
        'The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description=
        'The time zone supported by ActiveSupport::TimeZone (for example Pacific Time (US & Canada)), or TZInfo::Timezone (for example America/Los_Angeles).'
        )
    active: Optional[bool] = Field(None, description=
        'The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated.'
        )
class TakeOwnershipOfPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class DeletePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class RunScheduledPipelineImmediatelyInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class CreatePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description=
        'The key of a variable; must have no more than 255 characters; only A-Z, a-z, 0-9, and _ are allowed.'
        )
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description=
        'The type of a variable. Available types are: env_var (default) and file.'
        )
class EditPipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description=
        'The type of a variable. Available types are: env_var (default) and file.'
        )
class DeletePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')

# Classes from file: dockerfile_templates.py
class TemplatesDockerfilesKey(BaseModel):
    key: str

# Classes from file: group_releases.py

# Classes from file: keys.py

# Classes from file: packages.py

# Classes from file: labels_(project).py

# Classes from file: freeze_periods.py

# Classes from file: broadcast_messages.py
class GetASpecificBroadcastMessage(BaseModel):
    id: int
class CreateABroadcastMessage(BaseModel):
    message: str
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class UpdateABroadcastMessage(BaseModel):
    id: int
    message: Optional[str]
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class DeleteABroadcastMessage(BaseModel):
    id: int

# Classes from file: groups.py

# Classes from file: wikis_project.py
class ProjectsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class ProjectsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class ProjectsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class ProjectsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class ProjectsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None

# Classes from file: npm.py

# Classes from file: avatar.py
class Avatar(BaseModel):
    email: str
    size: Optional[int] = None

# Classes from file: resource_group.py

# Classes from file: error_tracking.py
class GetErrorTrackingSettings(BaseModel):
    id: Union[int, str]
class CreateErrorTrackingSettings(BaseModel):
    id: int
    active: bool
    integrated: bool
class EnableOrDisableTheErrorTrackingProjectSettings(BaseModel):
    id: int
    active: bool
    integrated: Optional[bool] = None
class ListProjectClientKeys(BaseModel):
    id: Union[int, str]
class CreateAClientKey(BaseModel):
    id: Union[int, str]
class DeleteAClientKey(BaseModel):
    id: Union[int, str]
    key_id: int

# Classes from file: debian_project_distributions.py
class ListAllDebianDistributionsInAProject(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class SingleDebianProjectDistributionKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int

# Classes from file: resource_label_events.py

# Classes from file: repository_files.py
class ProjectIdRepositoryFiles(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    file_path: str = Field(description='URL encoded full path to new file')
    ref: str = Field(description='The name of branch, tag or commit')
class ProjectIdRepositoryFilesBlame(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    file_path: str = Field(description=
        'URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(description='The name of branch, tag or commit.')
    range_start: int = Field(description=
        'The first line of the range to blame.')
    range_end: int = Field(description='The last line of the range to blame.')
    range: Optional[dict] = Field(description='Blame range.')
class ProjectsIdRepositoryFilesFilepathRaw(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    file_path: str = Field(..., description=
        'URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(..., description=
        'The name of branch, tag or commit. Default is the HEAD of the project.'
        )
    lfs: Optional[bool] = Field(None, description=
        'Determines if the response should be Git LFS file contents, rather than the pointer. If the file is not tracked by Git LFS, ignored. Defaults to false.'
        )
class ProjectsIdRepositoryFilesFilepathCreate(BaseModel):
    branch: str = Field(description=
        'Name of the new branch to create. The commit is added to this branch.'
        )
    commit_message: str = Field(description='The commit message.')
    content: str = Field(description='The file’s content.')
    file_path: str = Field(description=
        'URL-encoded full path to new file. For example: lib%2Fclass%2Erb.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    author_email: Optional[str] = Field(None, description=
        'The commit author’s email address.')
    author_name: Optional[str] = Field(None, description=
        'The commit author’s name.')
    encoding: Optional[str] = Field(None, description=
        'Change encoding to base64. Default is text.')
    execute_filemode: Optional[bool] = Field(None, description=
        'Enables or disables the execute flag on the file. Can be true or false.'
        )
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathUpdate(BaseModel):
    branch: str
    commit_message: str
    content: str
    file_path: str
    id: Union[int, str]
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    encoding: Optional[str] = None
    execute_filemode: Optional[bool] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathDelete(BaseModel):
    branch: str
    commit_message: str
    file_path: str
    id: int
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositorySubmodulesSubmodule(BaseModel):
    id: int
    submodule: str
    branch: str
    commit_sha: str
    commit_message: Optional[str] = None

# Classes from file: nuget.py

# Classes from file: container_registry.py
class ContainerRegistryAccessLevelEnum(str, Enum):
    enabled = 'enabled'
    private = 'private'
    disabled = 'disabled'
class ChangeContainerRegistryVisibility(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project accessible by the authenticated user.'
        )
    container_registry_access_level: Optional[ContainerRegistryAccessLevelEnum
        ] = Field(default=None, description=
        'The desired visibility of the Container Registry. One of enabled (default), private, or disabled.'
        )
class ListProjectRegistryRepositories(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
class GroupsIdRegistryRepositories(BaseModel):
    id: Union[int, str]
class RegistryRepositoriesId(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
    size: Optional[bool] = None
class ProjectsIdRegistryRepositoriesRepositoryid(BaseModel):
    id: Union[int, str]
    repository_id: int
class ProjectsIdRegistryRepositoriesRepositoryidTags(BaseModel):
    id: Union[int, str]
    repository_id: int
class GetDetailsOfARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteRegistryRepositoryTagsInBulk(BaseModel):
    id: Union[int, str]
    repository_id: int
    name_regex: Optional[str] = None
    name_regex_delete: str
    name_regex_keep: Optional[str] = None
    keep_n: Optional[int] = None
    older_than: Optional[str] = None
class ObtainTokenInput(BaseModel):
    CI_SERVER_URL: str = Field(description='CI server URL.')
    service: str = Field(default='container_registry', description=
        'The service type.')
    scope: str = Field(description='Scope for the token.')
class DeleteImageTagsByReferenceInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    CI_REGISTRY_IMAGE: str = Field(description='The registry image.')
    CI_COMMIT_SHORT_SHA: str = Field(description='The commit SHA.')
class ListAllContainerRepositoriesInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    admin_username: str = Field(description='The admin username.')
    admin_password: str = Field(description='The admin password.')
    service: str = Field(default='container_registry', description=
        'The service type.')
    scope: str = Field(default='registry:catalog:*', description=
        'Scope for the token.')

# Classes from file: resource_milestone_events.py

# Classes from file: templates.py
class TemplatesGitignoresKey(BaseModel):
    key: str
class TemplatesGitlabciymlsKey(BaseModel):
    key: str

# Classes from file: jobs.py
class JobScope(str, Enum):
    created = 'created'
    pending = 'pending'
    running = 'running'
    failed = 'failed'
    success = 'success'
    canceled = 'canceled'
    skipped = 'skipped'
    waiting_for_resource = 'waiting_for_resource'
    manual = 'manual'
class ListProjectJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
class ListPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
    include_retried: Optional[bool] = Field(False, description=
        'Include retried jobs in the response.')
class ListPipelineTriggerJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
class GetAllowedAgentsInput(BaseModel):
    CI_JOB_TOKEN: str = Field(..., description=
        'Token value associated with the GitLab-provided CI_JOB_TOKEN variable.'
        )
class GetSingleJobInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='ID of a job.')
class JobInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='The ID of a job.')
class JobVariable(BaseModel):
    key: str = Field(..., description='The key of the job variable.')
    value: str = Field(..., description='The value of the job variable.')
class RunJobInput(JobInput):
    job_variables_attributes: Optional[List[JobVariable]] = Field(None,
        description=
        'An array containing the custom variables available to the job.')

# Classes from file: gitignore.py
class ListAllGitignoreTemplates(BaseModel):
    pass
class GetSingleGitignoreTemplate(BaseModel):
    key: str

# Classes from file: releases.py

# Classes from file: gitlab_ci_yaml.py
class ListAllCICDYamlTemplates(BaseModel):
    pass
class GetSingleCICDYamlTemplate(BaseModel):
    key: str

# Classes from file: milestones_(project).py

# Classes from file: group_activity_analytics.py

# Classes from file: job_artifacts.py
class GetJobArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int
    job_token: Optional[str] = None
class DownloadArtifacts(BaseModel):
    id: Union[int, str]
    ref_name: str
    job: str
    job_token: Optional[str] = None
class DownloadSingleArtifactByJobID(BaseModel):
    id: Union[int, str]
    job_id: int
    artifact_path: str
    job_token: Optional[str] = None
class DownloadSingleArtifactFromSpecificTag(BaseModel):
    id: Union[int, str]
    ref_name: str
    artifact_path: str
    job: str
    job_token: Optional[str] = None
class KeepArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int

# Classes from file: issues_statistics.py

# Classes from file: project_statistics.py

# Classes from file: experiments.py
class ListAllExperiments(BaseModel):
    pass

# Classes from file: scim.py

# Classes from file: feature_flag_user_lists.py

# Classes from file: vulnerability_findings.py
class ProjectsIdVulnerabilityfindings(BaseModel):
    id: int
    report_type: Optional[List[str]] = None
    scope: Optional[str] = None
    severity: Optional[List[str]] = None
    confidence: Optional[List[str]] = None
    pipeline_id: int

# Classes from file: licenses_(templates).py

# Classes from file: topics.py

# Classes from file: secrets.py

# Classes from file: debian.py
class ProjectsIdPackagesDebianFilename(BaseModel):
    id: str
    file_name: str
    distribution: Optional[str] = None
    component: Optional[str] = None
class ProjectsIdPackagesDebianPoolDistributionLetterPackagenamePackageversionFilename(
    BaseModel):
    distribution: str
    letter: str
    package_name: str
    package_version: str
    file_name: str
class DownloadADistributionReleaseFile(BaseModel):
    distribution: str
class DownloadASignedDistributionReleaseFile(BaseModel):
    distribution: str
class DownloadAReleaseFileSignature(BaseModel):
    distribution: str
class DownloadAPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadAPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadADebianInstallerPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DowloadADebianInstallerPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadASourcePackagesIndex(BaseModel):
    distribution: str
    component: str
class DownloadASourcePackagesIndexByHash(BaseModel):
    distribution: str
    component: str

# Classes from file: ruby_gems.py

# Classes from file: markdown.py

# Classes from file: debian_group_distributions.py
class ListAllDebianDistributionsInAGroup(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class GroupsIdDebiandistributionsCodenameKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int

# Classes from file: variables_project.py
class Variable(BaseModel):
    key: str
    value: str
    variable_type: Optional[str] = 'env_var'
    protected: Optional[bool] = False
    masked: Optional[bool] = False
    raw: Optional[bool] = False
    environment_scope: Optional[str] = '*'
    description: Optional[str] = None
class VariableFilter(BaseModel):
    environment_scope: Optional[str] = None
class GetProjectVariables(BaseModel):
    id: Union[int, str]
class GetVariable(BaseModel):
    id: Union[int, str]
    key: str
    filter: Optional[VariableFilter] = None
class CreateVariable(GetProjectVariables, Variable):
    pass
class UpdateVariable(GetVariable, Variable):
    pass
class DeleteVariable(GetVariable):
    pass

# Classes from file: links_(epic).py

# Classes from file: wikis_group.py
class GroupsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class GroupsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class GroupsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class GroupsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class GroupsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None

# Classes from file: audit_events.py
class Auditevents(BaseModel):
    created_after: Optional[str] = None
    created_before: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[int] = None
class AuditeventsId(BaseModel):
    id: int
class GroupsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class GroupsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int
class ProjectsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class ProjectsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int

# Classes from file: project_access_tokens.py

# Classes from file: runners.py

# Classes from file: environments.py
class ProjectsIdEnvironments(BaseModel):
    id: int
    name: Optional[str] = None
    search: Optional[str] = None
    states: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentid(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsCreate(BaseModel):
    id: int
    name: str
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentsid(BaseModel):
    id: int
    environment_id: int
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentidDelete(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsReviewapps(BaseModel):
    id: int
    before: Optional[datetime] = None
    limit: Optional[int] = None
    dry_run: Optional[bool] = None
class ProjectsIdEnvironmentsEnvironmentidStop(BaseModel):
    id: int
    environment_id: int
    force: Optional[bool] = None
class ProjectsIdEnvironmentsStopstale(BaseModel):
    id: int
    before: datetime

# Classes from file: group_level_protected_branches.py

# Classes from file: http_wrapper.py

# Classes from file: gitlab_pages.py

# Classes from file: marketplace.py

# Classes from file: snippets.py

# Classes from file: notes_(comments).py

# Classes from file: terraform_registry.py

# Classes from file: repositories.py
class ProjectsIdRepositoryTree(BaseModel):
    id: int
    page_token: Optional[str] = None
    pagination: Optional[str] = None
    path: Optional[str] = None
    per_page: Optional[str] = None
    recursive: bool = Field(False)
    ref: Optional[str] = None
class ProjectsIdRepositoryBlobsSha(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryBlobsShaRaw(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryArchive(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    path: Optional[str] = Field(None, description=
        'The subpath of the repository to download. Defaults to the whole repository.'
        )
    sha: Optional[str] = Field(None, description=
        'The commit SHA to download. A tag, branch reference, or SHA can be used. Defaults to the tip of the default branch.'
        )
    format: Optional[str] = Field(None, description=
        "The archive format. Options are: 'bz2', 'tar', 'tar.bz2', 'tar.gz', 'tb2', 'tbz', 'tbz2', 'zip'. Defaults to 'tar.gz'."
        )
class ProjectsIdRepositoryCompare(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    from_commit_or_branch: str = Field(..., alias='from', description=
        'The commit SHA or branch name.')
    to: str = Field(..., description='The commit SHA or branch name.')
    from_project_id: Optional[int] = Field(None, description=
        'The ID to compare from.')
    straight: Optional[bool] = Field(False, description=
        'Comparison method: true for direct comparison between from and to (from..to), false to compare using merge base (from…to)’. Default is false.'
        )
class ProjectsIdRepositoryContributors(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    order_by: Optional[str] = Field(None, description=
        'Return contributors ordered by name, email, or commits (orders by commit date) fields. Default is commits.'
        )
    sort: Optional[str] = Field(None, description=
        'Return contributors sorted in asc or desc order. Default is asc.')
class ProjectsIdRepositoryMergebase(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    refs: List[str] = Field(description=
        'The refs to find the common ancestor of. Accepts multiple refs.')
class ProjectsIdRepositoryChangelog(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    version: str = Field(description=
        'The version to generate the changelog for. The format must follow semantic versioning.'
        )
    branch: Optional[str] = Field(None, description=
        'The branch to commit the changelog changes to. Defaults to the project’s default branch.'
        )
    config_file: Optional[str] = Field(None, description=
        'Path to the changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.'
        )
    date: Optional[datetime] = Field(None, description=
        'The date and time of the release. Defaults to the current time.')
    file: Optional[str] = Field(None, description=
        'The file to commit the changes to. Defaults to CHANGELOG.md.')
    from_: Optional[str] = Field(None, alias='from', description=
        'The SHA of the commit that marks the beginning of the range of commits to include in the changelog. This commit isn’t included in the changelog.'
        )
    message: Optional[str] = Field(None, description=
        'The commit message to use when committing the changes. Defaults to Add changelog for version X, where X is the value of the version argument.'
        )
    to: Optional[str] = Field(None, description=
        'The SHA of the commit that marks the end of the range of commits to include in the changelog. This commit is included in the changelog. Defaults to the branch specified in the branch attribute. Limited to 15000 commits unless the feature flag changelog_commits_limitation is disabled.'
        )
    trailer: Optional[str] = Field(None, description=
        'The Git trailer to use for including commits. Defaults to Changelog. Case-sensitive: Example does not match example or eXaMpLE.'
        )
class GenerateChangelogData(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    version: str = Field(description=
        'The version to generate the changelog for. The format must follow semantic versioning.'
        )
    config_file: Optional[str] = Field(description=
        'The path of changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.'
        )
    date: Optional[datetime] = Field(description=
        'The date and time of the release. Uses ISO 8601 format. Defaults to the current time.'
        )
    from_: Optional[str] = Field(alias='from', description=
        'The start of the range of commits (as a SHA) to use for generating the changelog. This commit itself isn’t included in the list.'
        )
    to: Optional[str] = Field(description=
        'The end of the range of commits (as a SHA) to use for the changelog. This commit is included in the list. Defaults to the HEAD of the default project branch.'
        )
    trailer: Optional[str] = Field(description=
        'The Git trailer to use for including commits. Defaults to Changelog.')

# Classes from file: deployments.py
class ListProjectDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class GetASpecificDeployment(BaseModel):
    id: int
    deployment_id: int
class GetDeploymentFrequency(BaseModel):
    id: int
    finished_after: Optional[datetime] = None
class DeploymentDuration(BaseModel):
    created_at: datetime
    finished_at: datetime
class ListProjectDeployment(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsCreate(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsDeploymentid(BaseModel):
    id: int
    deployment_id: int
class CreateADeployment(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeploymentsDeploymentidUpdate(BaseModel):
    id: int
    deployment_id: int
    status: str
class ProjectsIdDeploymentsDeploymentidDelete(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidMergerequests(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidApproval(BaseModel):
    id: int
    deployment_id: int
    status: str
    comment: Optional[str] = None
    represented_as: Optional[str] = None

# Classes from file: snippet_repository_storage_moves.py

# Classes from file: notification_settings.py

# Classes from file: iterations_(group).py

# Classes from file: search.py

# Classes from file: project_aliases.py

# Classes from file: http_wrapper_privatetoken.py

# Classes from file: group_badges.py
class GroupsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class GroupsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesAdd(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class GroupsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class GroupsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str

# Classes from file: external_status_checks.py
class ProjectsIdExternalstatuschecks(BaseModel):
    id: Union[int, str] = Field(description='ID of a project')
class CreateUpdateExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    name: Optional[str] = Field(description=
        'Display name of external status check service')
    external_url: Optional[str] = Field(description=
        'URL of external status check service')
    protected_branch_ids: Optional[List[int]] = Field(description=
        'IDs of protected branches to scope the rule by')
class UpdateExternalStatusCheckService(BaseModel):
    id: Union[int, str]
    check_id: int
    name: Optional[str] = None
    external_url: Optional[str] = None
    protected_branch_ids: Optional[List[int]] = None
class DeleteExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    check_id: int = Field(description='ID of an external status check service')
class MergeRequestStatusChecks(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
class SetStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    sha: str = Field(description='SHA at HEAD of the source branch')
    external_status_check_id: int = Field(description=
        'ID of an external status check')
    status: Optional[str] = Field(description=
        'Set to passed to pass the check or failed to fail it')
class RetryFailedStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    external_status_check_id: int = Field(description=
        'ID of a failed external status check')

# Classes from file: access_requests.py
class ProjectsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class ProjectsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class GroupsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int
class ProjectsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int

# Classes from file: project_templates.py

# Classes from file: sidekiq_metrics.py

# Classes from file: group_level_protected_environments.py

# Classes from file: invitations.py

# Classes from file: go_proxy.py

# Classes from file: license.py

# Classes from file: project_repository_storage_moves.py

# Classes from file: merge_trains.py

# Classes from file: vulnerabilities.py
class VulnerabilitiesId(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdConfirm(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdResolve(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdDismiss(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdRevert(BaseModel):
    id: Union[int, str]

# Classes from file: variables_group.py
class ListGroupVariables(BaseModel):
    id: Union[int, str]
class VariableType(str, Enum):
    env_var = 'env_var'
    file = 'file'
class ShowGroupVariableDetails(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
class CreateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class UpdateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class RemoveGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')

# Classes from file: pypi.py

# Classes from file: maven.py

# Classes from file: group_access_tokens.py

# Classes from file: projects.py
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
    custom_attributes: Optional[Dict[str, str]] = Field(None, description=
        'A dictionary of custom attributes to filter by')
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
class CreateProjectRequest(BaseModel):
    name: Optional[str] = Field(None, description=
        'The name of the new project. Equals path if not provided.')
    path: Optional[str] = Field(None, description=
        'Repository name for new project. Generated based on name if not provided (generated as lowercase with dashes). Starting with GitLab 14.9, path must not start or end with a special character and must not contain consecutive special characters.'
        )
    allow_merge_on_skipped_pipeline: Optional[bool] = Field(None,
        description=
        'Set whether or not merge requests can be merged with skipped jobs.')
    only_allow_merge_if_all_status_checks_passed: Optional[bool] = Field(None,
        description=
        'Indicates that merges of merge requests should be blocked unless all status checks have passed. Defaults to false. Introduced in GitLab 15.5 with feature flag only_allow_merge_if_all_status_checks_passed disabled by default.'
        )
    analytics_access_level: Optional[str] = Field(None, description=
        'One of disabled, private or enabled.')
    approvals_before_merge: Optional[int] = Field(None, description=
        'How many approvers should approve merge requests by default. To configure approval rules, see Merge request approvals API. Deprecated in GitLab 16.0.'
        )
    auto_cancel_pending_pipelines: Optional[str] = Field(None, description=
        'Auto-cancel pending pipelines. This action toggles between an enabled state and a disabled state; it is not a boolean.'
        )
    auto_devops_deploy_strategy: Optional[str] = Field(None, description=
        'Auto Deploy strategy (continuous, manual or timed_incremental).')
    auto_devops_enabled: Optional[bool] = Field(None, description=
        'Enable Auto DevOps for this project.')
    autoclose_referenced_issues: Optional[bool] = Field(None, description=
        'Set whether auto-closing referenced issues on default branch.')
    avatar: Optional[Union[str, Any]] = Field(None, description=
        'Image file for avatar of the project.')
    build_git_strategy: Optional[str] = Field(None, description=
        'The Git strategy. Defaults to fetch.')
    build_timeout: Optional[int] = Field(None, description=
        'The maximum amount of time, in seconds, that a job can run.')
    builds_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    ci_config_path: Optional[str] = Field(None, description=
        'The path to CI configuration file.')
    container_expiration_policy_attributes: Optional[dict] = Field(None,
        description='Update the image cleanup policy for this project.')
    container_registry_access_level: Optional[str] = Field(None,
        description=
        'Set visibility of container registry, for this project, to one of disabled, private or enabled.'
        )
    container_registry_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable container registry for this project. Use container_registry_access_level instead.'
        )
    default_branch: Optional[str] = Field(None, description=
        'The default branch name. Requires initialize_with_readme to be true.')
    description: Optional[str] = Field(None, description=
        'Short project description.')
    emails_disabled: Optional[bool] = Field(None, description=
        'Disable email notifications.')
    external_authorization_classification_label: Optional[str] = Field(None,
        description='The classification label for the project.')
    forking_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    group_with_project_templates_id: Optional[int] = Field(None,
        description=
        'For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true.'
        )
    import_url: Optional[str] = Field(None, description=
        'URL to import repository from. When the URL value isn’t empty, you must not set initialize_with_readme to true. Doing so might result in the following error: not a git repository.'
        )
    initialize_with_readme: Optional[bool] = Field(None, description=
        'Whether to create a Git repository with just a README.md file. Default is false.'
        )
    issues_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    issues_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable issues for this project. Use issues_access_level instead.'
        )
    jobs_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable jobs for this project. Use builds_access_level instead.'
        )
    lfs_enabled: Optional[bool] = Field(None, description='Enable LFS.')
    merge_method: Optional[str] = Field(None, description=
        'Set the merge method used.')
    merge_pipelines_enabled: Optional[bool] = Field(None, description=
        'Enable or disable merge pipelines.')
    merge_requests_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    merge_requests_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable merge requests for this project. Use merge_requests_access_level instead.'
        )
    merge_trains_enabled: Optional[bool] = Field(None, description=
        'Enable or disable merge trains.')
    mirror_trigger_builds: Optional[bool] = Field(None, description=
        'Pull mirroring triggers builds.')
    mirror: Optional[bool] = Field(None, description=
        'Enables pull mirroring in a project.')
    namespace_id: Optional[int] = Field(None, description=
        'Namespace for the new project (defaults to the current user’s namespace).'
        )
    only_allow_merge_if_all_discussions_are_resolved: Optional[bool] = Field(
        None, description=
        'Set whether merge requests can only be merged when all the discussions are resolved.'
        )
    only_allow_merge_if_pipeline_succeeds: Optional[bool] = Field(None,
        description=
        'Set whether merge requests can only be merged with successful pipelines.'
        )
    packages_enabled: Optional[bool] = Field(None, description=
        'Enable or disable packages repository feature.')
    pages_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, enabled, or public.')
    printing_merge_request_link_enabled: Optional[bool] = Field(None,
        description=
        'Show link to create/view merge request when pushing from the command line.'
        )
    public_builds: Optional[bool] = Field(None, description=
        'If true, jobs can be viewed by non-project members.')
    releases_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    environments_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    feature_flags_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    infrastructure_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    monitor_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    remove_source_branch_after_merge: Optional[bool] = Field(None,
        description=
        'Enable Delete source branch option by default for all new merge requests.'
        )
    repository_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    repository_storage: Optional[str] = Field(None, description=
        'Which storage shard the repository is on. (administrator only)')
    request_access_enabled: Optional[bool] = Field(None, description=
        'Allow users to request member access.')
    requirements_access_level: Optional[str] = Field(None, description=
        'One of disabled, private or enabled')
    resolve_outdated_diff_discussions: Optional[bool] = Field(None,
        description=
        'Automatically resolve merge request diffs discussions on lines changed with a push.'
        )
    security_and_compliance_access_level: Optional[str] = Field(None,
        description=
        '(GitLab 14.9 and later) Security and compliance access level. One of disabled, private, or enabled.'
        )
    shared_runners_enabled: Optional[bool] = Field(None, description=
        'Enable shared runners for this project.')
    group_runners_enabled: Optional[bool] = Field(None, description=
        'Enable group runners for this project.')
    snippets_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    snippets_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable snippets for this project. Use snippets_access_level instead.'
        )
    squash_option: Optional[str] = Field(None, description=
        'One of never, always, default_on, or default_off.')
    tag_list: Optional[list] = Field(None, description=
        '(Deprecated in GitLab 14.0) The list of tags for a project; put array of tags, that should be finally assigned to a project. Use topics instead.'
        )
    template_name: Optional[str] = Field(None, description=
        'When used without use_custom_template, name of a built-in project template.'
        )
    template_project_id: Optional[int] = Field(None, description=
        'When used with use_custom_template, project ID of a custom project template.'
        )
    topics: Optional[list] = Field(None, description=
        'The list of topics for a project; put array of topics, that should be finally assigned to a project. (Introduced in GitLab 14.0.)'
        )
    use_custom_template: Optional[bool] = Field(None, description=
        'Use either custom instance or group (with group_with_project_templates_id) project template.'
        )
    visibility: Optional[str] = Field(None, description=
        'See project visibility level.')
    wiki_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    wiki_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable wiki for this project. Use wiki_access_level instead.'
        )
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
    container_expiration_policy_attributes: Optional[
        ContainerExpirationPolicyAttributes] = None
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

# Classes from file: merge_requests.py
class ProjectsMergeRequestCreate(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    source_branch: str = Field(description='The source branch name.')
    target_branch: str = Field(description='The target branch name.')
    title: str = Field(description='The title of merge request.')
    allow_collaboration: Optional[bool] = Field(None, description=
        'Allow commits from members who can merge to the target branch.')
    approvals_before_merge: Optional[int] = Field(None, description=
        'The amount of approvals required before merging.')
    allow_maintainer_to_push: Optional[bool] = Field(None, description=
        'Allow users who can merge to the target branch to push to the source branch.'
        )
    assignee_id: Optional[int] = Field(None, description=
        'The ID of a user to assign merge request.')
    assignee_ids: Optional[List[int]] = Field(None, description=
        'The IDs of users to assign merge request.')
    description: Optional[str] = Field(None, description=
        'The description of merge request.')
    labels: Optional[str] = Field(None, description=
        'Comma-separated list of label names.')
    milestone_id: Optional[int] = Field(None, description=
        'The global ID of a milestone to assign merge request.')
    remove_source_branch: Optional[bool] = Field(None, description=
        'Flag indicating if a merge request should remove the source branch when merging.'
        )
    reviewer_ids: Optional[List[int]] = Field(None, description=
        'The IDs of users to request review from when merge request created.')
    squash: Optional[bool] = Field(None, description=
        'Squash commits into a single commit when merging.')
    squash_on_merge: Optional[bool] = Field(None, description=
        'Squash commits into a single commit after merging.')
    target_project_id: Optional[int] = Field(None, description=
        'The target project ID. If the user is a maintainer of the target project, the source project is set as the target_project_id.'
        )

# Classes from file: member_roles.py

# Classes from file: resource_weight_events.py

# Classes from file: search_migrations.py

# Classes from file: integrations.py

# Classes from file: emoji_reactions.py
class AwardEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
class SingleEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class NewEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    name: str
class DeleteEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class ListCommentEmojiReactionsParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
class GetCommentEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int
class AwardCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    name: str
class DeleteCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int

# Classes from file: settings_(application).py

# Classes from file: pipelines.py
class Scope(str, Enum):
    running = 'running'
    pending = 'pending'
    finished = 'finished'
    branches = 'branches'
    tags = 'tags'
class Status(str, Enum):
    created = 'created'
    waiting_for_resource = 'waiting_for_resource'
    preparing = 'preparing'
    pending = 'pending'
    running = 'running'
    success = 'success'
    failed = 'failed'
    canceled = 'canceled'
    skipped = 'skipped'
    manual = 'manual'
    scheduled = 'scheduled'
class Source(str, Enum):
    push = 'push'
    web = 'web'
    trigger = 'trigger'
    schedule = 'schedule'
    api = 'api'
    external = 'external'
    pipeline = 'pipeline'
    chat = 'chat'
    webide = 'webide'
    merge_request_event = 'merge_request_event'
    external_pull_request_event = 'external_pull_request_event'
    parent_pipeline = 'parent_pipeline'
    ondemand_dast_scan = 'ondemand_dast_scan'
    ondemand_dast_validation = 'ondemand_dast_validation'
class OrderBy(str, Enum):
    id = 'id'
    status = 'status'
    ref = 'ref'
    updated_at = 'updated_at'
    user_id = 'user_id'
class Sort(str, Enum):
    asc = 'asc'
    desc = 'desc'
class ListProjectPipelinesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    scope: Optional[Scope]
    status: Optional[Status]
    source: Optional[Source]
    ref: Optional[str]
    sha: Optional[str]
    yaml_errors: Optional[bool]
    username: Optional[str]
    updated_after: Optional[datetime]
    updated_before: Optional[datetime]
    name: Optional[str]
    order_by: Optional[OrderBy]
    sort: Optional[Sort]
class GetPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineVariablesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportSummaryInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetLatestPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    ref: Optional[str] = Field(None, description=
        'The branch or tag to check for the latest pipeline. Defaults to the default branch when not specified.'
        )
class CreatePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    ref: str = Field(..., description=
        'The branch or tag to run the pipeline on.')
    variables: Optional[List[Dict[str, Union[str, Dict[str, str]]]]] = Field(
        None, description=
        'An array of hashes containing the variables available in the pipeline.'
        )
class RetryJobsInPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class CancelPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class DeletePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')

# Classes from file: lint_.gitlab_ci.yml.py

# Classes from file: service_data.py

# Classes from file: dependencies.py
class ProjectsIdDependencies(BaseModel):
    id: Union[int, str]
    package_manager: Optional[str] = None

# Classes from file: project_badges.py
class ProjectsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class ProjectsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesCreate(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str

# Classes from file: helm.py

# Classes from file: namespaces.py

# Classes from file: links_(issue).py

# Classes from file: deploy_keys.py
class Deploykeys(BaseModel):
    public: Optional[bool] = None
class ProjectsIdDeploykeys(BaseModel):
    id: int
class UsersIdorusernameProjectdeploykeys(BaseModel):
    id_or_username: str
class ProjectsIdDeploykeysKeyidSingle(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysAdd(BaseModel):
    id: int
    key: str
    title: str
    can_push: Optional[bool] = None
    expires_at: Optional[datetime] = None
class ProjectsIdDeploykeysKeyidUpdate(BaseModel):
    id: int
    can_push: Optional[bool] = None
    title: Optional[str] = None
class ProjectsIdDeploykeysKeyidDelete(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysKeyidEnable(BaseModel):
    id: int
    key_id: int

# Classes from file: issue_boards_(project).py

# Classes from file: job_token_scopes.py
class GetProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
class PatchProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
    enabled: bool
class GetProjectCICDJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
class CreateNewProjectToJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int
class RemoveProjectFromJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int

# Classes from file: merge_request_context_commits.py

# Classes from file: system_hooks.py

# Classes from file: user_starred_metrics_dashboards.py
class ProjectsIdMetricsUserstarreddashboardsAdd(BaseModel):
    id: Union[int, str]
    dashboard_path: str
class ProjectsIdMetricsUserstarreddashboardsRemove(BaseModel):
    id: Union[int, str]
    dashboard_path: Optional[str] = None

# Classes from file: secure_files.py

# Classes from file: issues.py

# Classes from file: labels_(group).py

# Classes from file: tags.py

# Classes from file: release_links.py

# Classes from file: import.py

# Classes from file: pages_domains.py

# Classes from file: pipeline_triggers.py
class ListProjectTriggerTokensInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
class GetTriggerTokenDetailsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class CreateTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    description: str = Field(..., description='The trigger name.')
class UpdateProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
    description: Optional[str] = Field(None, description='The trigger name.')
class RemoveProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class TriggerPipelineWithTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    ref: str = Field(..., description=
        'The branch or tag to run the pipeline on.')
    token: str = Field(..., description='The trigger token or CI/CD job token.'
        )
    variables: Optional[Dict[str, str]] = Field(None, description=
        'A map of key-valued strings containing the pipeline variables.')

# Classes from file: linked_epics.py

# Classes from file: resource_state_events.py

# Classes from file: project_remote_mirrors.py

# Classes from file: to_do_lists.py

# Classes from file: deploy_tokens.py

# Classes from file: dashboard_annotations.py
class CreateNewAnnotation(BaseModel):
    id: Union[int, str]
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str] = None
    description: str

    @validator('starting_at', 'ending_at', pre=True)
    def parse_iso8601(cls, v):
        if v is None:
            return v
        try:
            return datetime.fromisoformat(v)
        except ValueError:
            raise ValueError('datetime is not in ISO 8601 format')

# Classes from file: geo_nodes.py

# Classes from file: merge_request_approvals.py

# Classes from file: conan.py
class RoutePrefix(str, Enum):
    instance_level = '/packages/conan/v1'
    project_level = '/projects/:id/packages/conan/v1`'
class Ping(BaseModel):
    route_prefix: RoutePrefix = Field(description=
        'pick either instance_level or project_level')
class SearchInput(BaseModel):
    route_prefix: RoutePrefix
    q: str = Field(..., description=
        'Search query. You can use * as a wildcard.')
class AuthenticateInput(BaseModel):
    route_prefix: RoutePrefix
class CheckCredentialsInput(BaseModel):
    route_prefix: RoutePrefix
class RecipeSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifest(BaseModel):
    package_name: str = Field(description='Name of a package.')
    package_version: str = Field(description='Version of a package.')
    package_username: str = Field(description=
        'Conan username of a package. This attribute is the +-separated full path of your project.'
        )
    package_channel: str = Field(description='Channel of a package.')
class PackageManifest(RecipeManifest):
    conan_package_reference: str = Field(description=
        'Reference hash of a Conan package. Conan generates this value.')
class UploadUrls(RecipeManifest):
    files: Dict[str, int] = Field(description=
        'Dictionary of file names with their sizes.')
class PackageUploadUrlsInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
    file_sizes: Dict[str, int]
class DownloadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
class UploadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
    file_content: str
class DownloadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
class UploadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
    file_content: str
class DeletePackageInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str

# Classes from file: custom_attributes.py
class UsersIdCustomattributes(BaseModel):
    id: int
class GroupsIdCustomattributes(BaseModel):
    id: int
class ProjectsIdCustomattributes(BaseModel):
    id: int
class UsersIdCustomattributesKey(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class UsersIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class GroupsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class ProjectsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class UsersIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str

# Classes from file: epics.py
class NotMatch(BaseModel):
    author_id: Optional[int] = Field(None, description=
        'Can exclude by author ID')
    author_username: Optional[str] = Field(None, description=
        'Can exclude by author username (GitLab 14.7 and later)')
    labels: Optional[str] = Field(None, description='Can exclude by labels')
class GroupsIdEpics(BaseModel):
    id: Union[int, str]
    author_id: Optional[int] = None
    author_username: Optional[str] = None
    labels: Optional[str] = None
    with_labels_details: Optional[bool] = None
    order_by: Optional[str] = None
    sort: Optional[str] = None
    search: Optional[str] = None
    state: Optional[str] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    include_ancestor_groups: Optional[bool] = None
    include_descendant_groups: Optional[bool] = None
    my_reaction_emoji: Optional[str] = None
    not_: Optional[NotMatch] = Field(None, alias='not', description=
        'Return epics that do not match the parameters supplied')
class SingleEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class NewEpicInput(BaseModel):
    id: Union[int, str]
    title: str
    labels: Optional[str]
    description: Optional[str]
    color: Optional[str]
    confidential: Optional[bool]
    created_at: Optional[datetime]
    start_date_is_fixed: Optional[bool]
    start_date_fixed: Optional[str]
    due_date_is_fixed: Optional[bool]
    due_date_fixed: Optional[str]
    parent_id: Optional[Union[int, str]]
class UpdateEpic(BaseModel):
    id: int
    epic_iid: int
    add_labels: Optional[str] = None
    confidential: Optional[bool] = None
    description: Optional[str] = None
    due_date_fixed: Optional[str] = None
    due_date_is_fixed: Optional[bool] = None
    labels: Optional[str] = None
    parent_id: Optional[int] = None
    remove_labels: Optional[str] = None
    start_date_fixed: Optional[str] = None
    start_date_is_fixed: Optional[bool] = None
    state_event: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
class DeleteEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class CreateAToDoItem(BaseModel):
    id: Union[int, str]
    epic_iid: int

# Classes from file: issues_(epic).py

# Classes from file: suggestions.py

# Classes from file: product_analytics.py

# Classes from file: discussions.py
class ListProjectIssueDiscussionItems(BaseModel):
    id: Union[int, str]
    issue_iid: int
class GetSingleIssueDiscussionItem(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
class CreateNewIssueThread(BaseModel):
    body: str
    id: Union[int, str]
    issue_iid: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingIssueThreadPayload(BaseModel):
    body: str = Field(..., description='The content of the note or reply.')
    discussion_id: int = Field(..., description='The ID of a thread.')
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    issue_iid: int = Field(..., description='The IID of an issue.')
    note_id: int = Field(..., description='The ID of a thread note.')
    created_at: Optional[datetime] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyExistingIssueThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    issue_iid: int
    note_id: int
class DeleteIssueThreadNote(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
    note_id: int
class ProjectsIdSnippetsSnippetidDiscussions(BaseModel):
    id: Union[int, str]
    snippet_id: int
class ListProjectSnippetDiscussionItems(BaseModel):
    id: Union[int, str]
    snippet_id: int
class GetSingleSnippetDiscussionItem(BaseModel):
    id: Union[int, str]
    snippet_id: int
    discussion_id: int
class CreateNewSnippetThread(BaseModel):
    body: str
    id: Union[int, str]
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingSnippetThread(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class ModifyExistingSnippetThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class DeleteSnippetThreadNote(BaseModel):
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class GroupsIdEpicsEpicidDiscussions(BaseModel):
    epic_id: int
    id: Union[int, str]
class SingleEpicDiscussionItem(BaseModel):
    discussion_id: int = Field(description='The ID of a discussion item.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
class CreateNewEpicThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    created_at: Optional[Union[str, datetime]] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class AddNoteToEpicThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[Union[str, datetime]] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyEpicThreadNote(BaseModel):
    body: str = Field(description='The content of note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class DeleteEpicThreadNote(BaseModel):
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class ListMergeRequestDiscussionItems(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class SingleMergeRequestDiscussionItem(BaseModel):
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class BasicMergeRequestParams(BaseModel):
    body: str = Field(description='The content of the thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class DiffNoteParams(BaseModel):
    base_sha: str = Field(description='Base commit SHA in the source branch.')
    head_sha: str = Field(description=
        'SHA referencing HEAD of this merge request.')
    start_sha: str = Field(description=
        'SHA referencing commit in target branch.')
    new_path: str = Field(description='File path after change.')
    old_path: str = Field(description='File path before change.')
    position_type: str = Field(description=
        'Type of the position reference. Allowed values: text or image.')
class TextDiffNoteParams(BaseModel):
    new_line: Optional[int] = Field(description=
        'For text diff notes, the line number after change.')
    old_line: Optional[int] = Field(description=
        'For text diff notes, the line number before change.')
class ImageDiffNoteParams(BaseModel):
    width: Optional[int] = Field(description=
        'For image diff notes, width of the image.')
    height: Optional[int] = Field(description=
        'For image diff notes, height of the image.')
    x: Optional[float] = Field(description=
        'For image diff notes, X coordinate.')
    y: Optional[float] = Field(description=
        'For image diff notes, Y coordinate.')
class MultilineCommentsParams(BaseModel):
    line_range: dict = Field(description=
        'Line range for a multi-line diff note.')
class CreateNewMergeRequestThread(BasicMergeRequestParams):
    position: DiffNoteParams = Field(description=
        'Position when creating a diff note.')
    text_position: Optional[TextDiffNoteParams] = Field(description=
        'Position parameters for text diff notes.')
    image_position: Optional[ImageDiffNoteParams] = Field(description=
        'Position parameters for image diff notes.')
    multiline_comments: Optional[MultilineCommentsParams] = Field(description
        ='Parameters for multiline comments.')
    commit_id: Optional[str] = Field(description=
        'SHA referencing commit to start this thread on.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class ResolveMergeRequestThread(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    discussion_id: str = Field(description='The ID of a thread.')
    resolved: bool = Field(description='Resolve or unresolve the discussion.')
class AddNoteToMergeRequestThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    discussion_id: str = Field(description='The ID of a thread.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class ModifyMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description=
        'The content of the note or reply. Exactly one of body or resolved must be set.'
        )
    resolved: Optional[bool] = Field(description=
        'Resolve or unresolve the note. Exactly one of body or resolved must be set.'
        )
class DeleteMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
class ListProjectCommitDiscussionItems(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
class GetSingleCommitDiscussionItem(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
class Position(BaseModel):
    base_sha: str = Field(description='SHA of the parent commit.')
    head_sha: str = Field(description=
        'The SHA of this commit. Same as commit_id.')
    start_sha: str = Field(description='SHA of the parent commit.')
    position_type: str = Field(description=
        'Type of the position reference. Allowed values: text or image.')
    hash: Optional[str] = Field(description=
        'Position when creating a diff note.')
    new_path: Optional[str] = Field(description='File path after change.')
    new_line: Optional[int] = Field(description='Line number after change.')
    old_path: Optional[str] = Field(description='File path before change.')
    old_line: Optional[int] = Field(description='Line number before change.')
    height: Optional[int] = Field(description=
        'For image diff notes, image height.')
    width: Optional[int] = Field(description=
        'For image diff notes, image width.')
    x: Optional[int] = Field(description='For image diff notes, X coordinate.')
    y: Optional[int] = Field(description='For image diff notes, Y coordinate.')
class CreateNewCommitThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    position: Position = Field(description=
        'Position when creating a diff note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class AddNoteToCommitThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyCommitThreadNote(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description='The content of a note.')
class DeleteCommitThreadNote(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    note_id: int = Field(description='The ID of a thread note.')

# Classes from file: project_relations_export.py

# Classes from file: snippets_(project).py

# Classes from file: branches.py
class ProjectsIdRepositoryBranches(BaseModel):
    id: int
    search: Optional[str] = None
    regex: Optional[str] = None
class ProjectsIdRepositoryBranchesBranchSingle(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryBranchesCreate(BaseModel):
    id: int
    branch: str
    ref: str
class ProjectsIdRepositoryBranchesBranch(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryMergedbranches(BaseModel):
    id: int

# Classes from file: metadata.py

# Classes from file: version.py

# Classes from file: protected_tags.py

# Classes from file: issue_boards_(group).py

# Classes from file: repository_submodules.py

# Classes from file: milestones_(group).py

# Classes from file: members.py

# Classes from file: protected_branches.py

# Classes from file: commits.py
class ProjectsIdRepositoryCommits(BaseModel):
    id: int
    ref_name: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None
    path: Optional[str] = None
    author: Optional[str] = None
    all: Optional[bool]
    with_stats: Optional[bool]
    first_parent: Optional[bool]
    order: Optional[str]
    trailers: Optional[bool]
class ProjectsIdRepositoryCommitsSha(BaseModel):
    id: int
    sha: str
    stats: Optional[bool] = None
class ProjectsIdRepositoryCommitsShaRefs(BaseModel):
    id: int
    sha: str
    type: Optional[str] = None
class ProjectsIdRepositoryCommitsShaCherrypick(BaseModel):
    id: int
    sha: str
    branch: str
    dry_run: Optional[bool] = None
    message: Optional[str] = None
class ProjectsIdRepositoryCommitsShaRevert(BaseModel):
    id: int
    sha: str
    branch: str
    dry_run: Optional[bool] = None
class ProjectsIdRepositoryCommitsShaDiff(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaComments(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaCommentsPost(BaseModel):
    id: int
    sha: str
    note: str
    path: Optional[str] = None
    line: Optional[int] = None
    line_type: Optional[str] = None
class ProjectsIdRepositoryCommitsShaDiscussions(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaStatuses(BaseModel):
    id: int
    sha: str
    ref: Optional[str] = None
    stage: Optional[str] = None
    name: Optional[str] = None
    all: Optional[bool] = None
class ProjectsIdStatusesSha(BaseModel):
    id: int
    sha: str
    state: str
    ref: Optional[str] = None
    context: Optional[str] = None
    name: Optional[str] = None
    target_url: Optional[str] = None
    description: Optional[str] = None
    coverage: Optional[float] = None
    pipeline_id: Optional[int] = None
class ProjectsIdRepositoryCommitsShaMergerequests(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaSignature(BaseModel):
    id: int
    sha: str

# Classes from file: application_appearance.py
class ApplicationAppearance(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    pwa_name: Optional[str] = None
    pwa_short_name: Optional[str] = None
    pwa_description: Optional[str] = None
    pwa_icon: Optional[Any] = None
    logo: Optional[Any] = None
    header_logo: Optional[Any] = None
    favicon: Optional[Any] = None
    new_project_guidelines: Optional[str] = None
    profile_image_guidelines: Optional[str] = None
    header_message: Optional[str] = None
    footer_message: Optional[str] = None
    message_background_color: Optional[str] = None
    message_font_color: Optional[str] = None
    email_header_and_footer_enabled: Optional[bool] = None
class ChangeLogo(BaseModel):
    logo: Any
    pwa_icon: Any

# Classes from file: users.py

# Classes from file: project_vulnerabilities.py

# Classes from file: draft_notes.py
class ProjectsIdMergerequestsMergerequestiidDraftnotes(BaseModel):
    id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidSingle(
    BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesCreate(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    note: str
    commit_id: Optional[str] = None
    in_reply_to_discussion_id: Optional[int] = None
    resolve_discussion: Optional[bool] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidModify(
    BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
    note: Optional[str] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidDelete(
    BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidPublish(
    BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesBulkpublish(BaseModel):
    id: Union[int, str]
    merge_request_iid: int

# Classes from file: group_migration_by_direct_transfer.py

# Classes from file: resource_iteration_events.py

# Classes from file: agents_for_kubernetes.py
class ListTheAgentsForAProject(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
class GetDetailsAboutAnAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class RegisterAnAgentWithAProject(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    name: str = Field(description='Name for the agent')
class DeleteARegisteredAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class ListTokensForAnAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class GetSingleAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')
class CreateAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    name: int = Field(description='Name for the token')
    description: Optional[int] = Field(None, description=
        'Description for the token')
class RevokeAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')

# Classes from file: project_import_export.py

# Classes from file: project_level_protected_environments.py

# Classes from file: composer.py
class GroupIdPackagesComposerPackages(BaseModel):
    id: Union[int, str]
class GroupIdPackagesComposerPSha(BaseModel):
    id: Union[int, str]
    sha: str
class V1PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str
class V2PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
class CreateAPackageInput(BaseModel):
    id: Union[int, str]
    tag: Optional[str] = None
    branch: Optional[str] = None
class ProjectsIdPackagesComposerArchivesPackagename(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str

# Classes from file: alert_management.py
class ListMetricImages(BaseModel):
    id: int
    alert_iid: int
class UpdateMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int
    url: Optional[str] = None
    url_text: Optional[str] = None
class DeleteMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int

# Classes from file: sidekiq_queues.py

# Classes from file: vulnerability_export.py
class SecurityProjectsIdVulnerabilityexports(BaseModel):
    id: Union[int, str]
class SecurityGroupsIdVulnerabilityexports(BaseModel):
    id: Union[int, str]
class SecurityVulnerabilityexportsId(BaseModel):
    id: Union[int, str]
class SecurityVulnerabilityexportsIdDownload(BaseModel):
    id: Union[int, str]

# Classes from file: events.py
class Events(BaseModel):
    action: Optional[str] = None
    target_type: Optional[str] = None
    before: Optional[datetime] = Field(None, description=
        'Include only events created before a certain date.')
    after: Optional[datetime] = Field(None, description=
        'Include only events created after a particular date.')
    target_id: Optional[int] = None
    author_id: Optional[int] = None
    search: Optional[str] = None
class AuthenticatedUserEvents(Events):
    scope: Optional[str] = None
    sort: Optional[str] = None
class UserContributionEvents(Events):
    id: int
    sort: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
class ProjectVisibleEvents(Events):
    project_id: int
    sort: Optional[str] = None

# Classes from file: group_import_export.py

# Classes from file: dora4_metrics.py
class ProjectsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None
class GroupsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None

# Classes from file: plan_limits.py

# Classes from file: statistics_(application).py

# Classes from file: group_repository_storage_moves.py

# Classes from file: iterations_(project).py

# Classes from file: applications.py
class Applications(BaseModel):
    name: str
    redirect_uri: str
    scopes: str
    confidential: Optional[bool] = None
class ApplicationsId(BaseModel):
    id: int

# Classes from file: saml.py

# Classes from file: dependency_proxy.py
class GroupsIdDependencyproxyCache(BaseModel):
    id: int

# Classes from file: group_relations_export.py

# Classes from file: metrics_dashboard_annotations.py
class EnvironmentsIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str
class ClustersIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str

# Classes from file: personal_access_tokens.py

# Classes from file: __init__.py

# Classes from file: instance_level_ci_cd_variables.py

# Classes from file: geo_sites.py

# Classes from file: visual_review_discussions_deprecated.py
class PositionData(BaseModel):
    base_sha: str
    start_sha: str
    head_sha: str
    position_type: str
    new_path: Optional[str] = None
    new_line: Optional[int] = None
    old_path: Optional[str] = None
    old_line: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None
class CreateNewMergeRequestThread(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    body: str
    position: Optional[PositionData] = None

# Classes from file: feature_flags.py
class StrategyParameters(BaseModel):
    pass
class StrategyScope(BaseModel):
    environment_scope: Optional[str] = None
class Strategy(BaseModel):
    name: Optional[str] = None
    parameters: Optional[StrategyParameters] = None
    scopes: Optional[List[StrategyScope]] = None
class ListFeatureFlagsForProject(BaseModel):
    id: Union[int, str]
    scope: Optional[str] = None
class GetSingleFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
class CreateFeatureFlag(BaseModel):
    id: Union[int, str]
    name: str
    version: str
    description: Optional[str] = None
    active: Optional[bool] = None
    strategies: Optional[List[Strategy]] = None
class UpdateFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
    description: Optional[str] = None
    active: Optional[bool] = None
    name: Optional[str] = None
    strategies: Optional[List[Strategy]] = None
class DeleteFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str

# Classes from file: pipelines_schedules.py
class GetAllPipelineSchedulesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    scope: Optional[str] = Field(None, description=
        'The scope of pipeline schedules, must be one of: active, inactive.')
class GetSinglePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class GetPipelinesTriggeredByScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class CreateNewPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    description: str = Field(..., description=
        'The description of the pipeline schedule.')
    ref: str = Field(..., description=
        'The branch or tag name that is triggered.')
    cron: str = Field(..., description=
        'The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description=
        'The time zone supported by ActiveSupport::TimeZone, for example: Pacific Time (US & Canada) (default: UTC).'
        )
    active: Optional[bool] = Field(None, description=
        'The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated (default: true).'
        )
class EditPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    description: Optional[str] = Field(None, description=
        'The description of the pipeline schedule.')
    ref: Optional[str] = Field(None, description=
        'The branch or tag name that is triggered.')
    cron: Optional[str] = Field(None, description=
        'The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description=
        'The time zone supported by ActiveSupport::TimeZone (for example Pacific Time (US & Canada)), or TZInfo::Timezone (for example America/Los_Angeles).'
        )
    active: Optional[bool] = Field(None, description=
        'The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated.'
        )
class TakeOwnershipOfPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class DeletePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class RunScheduledPipelineImmediatelyInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class CreatePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description=
        'The key of a variable; must have no more than 255 characters; only A-Z, a-z, 0-9, and _ are allowed.'
        )
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description=
        'The type of a variable. Available types are: env_var (default) and file.'
        )
class EditPipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description=
        'The type of a variable. Available types are: env_var (default) and file.'
        )
class DeletePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')

# Classes from file: dockerfile_templates.py
class TemplatesDockerfilesKey(BaseModel):
    key: str

# Classes from file: group_releases.py

# Classes from file: keys.py

# Classes from file: packages.py

# Classes from file: labels_(project).py

# Classes from file: freeze_periods.py

# Classes from file: broadcast_messages.py
class GetASpecificBroadcastMessage(BaseModel):
    id: int
class CreateABroadcastMessage(BaseModel):
    message: str
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class UpdateABroadcastMessage(BaseModel):
    id: int
    message: Optional[str]
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class DeleteABroadcastMessage(BaseModel):
    id: int

# Classes from file: groups.py

# Classes from file: wikis_project.py
class ProjectsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class ProjectsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class ProjectsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class ProjectsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class ProjectsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None

# Classes from file: npm.py

# Classes from file: avatar.py
class Avatar(BaseModel):
    email: str
    size: Optional[int] = None

# Classes from file: resource_group.py

# Classes from file: error_tracking.py
class GetErrorTrackingSettings(BaseModel):
    id: Union[int, str]
class CreateErrorTrackingSettings(BaseModel):
    id: int
    active: bool
    integrated: bool
class EnableOrDisableTheErrorTrackingProjectSettings(BaseModel):
    id: int
    active: bool
    integrated: Optional[bool] = None
class ListProjectClientKeys(BaseModel):
    id: Union[int, str]
class CreateAClientKey(BaseModel):
    id: Union[int, str]
class DeleteAClientKey(BaseModel):
    id: Union[int, str]
    key_id: int

# Classes from file: debian_project_distributions.py
class ListAllDebianDistributionsInAProject(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class SingleDebianProjectDistributionKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int

# Classes from file: resource_label_events.py

# Classes from file: repository_files.py
class ProjectIdRepositoryFiles(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    file_path: str = Field(description='URL encoded full path to new file')
    ref: str = Field(description='The name of branch, tag or commit')
class ProjectIdRepositoryFilesBlame(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    file_path: str = Field(description=
        'URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(description='The name of branch, tag or commit.')
    range_start: int = Field(description=
        'The first line of the range to blame.')
    range_end: int = Field(description='The last line of the range to blame.')
    range: Optional[dict] = Field(description='Blame range.')
class ProjectsIdRepositoryFilesFilepathRaw(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    file_path: str = Field(..., description=
        'URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(..., description=
        'The name of branch, tag or commit. Default is the HEAD of the project.'
        )
    lfs: Optional[bool] = Field(None, description=
        'Determines if the response should be Git LFS file contents, rather than the pointer. If the file is not tracked by Git LFS, ignored. Defaults to false.'
        )
class ProjectsIdRepositoryFilesFilepathCreate(BaseModel):
    branch: str = Field(description=
        'Name of the new branch to create. The commit is added to this branch.'
        )
    commit_message: str = Field(description='The commit message.')
    content: str = Field(description='The file’s content.')
    file_path: str = Field(description=
        'URL-encoded full path to new file. For example: lib%2Fclass%2Erb.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    author_email: Optional[str] = Field(None, description=
        'The commit author’s email address.')
    author_name: Optional[str] = Field(None, description=
        'The commit author’s name.')
    encoding: Optional[str] = Field(None, description=
        'Change encoding to base64. Default is text.')
    execute_filemode: Optional[bool] = Field(None, description=
        'Enables or disables the execute flag on the file. Can be true or false.'
        )
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathUpdate(BaseModel):
    branch: str
    commit_message: str
    content: str
    file_path: str
    id: Union[int, str]
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    encoding: Optional[str] = None
    execute_filemode: Optional[bool] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathDelete(BaseModel):
    branch: str
    commit_message: str
    file_path: str
    id: int
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositorySubmodulesSubmodule(BaseModel):
    id: int
    submodule: str
    branch: str
    commit_sha: str
    commit_message: Optional[str] = None

# Classes from file: nuget.py

# Classes from file: container_registry.py
class ContainerRegistryAccessLevelEnum(str, Enum):
    enabled = 'enabled'
    private = 'private'
    disabled = 'disabled'
class ChangeContainerRegistryVisibility(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project accessible by the authenticated user.'
        )
    container_registry_access_level: Optional[ContainerRegistryAccessLevelEnum
        ] = Field(default=None, description=
        'The desired visibility of the Container Registry. One of enabled (default), private, or disabled.'
        )
class ListProjectRegistryRepositories(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
class GroupsIdRegistryRepositories(BaseModel):
    id: Union[int, str]
class RegistryRepositoriesId(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
    size: Optional[bool] = None
class ProjectsIdRegistryRepositoriesRepositoryid(BaseModel):
    id: Union[int, str]
    repository_id: int
class ProjectsIdRegistryRepositoriesRepositoryidTags(BaseModel):
    id: Union[int, str]
    repository_id: int
class GetDetailsOfARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteRegistryRepositoryTagsInBulk(BaseModel):
    id: Union[int, str]
    repository_id: int
    name_regex: Optional[str] = None
    name_regex_delete: str
    name_regex_keep: Optional[str] = None
    keep_n: Optional[int] = None
    older_than: Optional[str] = None
class ObtainTokenInput(BaseModel):
    CI_SERVER_URL: str = Field(description='CI server URL.')
    service: str = Field(default='container_registry', description=
        'The service type.')
    scope: str = Field(description='Scope for the token.')
class DeleteImageTagsByReferenceInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    CI_REGISTRY_IMAGE: str = Field(description='The registry image.')
    CI_COMMIT_SHORT_SHA: str = Field(description='The commit SHA.')
class ListAllContainerRepositoriesInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    admin_username: str = Field(description='The admin username.')
    admin_password: str = Field(description='The admin password.')
    service: str = Field(default='container_registry', description=
        'The service type.')
    scope: str = Field(default='registry:catalog:*', description=
        'Scope for the token.')

# Classes from file: resource_milestone_events.py

# Classes from file: templates.py
class TemplatesGitignoresKey(BaseModel):
    key: str
class TemplatesGitlabciymlsKey(BaseModel):
    key: str

# Classes from file: jobs.py
class JobScope(str, Enum):
    created = 'created'
    pending = 'pending'
    running = 'running'
    failed = 'failed'
    success = 'success'
    canceled = 'canceled'
    skipped = 'skipped'
    waiting_for_resource = 'waiting_for_resource'
    manual = 'manual'
class ListProjectJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
class ListPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
    include_retried: Optional[bool] = Field(False, description=
        'Include retried jobs in the response.')
class ListPipelineTriggerJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
class GetAllowedAgentsInput(BaseModel):
    CI_JOB_TOKEN: str = Field(..., description=
        'Token value associated with the GitLab-provided CI_JOB_TOKEN variable.'
        )
class GetSingleJobInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='ID of a job.')
class JobInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='The ID of a job.')
class JobVariable(BaseModel):
    key: str = Field(..., description='The key of the job variable.')
    value: str = Field(..., description='The value of the job variable.')
class RunJobInput(JobInput):
    job_variables_attributes: Optional[List[JobVariable]] = Field(None,
        description=
        'An array containing the custom variables available to the job.')

# Classes from file: gitignore.py
class ListAllGitignoreTemplates(BaseModel):
    pass
class GetSingleGitignoreTemplate(BaseModel):
    key: str

# Classes from file: releases.py

# Classes from file: gitlab_ci_yaml.py
class ListAllCICDYamlTemplates(BaseModel):
    pass
class GetSingleCICDYamlTemplate(BaseModel):
    key: str

# Classes from file: milestones_(project).py

# Classes from file: group_activity_analytics.py

# Classes from file: job_artifacts.py
class GetJobArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int
    job_token: Optional[str] = None
class DownloadArtifacts(BaseModel):
    id: Union[int, str]
    ref_name: str
    job: str
    job_token: Optional[str] = None
class DownloadSingleArtifactByJobID(BaseModel):
    id: Union[int, str]
    job_id: int
    artifact_path: str
    job_token: Optional[str] = None
class DownloadSingleArtifactFromSpecificTag(BaseModel):
    id: Union[int, str]
    ref_name: str
    artifact_path: str
    job: str
    job_token: Optional[str] = None
class KeepArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int

# Classes from file: issues_statistics.py

# Classes from file: project_statistics.py

# Classes from file: experiments.py
class ListAllExperiments(BaseModel):
    pass

# Classes from file: scim.py

# Classes from file: feature_flag_user_lists.py

# Classes from file: vulnerability_findings.py
class ProjectsIdVulnerabilityfindings(BaseModel):
    id: int
    report_type: Optional[List[str]] = None
    scope: Optional[str] = None
    severity: Optional[List[str]] = None
    confidence: Optional[List[str]] = None
    pipeline_id: int

# Classes from file: licenses_(templates).py

# Classes from file: topics.py

# Classes from file: secrets.py

# Classes from file: debian.py
class ProjectsIdPackagesDebianFilename(BaseModel):
    id: str
    file_name: str
    distribution: Optional[str] = None
    component: Optional[str] = None
class ProjectsIdPackagesDebianPoolDistributionLetterPackagenamePackageversionFilename(
    BaseModel):
    distribution: str
    letter: str
    package_name: str
    package_version: str
    file_name: str
class DownloadADistributionReleaseFile(BaseModel):
    distribution: str
class DownloadASignedDistributionReleaseFile(BaseModel):
    distribution: str
class DownloadAReleaseFileSignature(BaseModel):
    distribution: str
class DownloadAPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadAPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadADebianInstallerPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DowloadADebianInstallerPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadASourcePackagesIndex(BaseModel):
    distribution: str
    component: str
class DownloadASourcePackagesIndexByHash(BaseModel):
    distribution: str
    component: str

# Classes from file: ruby_gems.py

# Classes from file: markdown.py

# Classes from file: debian_group_distributions.py
class ListAllDebianDistributionsInAGroup(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class GroupsIdDebiandistributionsCodenameKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int

# Classes from file: variables_project.py
class Variable(BaseModel):
    key: str
    value: str
    variable_type: Optional[str] = 'env_var'
    protected: Optional[bool] = False
    masked: Optional[bool] = False
    raw: Optional[bool] = False
    environment_scope: Optional[str] = '*'
    description: Optional[str] = None
class VariableFilter(BaseModel):
    environment_scope: Optional[str] = None
class GetProjectVariables(BaseModel):
    id: Union[int, str]
class GetVariable(BaseModel):
    id: Union[int, str]
    key: str
    filter: Optional[VariableFilter] = None
class CreateVariable(GetProjectVariables, Variable):
    pass
class UpdateVariable(GetVariable, Variable):
    pass
class DeleteVariable(GetVariable):
    pass

# Classes from file: links_(epic).py

# Classes from file: wikis_group.py
class GroupsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class GroupsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class GroupsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class GroupsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class GroupsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None

# Classes from file: audit_events.py
class Auditevents(BaseModel):
    created_after: Optional[str] = None
    created_before: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[int] = None
class AuditeventsId(BaseModel):
    id: int
class GroupsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class GroupsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int
class ProjectsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class ProjectsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int

# Classes from file: project_access_tokens.py

# Classes from file: runners.py

# Classes from file: environments.py
class ProjectsIdEnvironments(BaseModel):
    id: int
    name: Optional[str] = None
    search: Optional[str] = None
    states: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentid(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsCreate(BaseModel):
    id: int
    name: str
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentsid(BaseModel):
    id: int
    environment_id: int
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentidDelete(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsReviewapps(BaseModel):
    id: int
    before: Optional[datetime] = None
    limit: Optional[int] = None
    dry_run: Optional[bool] = None
class ProjectsIdEnvironmentsEnvironmentidStop(BaseModel):
    id: int
    environment_id: int
    force: Optional[bool] = None
class ProjectsIdEnvironmentsStopstale(BaseModel):
    id: int
    before: datetime

# Classes from file: group_level_protected_branches.py

# Classes from file: http_wrapper.py

# Classes from file: gitlab_pages.py

# Classes from file: marketplace.py

# Classes from file: snippets.py

# Classes from file: notes_(comments).py

# Classes from file: terraform_registry.py

# Classes from file: repositories.py
class ProjectsIdRepositoryTree(BaseModel):
    id: int
    page_token: Optional[str] = None
    pagination: Optional[str] = None
    path: Optional[str] = None
    per_page: Optional[str] = None
    recursive: bool = Field(False)
    ref: Optional[str] = None
class ProjectsIdRepositoryBlobsSha(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryBlobsShaRaw(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryArchive(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    path: Optional[str] = Field(None, description=
        'The subpath of the repository to download. Defaults to the whole repository.'
        )
    sha: Optional[str] = Field(None, description=
        'The commit SHA to download. A tag, branch reference, or SHA can be used. Defaults to the tip of the default branch.'
        )
    format: Optional[str] = Field(None, description=
        "The archive format. Options are: 'bz2', 'tar', 'tar.bz2', 'tar.gz', 'tb2', 'tbz', 'tbz2', 'zip'. Defaults to 'tar.gz'."
        )
class ProjectsIdRepositoryCompare(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    from_commit_or_branch: str = Field(..., alias='from', description=
        'The commit SHA or branch name.')
    to: str = Field(..., description='The commit SHA or branch name.')
    from_project_id: Optional[int] = Field(None, description=
        'The ID to compare from.')
    straight: Optional[bool] = Field(False, description=
        'Comparison method: true for direct comparison between from and to (from..to), false to compare using merge base (from…to)’. Default is false.'
        )
class ProjectsIdRepositoryContributors(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    order_by: Optional[str] = Field(None, description=
        'Return contributors ordered by name, email, or commits (orders by commit date) fields. Default is commits.'
        )
    sort: Optional[str] = Field(None, description=
        'Return contributors sorted in asc or desc order. Default is asc.')
class ProjectsIdRepositoryMergebase(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    refs: List[str] = Field(description=
        'The refs to find the common ancestor of. Accepts multiple refs.')
class ProjectsIdRepositoryChangelog(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    version: str = Field(description=
        'The version to generate the changelog for. The format must follow semantic versioning.'
        )
    branch: Optional[str] = Field(None, description=
        'The branch to commit the changelog changes to. Defaults to the project’s default branch.'
        )
    config_file: Optional[str] = Field(None, description=
        'Path to the changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.'
        )
    date: Optional[datetime] = Field(None, description=
        'The date and time of the release. Defaults to the current time.')
    file: Optional[str] = Field(None, description=
        'The file to commit the changes to. Defaults to CHANGELOG.md.')
    from_: Optional[str] = Field(None, alias='from', description=
        'The SHA of the commit that marks the beginning of the range of commits to include in the changelog. This commit isn’t included in the changelog.'
        )
    message: Optional[str] = Field(None, description=
        'The commit message to use when committing the changes. Defaults to Add changelog for version X, where X is the value of the version argument.'
        )
    to: Optional[str] = Field(None, description=
        'The SHA of the commit that marks the end of the range of commits to include in the changelog. This commit is included in the changelog. Defaults to the branch specified in the branch attribute. Limited to 15000 commits unless the feature flag changelog_commits_limitation is disabled.'
        )
    trailer: Optional[str] = Field(None, description=
        'The Git trailer to use for including commits. Defaults to Changelog. Case-sensitive: Example does not match example or eXaMpLE.'
        )
class GenerateChangelogData(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    version: str = Field(description=
        'The version to generate the changelog for. The format must follow semantic versioning.'
        )
    config_file: Optional[str] = Field(description=
        'The path of changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.'
        )
    date: Optional[datetime] = Field(description=
        'The date and time of the release. Uses ISO 8601 format. Defaults to the current time.'
        )
    from_: Optional[str] = Field(alias='from', description=
        'The start of the range of commits (as a SHA) to use for generating the changelog. This commit itself isn’t included in the list.'
        )
    to: Optional[str] = Field(description=
        'The end of the range of commits (as a SHA) to use for the changelog. This commit is included in the list. Defaults to the HEAD of the default project branch.'
        )
    trailer: Optional[str] = Field(description=
        'The Git trailer to use for including commits. Defaults to Changelog.')

# Classes from file: deployments.py
class ListProjectDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class GetASpecificDeployment(BaseModel):
    id: int
    deployment_id: int
class GetDeploymentFrequency(BaseModel):
    id: int
    finished_after: Optional[datetime] = None
class DeploymentDuration(BaseModel):
    created_at: datetime
    finished_at: datetime
class ListProjectDeployment(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsCreate(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsDeploymentid(BaseModel):
    id: int
    deployment_id: int
class CreateADeployment(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeploymentsDeploymentidUpdate(BaseModel):
    id: int
    deployment_id: int
    status: str
class ProjectsIdDeploymentsDeploymentidDelete(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidMergerequests(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidApproval(BaseModel):
    id: int
    deployment_id: int
    status: str
    comment: Optional[str] = None
    represented_as: Optional[str] = None

# Classes from file: snippet_repository_storage_moves.py

# Classes from file: notification_settings.py

# Classes from file: iterations_(group).py

# Classes from file: search.py

# Classes from file: project_aliases.py

# Classes from file: http_wrapper_privatetoken.py

# Classes from file: group_badges.py
class GroupsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class GroupsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesAdd(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class GroupsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class GroupsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str

# Classes from file: external_status_checks.py
class ProjectsIdExternalstatuschecks(BaseModel):
    id: Union[int, str] = Field(description='ID of a project')
class CreateUpdateExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    name: Optional[str] = Field(description=
        'Display name of external status check service')
    external_url: Optional[str] = Field(description=
        'URL of external status check service')
    protected_branch_ids: Optional[List[int]] = Field(description=
        'IDs of protected branches to scope the rule by')
class UpdateExternalStatusCheckService(BaseModel):
    id: Union[int, str]
    check_id: int
    name: Optional[str] = None
    external_url: Optional[str] = None
    protected_branch_ids: Optional[List[int]] = None
class DeleteExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    check_id: int = Field(description='ID of an external status check service')
class MergeRequestStatusChecks(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
class SetStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    sha: str = Field(description='SHA at HEAD of the source branch')
    external_status_check_id: int = Field(description=
        'ID of an external status check')
    status: Optional[str] = Field(description=
        'Set to passed to pass the check or failed to fail it')
class RetryFailedStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    external_status_check_id: int = Field(description=
        'ID of a failed external status check')

# Classes from file: access_requests.py
class ProjectsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class ProjectsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class GroupsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int
class ProjectsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int

# Classes from file: project_templates.py

# Classes from file: sidekiq_metrics.py

# Classes from file: group_level_protected_environments.py

# Classes from file: invitations.py

# Classes from file: go_proxy.py

# Classes from file: license.py

# Classes from file: project_repository_storage_moves.py

# Classes from file: merge_trains.py

# Classes from file: vulnerabilities.py
class VulnerabilitiesId(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdConfirm(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdResolve(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdDismiss(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdRevert(BaseModel):
    id: Union[int, str]

# Classes from file: variables_group.py
class ListGroupVariables(BaseModel):
    id: Union[int, str]
class VariableType(str, Enum):
    env_var = 'env_var'
    file = 'file'
class ShowGroupVariableDetails(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
class CreateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class UpdateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class RemoveGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')

# Classes from file: pypi.py

# Classes from file: maven.py

# Classes from file: group_access_tokens.py

# Classes from file: projects.py
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
    custom_attributes: Optional[Dict[str, str]] = Field(None, description=
        'A dictionary of custom attributes to filter by')
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
class CreateProjectRequest(BaseModel):
    name: Optional[str] = Field(None, description=
        'The name of the new project. Equals path if not provided.')
    path: Optional[str] = Field(None, description=
        'Repository name for new project. Generated based on name if not provided (generated as lowercase with dashes). Starting with GitLab 14.9, path must not start or end with a special character and must not contain consecutive special characters.'
        )
    allow_merge_on_skipped_pipeline: Optional[bool] = Field(None,
        description=
        'Set whether or not merge requests can be merged with skipped jobs.')
    only_allow_merge_if_all_status_checks_passed: Optional[bool] = Field(None,
        description=
        'Indicates that merges of merge requests should be blocked unless all status checks have passed. Defaults to false. Introduced in GitLab 15.5 with feature flag only_allow_merge_if_all_status_checks_passed disabled by default.'
        )
    analytics_access_level: Optional[str] = Field(None, description=
        'One of disabled, private or enabled.')
    approvals_before_merge: Optional[int] = Field(None, description=
        'How many approvers should approve merge requests by default. To configure approval rules, see Merge request approvals API. Deprecated in GitLab 16.0.'
        )
    auto_cancel_pending_pipelines: Optional[str] = Field(None, description=
        'Auto-cancel pending pipelines. This action toggles between an enabled state and a disabled state; it is not a boolean.'
        )
    auto_devops_deploy_strategy: Optional[str] = Field(None, description=
        'Auto Deploy strategy (continuous, manual or timed_incremental).')
    auto_devops_enabled: Optional[bool] = Field(None, description=
        'Enable Auto DevOps for this project.')
    autoclose_referenced_issues: Optional[bool] = Field(None, description=
        'Set whether auto-closing referenced issues on default branch.')
    avatar: Optional[Union[str, Any]] = Field(None, description=
        'Image file for avatar of the project.')
    build_git_strategy: Optional[str] = Field(None, description=
        'The Git strategy. Defaults to fetch.')
    build_timeout: Optional[int] = Field(None, description=
        'The maximum amount of time, in seconds, that a job can run.')
    builds_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    ci_config_path: Optional[str] = Field(None, description=
        'The path to CI configuration file.')
    container_expiration_policy_attributes: Optional[dict] = Field(None,
        description='Update the image cleanup policy for this project.')
    container_registry_access_level: Optional[str] = Field(None,
        description=
        'Set visibility of container registry, for this project, to one of disabled, private or enabled.'
        )
    container_registry_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable container registry for this project. Use container_registry_access_level instead.'
        )
    default_branch: Optional[str] = Field(None, description=
        'The default branch name. Requires initialize_with_readme to be true.')
    description: Optional[str] = Field(None, description=
        'Short project description.')
    emails_disabled: Optional[bool] = Field(None, description=
        'Disable email notifications.')
    external_authorization_classification_label: Optional[str] = Field(None,
        description='The classification label for the project.')
    forking_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    group_with_project_templates_id: Optional[int] = Field(None,
        description=
        'For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true.'
        )
    import_url: Optional[str] = Field(None, description=
        'URL to import repository from. When the URL value isn’t empty, you must not set initialize_with_readme to true. Doing so might result in the following error: not a git repository.'
        )
    initialize_with_readme: Optional[bool] = Field(None, description=
        'Whether to create a Git repository with just a README.md file. Default is false.'
        )
    issues_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    issues_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable issues for this project. Use issues_access_level instead.'
        )
    jobs_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable jobs for this project. Use builds_access_level instead.'
        )
    lfs_enabled: Optional[bool] = Field(None, description='Enable LFS.')
    merge_method: Optional[str] = Field(None, description=
        'Set the merge method used.')
    merge_pipelines_enabled: Optional[bool] = Field(None, description=
        'Enable or disable merge pipelines.')
    merge_requests_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    merge_requests_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable merge requests for this project. Use merge_requests_access_level instead.'
        )
    merge_trains_enabled: Optional[bool] = Field(None, description=
        'Enable or disable merge trains.')
    mirror_trigger_builds: Optional[bool] = Field(None, description=
        'Pull mirroring triggers builds.')
    mirror: Optional[bool] = Field(None, description=
        'Enables pull mirroring in a project.')
    namespace_id: Optional[int] = Field(None, description=
        'Namespace for the new project (defaults to the current user’s namespace).'
        )
    only_allow_merge_if_all_discussions_are_resolved: Optional[bool] = Field(
        None, description=
        'Set whether merge requests can only be merged when all the discussions are resolved.'
        )
    only_allow_merge_if_pipeline_succeeds: Optional[bool] = Field(None,
        description=
        'Set whether merge requests can only be merged with successful pipelines.'
        )
    packages_enabled: Optional[bool] = Field(None, description=
        'Enable or disable packages repository feature.')
    pages_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, enabled, or public.')
    printing_merge_request_link_enabled: Optional[bool] = Field(None,
        description=
        'Show link to create/view merge request when pushing from the command line.'
        )
    public_builds: Optional[bool] = Field(None, description=
        'If true, jobs can be viewed by non-project members.')
    releases_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    environments_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    feature_flags_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    infrastructure_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    monitor_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    remove_source_branch_after_merge: Optional[bool] = Field(None,
        description=
        'Enable Delete source branch option by default for all new merge requests.'
        )
    repository_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    repository_storage: Optional[str] = Field(None, description=
        'Which storage shard the repository is on. (administrator only)')
    request_access_enabled: Optional[bool] = Field(None, description=
        'Allow users to request member access.')
    requirements_access_level: Optional[str] = Field(None, description=
        'One of disabled, private or enabled')
    resolve_outdated_diff_discussions: Optional[bool] = Field(None,
        description=
        'Automatically resolve merge request diffs discussions on lines changed with a push.'
        )
    security_and_compliance_access_level: Optional[str] = Field(None,
        description=
        '(GitLab 14.9 and later) Security and compliance access level. One of disabled, private, or enabled.'
        )
    shared_runners_enabled: Optional[bool] = Field(None, description=
        'Enable shared runners for this project.')
    group_runners_enabled: Optional[bool] = Field(None, description=
        'Enable group runners for this project.')
    snippets_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    snippets_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable snippets for this project. Use snippets_access_level instead.'
        )
    squash_option: Optional[str] = Field(None, description=
        'One of never, always, default_on, or default_off.')
    tag_list: Optional[list] = Field(None, description=
        '(Deprecated in GitLab 14.0) The list of tags for a project; put array of tags, that should be finally assigned to a project. Use topics instead.'
        )
    template_name: Optional[str] = Field(None, description=
        'When used without use_custom_template, name of a built-in project template.'
        )
    template_project_id: Optional[int] = Field(None, description=
        'When used with use_custom_template, project ID of a custom project template.'
        )
    topics: Optional[list] = Field(None, description=
        'The list of topics for a project; put array of topics, that should be finally assigned to a project. (Introduced in GitLab 14.0.)'
        )
    use_custom_template: Optional[bool] = Field(None, description=
        'Use either custom instance or group (with group_with_project_templates_id) project template.'
        )
    visibility: Optional[str] = Field(None, description=
        'See project visibility level.')
    wiki_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    wiki_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable wiki for this project. Use wiki_access_level instead.'
        )
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
    container_expiration_policy_attributes: Optional[
        ContainerExpirationPolicyAttributes] = None
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

# Classes from file: merge_requests.py
class ProjectsMergeRequestCreate(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    source_branch: str = Field(description='The source branch name.')
    target_branch: str = Field(description='The target branch name.')
    title: str = Field(description='The title of merge request.')
    allow_collaboration: Optional[bool] = Field(None, description=
        'Allow commits from members who can merge to the target branch.')
    approvals_before_merge: Optional[int] = Field(None, description=
        'The amount of approvals required before merging.')
    allow_maintainer_to_push: Optional[bool] = Field(None, description=
        'Allow users who can merge to the target branch to push to the source branch.'
        )
    assignee_id: Optional[int] = Field(None, description=
        'The ID of a user to assign merge request.')
    assignee_ids: Optional[List[int]] = Field(None, description=
        'The IDs of users to assign merge request.')
    description: Optional[str] = Field(None, description=
        'The description of merge request.')
    labels: Optional[str] = Field(None, description=
        'Comma-separated list of label names.')
    milestone_id: Optional[int] = Field(None, description=
        'The global ID of a milestone to assign merge request.')
    remove_source_branch: Optional[bool] = Field(None, description=
        'Flag indicating if a merge request should remove the source branch when merging.'
        )
    reviewer_ids: Optional[List[int]] = Field(None, description=
        'The IDs of users to request review from when merge request created.')
    squash: Optional[bool] = Field(None, description=
        'Squash commits into a single commit when merging.')
    squash_on_merge: Optional[bool] = Field(None, description=
        'Squash commits into a single commit after merging.')
    target_project_id: Optional[int] = Field(None, description=
        'The target project ID. If the user is a maintainer of the target project, the source project is set as the target_project_id.'
        )

# Classes from file: member_roles.py

# Classes from file: resource_weight_events.py

# Classes from file: search_migrations.py

# Classes from file: integrations.py

# Classes from file: emoji_reactions.py
class AwardEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
class SingleEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class NewEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    name: str
class DeleteEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class ListCommentEmojiReactionsParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
class GetCommentEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int
class AwardCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    name: str
class DeleteCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int

# Classes from file: settings_(application).py

# Classes from file: pipelines.py
class Scope(str, Enum):
    running = 'running'
    pending = 'pending'
    finished = 'finished'
    branches = 'branches'
    tags = 'tags'
class Status(str, Enum):
    created = 'created'
    waiting_for_resource = 'waiting_for_resource'
    preparing = 'preparing'
    pending = 'pending'
    running = 'running'
    success = 'success'
    failed = 'failed'
    canceled = 'canceled'
    skipped = 'skipped'
    manual = 'manual'
    scheduled = 'scheduled'
class Source(str, Enum):
    push = 'push'
    web = 'web'
    trigger = 'trigger'
    schedule = 'schedule'
    api = 'api'
    external = 'external'
    pipeline = 'pipeline'
    chat = 'chat'
    webide = 'webide'
    merge_request_event = 'merge_request_event'
    external_pull_request_event = 'external_pull_request_event'
    parent_pipeline = 'parent_pipeline'
    ondemand_dast_scan = 'ondemand_dast_scan'
    ondemand_dast_validation = 'ondemand_dast_validation'
class OrderBy(str, Enum):
    id = 'id'
    status = 'status'
    ref = 'ref'
    updated_at = 'updated_at'
    user_id = 'user_id'
class Sort(str, Enum):
    asc = 'asc'
    desc = 'desc'
class ListProjectPipelinesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    scope: Optional[Scope]
    status: Optional[Status]
    source: Optional[Source]
    ref: Optional[str]
    sha: Optional[str]
    yaml_errors: Optional[bool]
    username: Optional[str]
    updated_after: Optional[datetime]
    updated_before: Optional[datetime]
    name: Optional[str]
    order_by: Optional[OrderBy]
    sort: Optional[Sort]
class GetPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineVariablesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportSummaryInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetLatestPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    ref: Optional[str] = Field(None, description=
        'The branch or tag to check for the latest pipeline. Defaults to the default branch when not specified.'
        )
class CreatePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    ref: str = Field(..., description=
        'The branch or tag to run the pipeline on.')
    variables: Optional[List[Dict[str, Union[str, Dict[str, str]]]]] = Field(
        None, description=
        'An array of hashes containing the variables available in the pipeline.'
        )
class RetryJobsInPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class CancelPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class DeletePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')

# Classes from file: lint_.gitlab_ci.yml.py

# Classes from file: service_data.py

# Classes from file: dependencies.py
class ProjectsIdDependencies(BaseModel):
    id: Union[int, str]
    package_manager: Optional[str] = None

# Classes from file: project_badges.py
class ProjectsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class ProjectsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesCreate(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str

# Classes from file: helm.py

# Classes from file: namespaces.py

# Classes from file: links_(issue).py

# Classes from file: deploy_keys.py
class Deploykeys(BaseModel):
    public: Optional[bool] = None
class ProjectsIdDeploykeys(BaseModel):
    id: int
class UsersIdorusernameProjectdeploykeys(BaseModel):
    id_or_username: str
class ProjectsIdDeploykeysKeyidSingle(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysAdd(BaseModel):
    id: int
    key: str
    title: str
    can_push: Optional[bool] = None
    expires_at: Optional[datetime] = None
class ProjectsIdDeploykeysKeyidUpdate(BaseModel):
    id: int
    can_push: Optional[bool] = None
    title: Optional[str] = None
class ProjectsIdDeploykeysKeyidDelete(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysKeyidEnable(BaseModel):
    id: int
    key_id: int

# Classes from file: issue_boards_(project).py

# Classes from file: job_token_scopes.py
class GetProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
class PatchProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
    enabled: bool
class GetProjectCICDJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
class CreateNewProjectToJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int
class RemoveProjectFromJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int

# Classes from file: merge_request_context_commits.py

# Classes from file: system_hooks.py

# Classes from file: user_starred_metrics_dashboards.py
class ProjectsIdMetricsUserstarreddashboardsAdd(BaseModel):
    id: Union[int, str]
    dashboard_path: str
class ProjectsIdMetricsUserstarreddashboardsRemove(BaseModel):
    id: Union[int, str]
    dashboard_path: Optional[str] = None

# Classes from file: secure_files.py

# Classes from file: issues.py

# Classes from file: labels_(group).py

# Classes from file: tags.py

# Classes from file: release_links.py

# Classes from file: import.py

# Classes from file: pages_domains.py

# Classes from file: pipeline_triggers.py
class ListProjectTriggerTokensInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
class GetTriggerTokenDetailsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class CreateTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    description: str = Field(..., description='The trigger name.')
class UpdateProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
    description: Optional[str] = Field(None, description='The trigger name.')
class RemoveProjectTriggerTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    trigger_id: int = Field(..., description='The trigger ID.')
class TriggerPipelineWithTokenInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    ref: str = Field(..., description=
        'The branch or tag to run the pipeline on.')
    token: str = Field(..., description='The trigger token or CI/CD job token.'
        )
    variables: Optional[Dict[str, str]] = Field(None, description=
        'A map of key-valued strings containing the pipeline variables.')

# Classes from file: linked_epics.py

# Classes from file: resource_state_events.py

# Classes from file: project_remote_mirrors.py

# Classes from file: to_do_lists.py

# Classes from file: deploy_tokens.py

# Classes from file: dashboard_annotations.py
class CreateNewAnnotation(BaseModel):
    id: Union[int, str]
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str] = None
    description: str

    @validator('starting_at', 'ending_at', pre=True)
    def parse_iso8601(cls, v):
        if v is None:
            return v
        try:
            return datetime.fromisoformat(v)
        except ValueError:
            raise ValueError('datetime is not in ISO 8601 format')

# Classes from file: geo_nodes.py

# Classes from file: merge_request_approvals.py

# Classes from file: conan.py
class RoutePrefix(str, Enum):
    instance_level = '/packages/conan/v1'
    project_level = '/projects/:id/packages/conan/v1`'
class Ping(BaseModel):
    route_prefix: RoutePrefix = Field(description=
        'pick either instance_level or project_level')
class SearchInput(BaseModel):
    route_prefix: RoutePrefix
    q: str = Field(..., description=
        'Search query. You can use * as a wildcard.')
class AuthenticateInput(BaseModel):
    route_prefix: RoutePrefix
class CheckCredentialsInput(BaseModel):
    route_prefix: RoutePrefix
class RecipeSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageSnapshotInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
class PackageManifestInput(BaseModel):
    route_prefix: RoutePrefix
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
class RecipeManifest(BaseModel):
    package_name: str = Field(description='Name of a package.')
    package_version: str = Field(description='Version of a package.')
    package_username: str = Field(description=
        'Conan username of a package. This attribute is the +-separated full path of your project.'
        )
    package_channel: str = Field(description='Channel of a package.')
class PackageManifest(RecipeManifest):
    conan_package_reference: str = Field(description=
        'Reference hash of a Conan package. Conan generates this value.')
class UploadUrls(RecipeManifest):
    files: Dict[str, int] = Field(description=
        'Dictionary of file names with their sizes.')
class PackageUploadUrlsInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    conan_package_reference: str
    file_sizes: Dict[str, int]
class DownloadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
class UploadRecipeFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    file_name: str
    file_content: str
class DownloadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
class UploadPackageFileInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str
    recipe_revision: str = '0'
    conan_package_reference: str
    package_revision: str = '0'
    file_name: str
    file_content: str
class DeletePackageInput(BaseModel):
    package_name: str
    package_version: str
    package_username: str
    package_channel: str

# Classes from file: custom_attributes.py
class UsersIdCustomattributes(BaseModel):
    id: int
class GroupsIdCustomattributes(BaseModel):
    id: int
class ProjectsIdCustomattributes(BaseModel):
    id: int
class UsersIdCustomattributesKey(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKey(BaseModel):
    id: int
    key: str
class UsersIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class GroupsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class ProjectsIdCustomattributesKeySet(BaseModel):
    id: int
    key: str
    value: str
class UsersIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class GroupsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str
class ProjectsIdCustomattributesKeyDelete(BaseModel):
    id: int
    key: str

# Classes from file: epics.py
class NotMatch(BaseModel):
    author_id: Optional[int] = Field(None, description=
        'Can exclude by author ID')
    author_username: Optional[str] = Field(None, description=
        'Can exclude by author username (GitLab 14.7 and later)')
    labels: Optional[str] = Field(None, description='Can exclude by labels')
class GroupsIdEpics(BaseModel):
    id: Union[int, str]
    author_id: Optional[int] = None
    author_username: Optional[str] = None
    labels: Optional[str] = None
    with_labels_details: Optional[bool] = None
    order_by: Optional[str] = None
    sort: Optional[str] = None
    search: Optional[str] = None
    state: Optional[str] = None
    created_after: Optional[datetime] = None
    created_before: Optional[datetime] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    include_ancestor_groups: Optional[bool] = None
    include_descendant_groups: Optional[bool] = None
    my_reaction_emoji: Optional[str] = None
    not_: Optional[NotMatch] = Field(None, alias='not', description=
        'Return epics that do not match the parameters supplied')
class SingleEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class NewEpicInput(BaseModel):
    id: Union[int, str]
    title: str
    labels: Optional[str]
    description: Optional[str]
    color: Optional[str]
    confidential: Optional[bool]
    created_at: Optional[datetime]
    start_date_is_fixed: Optional[bool]
    start_date_fixed: Optional[str]
    due_date_is_fixed: Optional[bool]
    due_date_fixed: Optional[str]
    parent_id: Optional[Union[int, str]]
class UpdateEpic(BaseModel):
    id: int
    epic_iid: int
    add_labels: Optional[str] = None
    confidential: Optional[bool] = None
    description: Optional[str] = None
    due_date_fixed: Optional[str] = None
    due_date_is_fixed: Optional[bool] = None
    labels: Optional[str] = None
    parent_id: Optional[int] = None
    remove_labels: Optional[str] = None
    start_date_fixed: Optional[str] = None
    start_date_is_fixed: Optional[bool] = None
    state_event: Optional[str] = None
    title: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
class DeleteEpic(BaseModel):
    id: Union[int, str]
    epic_iid: Union[int, str]
class CreateAToDoItem(BaseModel):
    id: Union[int, str]
    epic_iid: int

# Classes from file: issues_(epic).py

# Classes from file: suggestions.py

# Classes from file: product_analytics.py

# Classes from file: discussions.py
class ListProjectIssueDiscussionItems(BaseModel):
    id: Union[int, str]
    issue_iid: int
class GetSingleIssueDiscussionItem(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
class CreateNewIssueThread(BaseModel):
    body: str
    id: Union[int, str]
    issue_iid: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingIssueThreadPayload(BaseModel):
    body: str = Field(..., description='The content of the note or reply.')
    discussion_id: int = Field(..., description='The ID of a thread.')
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    issue_iid: int = Field(..., description='The IID of an issue.')
    note_id: int = Field(..., description='The ID of a thread note.')
    created_at: Optional[datetime] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyExistingIssueThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    issue_iid: int
    note_id: int
class DeleteIssueThreadNote(BaseModel):
    id: Union[int, str]
    issue_iid: int
    discussion_id: int
    note_id: int
class ProjectsIdSnippetsSnippetidDiscussions(BaseModel):
    id: Union[int, str]
    snippet_id: int
class ListProjectSnippetDiscussionItems(BaseModel):
    id: Union[int, str]
    snippet_id: int
class GetSingleSnippetDiscussionItem(BaseModel):
    id: Union[int, str]
    snippet_id: int
    discussion_id: int
class CreateNewSnippetThread(BaseModel):
    body: str
    id: Union[int, str]
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class AddNoteToExistingSnippetThread(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
    created_at: Optional[Union[str, datetime]]
class ModifyExistingSnippetThreadNote(BaseModel):
    body: str
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class DeleteSnippetThreadNote(BaseModel):
    discussion_id: int
    id: Union[int, str]
    note_id: int
    snippet_id: int
class GroupsIdEpicsEpicidDiscussions(BaseModel):
    epic_id: int
    id: Union[int, str]
class SingleEpicDiscussionItem(BaseModel):
    discussion_id: int = Field(description='The ID of a discussion item.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
class CreateNewEpicThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    created_at: Optional[Union[str, datetime]] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class AddNoteToEpicThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[Union[str, datetime]] = Field(None, description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyEpicThreadNote(BaseModel):
    body: str = Field(description='The content of note or reply.')
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class DeleteEpicThreadNote(BaseModel):
    discussion_id: int = Field(description='The ID of a thread.')
    epic_id: int = Field(description='The ID of an epic.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the group.')
    note_id: int = Field(description='The ID of a thread note.')
class ListMergeRequestDiscussionItems(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class SingleMergeRequestDiscussionItem(BaseModel):
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class BasicMergeRequestParams(BaseModel):
    body: str = Field(description='The content of the thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
class DiffNoteParams(BaseModel):
    base_sha: str = Field(description='Base commit SHA in the source branch.')
    head_sha: str = Field(description=
        'SHA referencing HEAD of this merge request.')
    start_sha: str = Field(description=
        'SHA referencing commit in target branch.')
    new_path: str = Field(description='File path after change.')
    old_path: str = Field(description='File path before change.')
    position_type: str = Field(description=
        'Type of the position reference. Allowed values: text or image.')
class TextDiffNoteParams(BaseModel):
    new_line: Optional[int] = Field(description=
        'For text diff notes, the line number after change.')
    old_line: Optional[int] = Field(description=
        'For text diff notes, the line number before change.')
class ImageDiffNoteParams(BaseModel):
    width: Optional[int] = Field(description=
        'For image diff notes, width of the image.')
    height: Optional[int] = Field(description=
        'For image diff notes, height of the image.')
    x: Optional[float] = Field(description=
        'For image diff notes, X coordinate.')
    y: Optional[float] = Field(description=
        'For image diff notes, Y coordinate.')
class MultilineCommentsParams(BaseModel):
    line_range: dict = Field(description=
        'Line range for a multi-line diff note.')
class CreateNewMergeRequestThread(BasicMergeRequestParams):
    position: DiffNoteParams = Field(description=
        'Position when creating a diff note.')
    text_position: Optional[TextDiffNoteParams] = Field(description=
        'Position parameters for text diff notes.')
    image_position: Optional[ImageDiffNoteParams] = Field(description=
        'Position parameters for image diff notes.')
    multiline_comments: Optional[MultilineCommentsParams] = Field(description
        ='Parameters for multiline comments.')
    commit_id: Optional[str] = Field(description=
        'SHA referencing commit to start this thread on.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class ResolveMergeRequestThread(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    discussion_id: str = Field(description='The ID of a thread.')
    resolved: bool = Field(description='Resolve or unresolve the discussion.')
class AddNoteToMergeRequestThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    discussion_id: str = Field(description='The ID of a thread.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class ModifyMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description=
        'The content of the note or reply. Exactly one of body or resolved must be set.'
        )
    resolved: Optional[bool] = Field(description=
        'Resolve or unresolve the note. Exactly one of body or resolved must be set.'
        )
class DeleteMergeRequestThreadNote(BaseModel):
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    merge_request_iid: int = Field(description='The IID of a merge request.')
    note_id: int = Field(description='The ID of a thread note.')
class ListProjectCommitDiscussionItems(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
class GetSingleCommitDiscussionItem(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a discussion item.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
class Position(BaseModel):
    base_sha: str = Field(description='SHA of the parent commit.')
    head_sha: str = Field(description=
        'The SHA of this commit. Same as commit_id.')
    start_sha: str = Field(description='SHA of the parent commit.')
    position_type: str = Field(description=
        'Type of the position reference. Allowed values: text or image.')
    hash: Optional[str] = Field(description=
        'Position when creating a diff note.')
    new_path: Optional[str] = Field(description='File path after change.')
    new_line: Optional[int] = Field(description='Line number after change.')
    old_path: Optional[str] = Field(description='File path before change.')
    old_line: Optional[int] = Field(description='Line number before change.')
    height: Optional[int] = Field(description=
        'For image diff notes, image height.')
    width: Optional[int] = Field(description=
        'For image diff notes, image width.')
    x: Optional[int] = Field(description='For image diff notes, X coordinate.')
    y: Optional[int] = Field(description='For image diff notes, Y coordinate.')
class CreateNewCommitThread(BaseModel):
    body: str = Field(description='The content of the thread.')
    commit_id: str = Field(description='The SHA of a commit.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    position: Position = Field(description=
        'Position when creating a diff note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted. Requires administrator or project/group owner rights.'
        )
class AddNoteToCommitThread(BaseModel):
    body: str = Field(description='The content of the note or reply.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    created_at: Optional[str] = Field(description=
        'Date time string, ISO 8601 formatted, such as 2016-03-11T03:45:40Z. Requires administrator or project/group owner rights.'
        )
class ModifyCommitThreadNote(BaseModel):
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    note_id: int = Field(description='The ID of a thread note.')
    body: Optional[str] = Field(description='The content of a note.')
class DeleteCommitThreadNote(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    commit_id: str = Field(description='The SHA of a commit.')
    discussion_id: str = Field(description='The ID of a thread.')
    note_id: int = Field(description='The ID of a thread note.')

# Classes from file: project_relations_export.py

# Classes from file: snippets_(project).py

# Classes from file: branches.py
class ProjectsIdRepositoryBranches(BaseModel):
    id: int
    search: Optional[str] = None
    regex: Optional[str] = None
class ProjectsIdRepositoryBranchesBranchSingle(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryBranchesCreate(BaseModel):
    id: int
    branch: str
    ref: str
class ProjectsIdRepositoryBranchesBranch(BaseModel):
    id: int
    branch: str
class ProjectsIdRepositoryMergedbranches(BaseModel):
    id: int

# Classes from file: metadata.py

# Classes from file: version.py

# Classes from file: protected_tags.py

# Classes from file: issue_boards_(group).py

# Classes from file: repository_submodules.py

# Classes from file: milestones_(group).py

# Classes from file: members.py

# Classes from file: protected_branches.py

# Classes from file: commits.py
class ProjectsIdRepositoryCommits(BaseModel):
    id: int
    ref_name: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None
    path: Optional[str] = None
    author: Optional[str] = None
    all: Optional[bool]
    with_stats: Optional[bool]
    first_parent: Optional[bool]
    order: Optional[str]
    trailers: Optional[bool]
class ProjectsIdRepositoryCommitsSha(BaseModel):
    id: int
    sha: str
    stats: Optional[bool] = None
class ProjectsIdRepositoryCommitsShaRefs(BaseModel):
    id: int
    sha: str
    type: Optional[str] = None
class ProjectsIdRepositoryCommitsShaCherrypick(BaseModel):
    id: int
    sha: str
    branch: str
    dry_run: Optional[bool] = None
    message: Optional[str] = None
class ProjectsIdRepositoryCommitsShaRevert(BaseModel):
    id: int
    sha: str
    branch: str
    dry_run: Optional[bool] = None
class ProjectsIdRepositoryCommitsShaDiff(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaComments(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaCommentsPost(BaseModel):
    id: int
    sha: str
    note: str
    path: Optional[str] = None
    line: Optional[int] = None
    line_type: Optional[str] = None
class ProjectsIdRepositoryCommitsShaDiscussions(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaStatuses(BaseModel):
    id: int
    sha: str
    ref: Optional[str] = None
    stage: Optional[str] = None
    name: Optional[str] = None
    all: Optional[bool] = None
class ProjectsIdStatusesSha(BaseModel):
    id: int
    sha: str
    state: str
    ref: Optional[str] = None
    context: Optional[str] = None
    name: Optional[str] = None
    target_url: Optional[str] = None
    description: Optional[str] = None
    coverage: Optional[float] = None
    pipeline_id: Optional[int] = None
class ProjectsIdRepositoryCommitsShaMergerequests(BaseModel):
    id: int
    sha: str
class ProjectsIdRepositoryCommitsShaSignature(BaseModel):
    id: int
    sha: str

# Classes from file: application_appearance.py
class ApplicationAppearance(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    pwa_name: Optional[str] = None
    pwa_short_name: Optional[str] = None
    pwa_description: Optional[str] = None
    pwa_icon: Optional[Any] = None
    logo: Optional[Any] = None
    header_logo: Optional[Any] = None
    favicon: Optional[Any] = None
    new_project_guidelines: Optional[str] = None
    profile_image_guidelines: Optional[str] = None
    header_message: Optional[str] = None
    footer_message: Optional[str] = None
    message_background_color: Optional[str] = None
    message_font_color: Optional[str] = None
    email_header_and_footer_enabled: Optional[bool] = None
class ChangeLogo(BaseModel):
    logo: Any
    pwa_icon: Any

# Classes from file: users.py

# Classes from file: project_vulnerabilities.py

# Classes from file: draft_notes.py
class ProjectsIdMergerequestsMergerequestiidDraftnotes(BaseModel):
    id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidSingle(
    BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesCreate(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    note: str
    commit_id: Optional[str] = None
    in_reply_to_discussion_id: Optional[int] = None
    resolve_discussion: Optional[bool] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidModify(
    BaseModel):
    id: Union[int, str]
    draft_note_id: int
    merge_request_iid: int
    note: Optional[str] = None
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidDelete(
    BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesDraftnoteidPublish(
    BaseModel):
    draft_note_id: int
    id: Union[int, str]
    merge_request_iid: int
class ProjectsIdMergerequestsMergerequestiidDraftnotesBulkpublish(BaseModel):
    id: Union[int, str]
    merge_request_iid: int

# Classes from file: group_migration_by_direct_transfer.py

# Classes from file: resource_iteration_events.py

# Classes from file: agents_for_kubernetes.py
class ListTheAgentsForAProject(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
class GetDetailsAboutAnAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class RegisterAnAgentWithAProject(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    name: str = Field(description='Name for the agent')
class DeleteARegisteredAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class ListTokensForAnAgent(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
class GetSingleAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')
class CreateAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    name: int = Field(description='Name for the token')
    description: Optional[int] = Field(None, description=
        'Description for the token')
class RevokeAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description=
        'ID or URL-encoded path of the project maintained by the authenticated user'
        )
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')

# Classes from file: project_import_export.py

# Classes from file: project_level_protected_environments.py

# Classes from file: composer.py
class GroupIdPackagesComposerPackages(BaseModel):
    id: Union[int, str]
class GroupIdPackagesComposerPSha(BaseModel):
    id: Union[int, str]
    sha: str
class V1PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str
class V2PackageMetadataInput(BaseModel):
    id: Union[int, str]
    package_name: str
class CreateAPackageInput(BaseModel):
    id: Union[int, str]
    tag: Optional[str] = None
    branch: Optional[str] = None
class ProjectsIdPackagesComposerArchivesPackagename(BaseModel):
    id: Union[int, str]
    package_name: str
    sha: str

# Classes from file: alert_management.py
class ListMetricImages(BaseModel):
    id: int
    alert_iid: int
class UpdateMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int
    url: Optional[str] = None
    url_text: Optional[str] = None
class DeleteMetricImage(BaseModel):
    id: int
    alert_iid: int
    image_id: int

# Classes from file: sidekiq_queues.py

# Classes from file: vulnerability_export.py
class SecurityProjectsIdVulnerabilityexports(BaseModel):
    id: Union[int, str]
class SecurityGroupsIdVulnerabilityexports(BaseModel):
    id: Union[int, str]
class SecurityVulnerabilityexportsId(BaseModel):
    id: Union[int, str]
class SecurityVulnerabilityexportsIdDownload(BaseModel):
    id: Union[int, str]

# Classes from file: events.py
class Events(BaseModel):
    action: Optional[str] = None
    target_type: Optional[str] = None
    before: Optional[datetime] = Field(None, description=
        'Include only events created before a certain date.')
    after: Optional[datetime] = Field(None, description=
        'Include only events created after a particular date.')
    target_id: Optional[int] = None
    author_id: Optional[int] = None
    search: Optional[str] = None
class AuthenticatedUserEvents(Events):
    scope: Optional[str] = None
    sort: Optional[str] = None
class UserContributionEvents(Events):
    id: int
    sort: Optional[str] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
class ProjectVisibleEvents(Events):
    project_id: int
    sort: Optional[str] = None

# Classes from file: group_import_export.py

# Classes from file: dora4_metrics.py
class ProjectsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None
class GroupsIdDoraMetrics(BaseModel):
    id: int
    metric: str
    end_date: Optional[str] = None
    environment_tiers: Optional[List[str]] = None
    interval: Optional[str] = None
    start_date: Optional[str] = None

# Classes from file: plan_limits.py

# Classes from file: statistics_(application).py

# Classes from file: group_repository_storage_moves.py

# Classes from file: iterations_(project).py

# Classes from file: applications.py
class Applications(BaseModel):
    name: str
    redirect_uri: str
    scopes: str
    confidential: Optional[bool] = None
class ApplicationsId(BaseModel):
    id: int

# Classes from file: saml.py

# Classes from file: dependency_proxy.py
class GroupsIdDependencyproxyCache(BaseModel):
    id: int

# Classes from file: group_relations_export.py

# Classes from file: metrics_dashboard_annotations.py
class EnvironmentsIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str
class ClustersIdMetricsdashboardAnnotations(BaseModel):
    dashboard_path: str
    starting_at: str
    ending_at: Optional[str]
    description: str

# Classes from file: personal_access_tokens.py

# Classes from file: __init__.py

# Classes from file: instance_level_ci_cd_variables.py

# Classes from file: geo_sites.py

# Classes from file: visual_review_discussions_deprecated.py
class PositionData(BaseModel):
    base_sha: str
    start_sha: str
    head_sha: str
    position_type: str
    new_path: Optional[str] = None
    new_line: Optional[int] = None
    old_path: Optional[str] = None
    old_line: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None
class CreateNewMergeRequestThread(BaseModel):
    id: Union[int, str]
    merge_request_iid: int
    body: str
    position: Optional[PositionData] = None

# Classes from file: feature_flags.py
class StrategyParameters(BaseModel):
    pass
class StrategyScope(BaseModel):
    environment_scope: Optional[str] = None
class Strategy(BaseModel):
    name: Optional[str] = None
    parameters: Optional[StrategyParameters] = None
    scopes: Optional[List[StrategyScope]] = None
class ListFeatureFlagsForProject(BaseModel):
    id: Union[int, str]
    scope: Optional[str] = None
class GetSingleFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
class CreateFeatureFlag(BaseModel):
    id: Union[int, str]
    name: str
    version: str
    description: Optional[str] = None
    active: Optional[bool] = None
    strategies: Optional[List[Strategy]] = None
class UpdateFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str
    description: Optional[str] = None
    active: Optional[bool] = None
    name: Optional[str] = None
    strategies: Optional[List[Strategy]] = None
class DeleteFeatureFlag(BaseModel):
    id: Union[int, str]
    feature_flag_name: str

# Classes from file: pipelines_schedules.py
class GetAllPipelineSchedulesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    scope: Optional[str] = Field(None, description=
        'The scope of pipeline schedules, must be one of: active, inactive.')
class GetSinglePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class GetPipelinesTriggeredByScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class CreateNewPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    description: str = Field(..., description=
        'The description of the pipeline schedule.')
    ref: str = Field(..., description=
        'The branch or tag name that is triggered.')
    cron: str = Field(..., description=
        'The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description=
        'The time zone supported by ActiveSupport::TimeZone, for example: Pacific Time (US & Canada) (default: UTC).'
        )
    active: Optional[bool] = Field(None, description=
        'The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated (default: true).'
        )
class EditPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    description: Optional[str] = Field(None, description=
        'The description of the pipeline schedule.')
    ref: Optional[str] = Field(None, description=
        'The branch or tag name that is triggered.')
    cron: Optional[str] = Field(None, description=
        'The cron schedule, for example: 0 1 * * *.')
    cron_timezone: Optional[str] = Field(None, description=
        'The time zone supported by ActiveSupport::TimeZone (for example Pacific Time (US & Canada)), or TZInfo::Timezone (for example America/Los_Angeles).'
        )
    active: Optional[bool] = Field(None, description=
        'The activation of pipeline schedule. If false is set, the pipeline schedule is initially deactivated.'
        )
class TakeOwnershipOfPipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class DeletePipelineScheduleInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class RunScheduledPipelineImmediatelyInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
class CreatePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description=
        'The key of a variable; must have no more than 255 characters; only A-Z, a-z, 0-9, and _ are allowed.'
        )
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description=
        'The type of a variable. Available types are: env_var (default) and file.'
        )
class EditPipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')
    value: str = Field(..., description='The value of a variable.')
    variable_type: Optional[str] = Field(None, description=
        'The type of a variable. Available types are: env_var (default) and file.'
        )
class DeletePipelineScheduleVariableInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_schedule_id: int = Field(..., description=
        'The pipeline schedule ID.')
    key: str = Field(..., description='The key of a variable.')

# Classes from file: dockerfile_templates.py
class TemplatesDockerfilesKey(BaseModel):
    key: str

# Classes from file: group_releases.py

# Classes from file: keys.py

# Classes from file: packages.py

# Classes from file: labels_(project).py

# Classes from file: freeze_periods.py

# Classes from file: broadcast_messages.py
class GetASpecificBroadcastMessage(BaseModel):
    id: int
class CreateABroadcastMessage(BaseModel):
    message: str
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class UpdateABroadcastMessage(BaseModel):
    id: int
    message: Optional[str]
    starts_at: Optional[datetime]
    ends_at: Optional[datetime]
    font: Optional[str]
    target_access_levels: Optional[List[int]]
    target_path: Optional[str]
    broadcast_type: Optional[str]
    dismissable: Optional[bool]
class DeleteABroadcastMessage(BaseModel):
    id: int

# Classes from file: groups.py

# Classes from file: wikis_project.py
class ProjectsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class ProjectsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class ProjectsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class ProjectsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class ProjectsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None

# Classes from file: npm.py

# Classes from file: avatar.py
class Avatar(BaseModel):
    email: str
    size: Optional[int] = None

# Classes from file: resource_group.py

# Classes from file: error_tracking.py
class GetErrorTrackingSettings(BaseModel):
    id: Union[int, str]
class CreateErrorTrackingSettings(BaseModel):
    id: int
    active: bool
    integrated: bool
class EnableOrDisableTheErrorTrackingProjectSettings(BaseModel):
    id: int
    active: bool
    integrated: Optional[bool] = None
class ListProjectClientKeys(BaseModel):
    id: Union[int, str]
class CreateAClientKey(BaseModel):
    id: Union[int, str]
class DeleteAClientKey(BaseModel):
    id: Union[int, str]
    key_id: int

# Classes from file: debian_project_distributions.py
class ListAllDebianDistributionsInAProject(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class SingleDebianProjectDistributionKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianProjectDistribution(BaseModel):
    id: Union[int, str]
    codename: int

# Classes from file: resource_label_events.py

# Classes from file: repository_files.py
class ProjectIdRepositoryFiles(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    file_path: str = Field(description='URL encoded full path to new file')
    ref: str = Field(description='The name of branch, tag or commit')
class ProjectIdRepositoryFilesBlame(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    file_path: str = Field(description=
        'URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(description='The name of branch, tag or commit.')
    range_start: int = Field(description=
        'The first line of the range to blame.')
    range_end: int = Field(description='The last line of the range to blame.')
    range: Optional[dict] = Field(description='Blame range.')
class ProjectsIdRepositoryFilesFilepathRaw(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    file_path: str = Field(..., description=
        'URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(..., description=
        'The name of branch, tag or commit. Default is the HEAD of the project.'
        )
    lfs: Optional[bool] = Field(None, description=
        'Determines if the response should be Git LFS file contents, rather than the pointer. If the file is not tracked by Git LFS, ignored. Defaults to false.'
        )
class ProjectsIdRepositoryFilesFilepathCreate(BaseModel):
    branch: str = Field(description=
        'Name of the new branch to create. The commit is added to this branch.'
        )
    commit_message: str = Field(description='The commit message.')
    content: str = Field(description='The file’s content.')
    file_path: str = Field(description=
        'URL-encoded full path to new file. For example: lib%2Fclass%2Erb.')
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    author_email: Optional[str] = Field(None, description=
        'The commit author’s email address.')
    author_name: Optional[str] = Field(None, description=
        'The commit author’s name.')
    encoding: Optional[str] = Field(None, description=
        'Change encoding to base64. Default is text.')
    execute_filemode: Optional[bool] = Field(None, description=
        'Enables or disables the execute flag on the file. Can be true or false.'
        )
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathUpdate(BaseModel):
    branch: str
    commit_message: str
    content: str
    file_path: str
    id: Union[int, str]
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    encoding: Optional[str] = None
    execute_filemode: Optional[bool] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathDelete(BaseModel):
    branch: str
    commit_message: str
    file_path: str
    id: int
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description=
        'Name of the base branch to create the new branch from.')
class ProjectsIdRepositorySubmodulesSubmodule(BaseModel):
    id: int
    submodule: str
    branch: str
    commit_sha: str
    commit_message: Optional[str] = None

# Classes from file: nuget.py

# Classes from file: container_registry.py
class ContainerRegistryAccessLevelEnum(str, Enum):
    enabled = 'enabled'
    private = 'private'
    disabled = 'disabled'
class ChangeContainerRegistryVisibility(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project accessible by the authenticated user.'
        )
    container_registry_access_level: Optional[ContainerRegistryAccessLevelEnum
        ] = Field(default=None, description=
        'The desired visibility of the Container Registry. One of enabled (default), private, or disabled.'
        )
class ListProjectRegistryRepositories(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
class GroupsIdRegistryRepositories(BaseModel):
    id: Union[int, str]
class RegistryRepositoriesId(BaseModel):
    id: Union[int, str]
    tags: Optional[bool] = None
    tags_count: Optional[bool] = None
    size: Optional[bool] = None
class ProjectsIdRegistryRepositoriesRepositoryid(BaseModel):
    id: Union[int, str]
    repository_id: int
class ProjectsIdRegistryRepositoriesRepositoryidTags(BaseModel):
    id: Union[int, str]
    repository_id: int
class GetDetailsOfARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteARegistryRepositoryTag(BaseModel):
    id: Union[int, str]
    repository_id: int
    tag_name: str
class DeleteRegistryRepositoryTagsInBulk(BaseModel):
    id: Union[int, str]
    repository_id: int
    name_regex: Optional[str] = None
    name_regex_delete: str
    name_regex_keep: Optional[str] = None
    keep_n: Optional[int] = None
    older_than: Optional[str] = None
class ObtainTokenInput(BaseModel):
    CI_SERVER_URL: str = Field(description='CI server URL.')
    service: str = Field(default='container_registry', description=
        'The service type.')
    scope: str = Field(description='Scope for the token.')
class DeleteImageTagsByReferenceInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    CI_REGISTRY_IMAGE: str = Field(description='The registry image.')
    CI_COMMIT_SHORT_SHA: str = Field(description='The commit SHA.')
class ListAllContainerRepositoriesInput(BaseModel):
    CI_REGISTRY: str = Field(description='The CI registry URL.')
    admin_username: str = Field(description='The admin username.')
    admin_password: str = Field(description='The admin password.')
    service: str = Field(default='container_registry', description=
        'The service type.')
    scope: str = Field(default='registry:catalog:*', description=
        'Scope for the token.')

# Classes from file: resource_milestone_events.py

# Classes from file: templates.py
class TemplatesGitignoresKey(BaseModel):
    key: str
class TemplatesGitlabciymlsKey(BaseModel):
    key: str

# Classes from file: jobs.py
class JobScope(str, Enum):
    created = 'created'
    pending = 'pending'
    running = 'running'
    failed = 'failed'
    success = 'success'
    canceled = 'canceled'
    skipped = 'skipped'
    waiting_for_resource = 'waiting_for_resource'
    manual = 'manual'
class ListProjectJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
class ListPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
    include_retried: Optional[bool] = Field(False, description=
        'Include retried jobs in the response.')
class ListPipelineTriggerJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='ID of a pipeline.')
    scope: Union[List[JobScope], JobScope, None] = Field(None, description=
        'Scope of jobs to show.')
class GetAllowedAgentsInput(BaseModel):
    CI_JOB_TOKEN: str = Field(..., description=
        'Token value associated with the GitLab-provided CI_JOB_TOKEN variable.'
        )
class GetSingleJobInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='ID of a job.')
class JobInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    job_id: int = Field(..., description='The ID of a job.')
class JobVariable(BaseModel):
    key: str = Field(..., description='The key of the job variable.')
    value: str = Field(..., description='The value of the job variable.')
class RunJobInput(JobInput):
    job_variables_attributes: Optional[List[JobVariable]] = Field(None,
        description=
        'An array containing the custom variables available to the job.')

# Classes from file: gitignore.py
class ListAllGitignoreTemplates(BaseModel):
    pass
class GetSingleGitignoreTemplate(BaseModel):
    key: str

# Classes from file: releases.py

# Classes from file: gitlab_ci_yaml.py
class ListAllCICDYamlTemplates(BaseModel):
    pass
class GetSingleCICDYamlTemplate(BaseModel):
    key: str

# Classes from file: milestones_(project).py

# Classes from file: group_activity_analytics.py

# Classes from file: job_artifacts.py
class GetJobArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int
    job_token: Optional[str] = None
class DownloadArtifacts(BaseModel):
    id: Union[int, str]
    ref_name: str
    job: str
    job_token: Optional[str] = None
class DownloadSingleArtifactByJobID(BaseModel):
    id: Union[int, str]
    job_id: int
    artifact_path: str
    job_token: Optional[str] = None
class DownloadSingleArtifactFromSpecificTag(BaseModel):
    id: Union[int, str]
    ref_name: str
    artifact_path: str
    job: str
    job_token: Optional[str] = None
class KeepArtifacts(BaseModel):
    id: Union[int, str]
    job_id: int

# Classes from file: issues_statistics.py

# Classes from file: project_statistics.py

# Classes from file: experiments.py
class ListAllExperiments(BaseModel):
    pass

# Classes from file: scim.py

# Classes from file: feature_flag_user_lists.py

# Classes from file: vulnerability_findings.py
class ProjectsIdVulnerabilityfindings(BaseModel):
    id: int
    report_type: Optional[List[str]] = None
    scope: Optional[str] = None
    severity: Optional[List[str]] = None
    confidence: Optional[List[str]] = None
    pipeline_id: int

# Classes from file: licenses_(templates).py

# Classes from file: topics.py

# Classes from file: secrets.py

# Classes from file: debian.py
class ProjectsIdPackagesDebianFilename(BaseModel):
    id: str
    file_name: str
    distribution: Optional[str] = None
    component: Optional[str] = None
class ProjectsIdPackagesDebianPoolDistributionLetterPackagenamePackageversionFilename(
    BaseModel):
    distribution: str
    letter: str
    package_name: str
    package_version: str
    file_name: str
class DownloadADistributionReleaseFile(BaseModel):
    distribution: str
class DownloadASignedDistributionReleaseFile(BaseModel):
    distribution: str
class DownloadAReleaseFileSignature(BaseModel):
    distribution: str
class DownloadAPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadAPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadADebianInstallerPackagesIndex(BaseModel):
    distribution: str
    component: str
    architecture: str
class DowloadADebianInstallerPackagesIndexByHash(BaseModel):
    distribution: str
    component: str
    architecture: str
class DownloadASourcePackagesIndex(BaseModel):
    distribution: str
    component: str
class DownloadASourcePackagesIndexByHash(BaseModel):
    distribution: str
    component: str

# Classes from file: ruby_gems.py

# Classes from file: markdown.py

# Classes from file: debian_group_distributions.py
class ListAllDebianDistributionsInAGroup(BaseModel):
    id: Union[int, str]
    codename: Optional[str] = None
    suite: Optional[str] = None
class SingleDebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int
class GroupsIdDebiandistributionsCodenameKey(BaseModel):
    id: Union[int, str]
    codename: int
class CreateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class UpdateADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: str
    suite: Optional[str] = None
    origin: Optional[str] = None
    label: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    valid_time_duration_seconds: Optional[int] = None
    components: Optional[List[str]] = None
    architectures: Optional[List[str]] = None
class DeleteADebianGroupDistribution(BaseModel):
    id: Union[int, str]
    codename: int

# Classes from file: variables_project.py
class Variable(BaseModel):
    key: str
    value: str
    variable_type: Optional[str] = 'env_var'
    protected: Optional[bool] = False
    masked: Optional[bool] = False
    raw: Optional[bool] = False
    environment_scope: Optional[str] = '*'
    description: Optional[str] = None
class VariableFilter(BaseModel):
    environment_scope: Optional[str] = None
class GetProjectVariables(BaseModel):
    id: Union[int, str]
class GetVariable(BaseModel):
    id: Union[int, str]
    key: str
    filter: Optional[VariableFilter] = None
class CreateVariable(GetProjectVariables, Variable):
    pass
class UpdateVariable(GetVariable, Variable):
    pass
class DeleteVariable(GetVariable):
    pass

# Classes from file: links_(epic).py

# Classes from file: wikis_group.py
class GroupsIdWikis(BaseModel):
    id: Union[int, str]
    with_content: Optional[bool] = None
class GroupsIdWikisSlug(BaseModel):
    id: Union[int, str]
    slug: str
    render_html: Optional[bool] = None
    version: Optional[str] = None
class GroupsIdWikisCreate(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[str] = None
class WikiFormat(str, Enum):
    markdown = 'markdown'
    rdoc = 'rdoc'
    asciidoc = 'asciidoc'
    org = 'org'
class GroupsIdWikisSlugEdit(BaseModel):
    id: Union[int, str]
    content: str
    title: str
    format: Optional[WikiFormat] = None
    slug: str

    @validator('content', 'title', pre=True, always=True)
    def check_content_and_title(cls, v):
        if not v:
            raise ValueError('You must provide either content or title')
        return v
class GroupsIdWikisSlugDelete(BaseModel):
    id: Union[int, str]
    slug: str
class GroupsIdWikisAttachments(BaseModel):
    id: Union[int, str]
    file: str
    branch: Optional[str] = None

# Classes from file: audit_events.py
class Auditevents(BaseModel):
    created_after: Optional[str] = None
    created_before: Optional[str] = None
    entity_type: Optional[str] = None
    entity_id: Optional[int] = None
class AuditeventsId(BaseModel):
    id: int
class GroupsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class GroupsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int
class ProjectsIdAuditevents(BaseModel):
    id: int
    created_after: Optional[str] = None
    created_before: Optional[str] = None
class ProjectsIdAuditeventsAuditeventid(BaseModel):
    id: int
    audit_event_id: int

# Classes from file: project_access_tokens.py

# Classes from file: runners.py

# Classes from file: environments.py
class ProjectsIdEnvironments(BaseModel):
    id: int
    name: Optional[str] = None
    search: Optional[str] = None
    states: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentid(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsCreate(BaseModel):
    id: int
    name: str
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentsid(BaseModel):
    id: int
    environment_id: int
    external_url: Optional[str] = None
    tier: Optional[str] = None
class ProjectsIdEnvironmentsEnvironmentidDelete(BaseModel):
    id: int
    environment_id: int
class ProjectsIdEnvironmentsReviewapps(BaseModel):
    id: int
    before: Optional[datetime] = None
    limit: Optional[int] = None
    dry_run: Optional[bool] = None
class ProjectsIdEnvironmentsEnvironmentidStop(BaseModel):
    id: int
    environment_id: int
    force: Optional[bool] = None
class ProjectsIdEnvironmentsStopstale(BaseModel):
    id: int
    before: datetime

# Classes from file: group_level_protected_branches.py

# Classes from file: http_wrapper.py

# Classes from file: gitlab_pages.py

# Classes from file: marketplace.py

# Classes from file: snippets.py

# Classes from file: notes_(comments).py

# Classes from file: terraform_registry.py

# Classes from file: repositories.py
class ProjectsIdRepositoryTree(BaseModel):
    id: int
    page_token: Optional[str] = None
    pagination: Optional[str] = None
    path: Optional[str] = None
    per_page: Optional[str] = None
    recursive: bool = Field(False)
    ref: Optional[str] = None
class ProjectsIdRepositoryBlobsSha(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryBlobsShaRaw(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user'
        )
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryArchive(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    path: Optional[str] = Field(None, description=
        'The subpath of the repository to download. Defaults to the whole repository.'
        )
    sha: Optional[str] = Field(None, description=
        'The commit SHA to download. A tag, branch reference, or SHA can be used. Defaults to the tip of the default branch.'
        )
    format: Optional[str] = Field(None, description=
        "The archive format. Options are: 'bz2', 'tar', 'tar.bz2', 'tar.gz', 'tb2', 'tbz', 'tbz2', 'zip'. Defaults to 'tar.gz'."
        )
class ProjectsIdRepositoryCompare(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    from_commit_or_branch: str = Field(..., alias='from', description=
        'The commit SHA or branch name.')
    to: str = Field(..., description='The commit SHA or branch name.')
    from_project_id: Optional[int] = Field(None, description=
        'The ID to compare from.')
    straight: Optional[bool] = Field(False, description=
        'Comparison method: true for direct comparison between from and to (from..to), false to compare using merge base (from…to)’. Default is false.'
        )
class ProjectsIdRepositoryContributors(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    order_by: Optional[str] = Field(None, description=
        'Return contributors ordered by name, email, or commits (orders by commit date) fields. Default is commits.'
        )
    sort: Optional[str] = Field(None, description=
        'Return contributors sorted in asc or desc order. Default is asc.')
class ProjectsIdRepositoryMergebase(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    refs: List[str] = Field(description=
        'The refs to find the common ancestor of. Accepts multiple refs.')
class ProjectsIdRepositoryChangelog(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    version: str = Field(description=
        'The version to generate the changelog for. The format must follow semantic versioning.'
        )
    branch: Optional[str] = Field(None, description=
        'The branch to commit the changelog changes to. Defaults to the project’s default branch.'
        )
    config_file: Optional[str] = Field(None, description=
        'Path to the changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.'
        )
    date: Optional[datetime] = Field(None, description=
        'The date and time of the release. Defaults to the current time.')
    file: Optional[str] = Field(None, description=
        'The file to commit the changes to. Defaults to CHANGELOG.md.')
    from_: Optional[str] = Field(None, alias='from', description=
        'The SHA of the commit that marks the beginning of the range of commits to include in the changelog. This commit isn’t included in the changelog.'
        )
    message: Optional[str] = Field(None, description=
        'The commit message to use when committing the changes. Defaults to Add changelog for version X, where X is the value of the version argument.'
        )
    to: Optional[str] = Field(None, description=
        'The SHA of the commit that marks the end of the range of commits to include in the changelog. This commit is included in the changelog. Defaults to the branch specified in the branch attribute. Limited to 15000 commits unless the feature flag changelog_commits_limitation is disabled.'
        )
    trailer: Optional[str] = Field(None, description=
        'The Git trailer to use for including commits. Defaults to Changelog. Case-sensitive: Example does not match example or eXaMpLE.'
        )
class GenerateChangelogData(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project.')
    version: str = Field(description=
        'The version to generate the changelog for. The format must follow semantic versioning.'
        )
    config_file: Optional[str] = Field(description=
        'The path of changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.'
        )
    date: Optional[datetime] = Field(description=
        'The date and time of the release. Uses ISO 8601 format. Defaults to the current time.'
        )
    from_: Optional[str] = Field(alias='from', description=
        'The start of the range of commits (as a SHA) to use for generating the changelog. This commit itself isn’t included in the list.'
        )
    to: Optional[str] = Field(description=
        'The end of the range of commits (as a SHA) to use for the changelog. This commit is included in the list. Defaults to the HEAD of the default project branch.'
        )
    trailer: Optional[str] = Field(description=
        'The Git trailer to use for including commits. Defaults to Changelog.')

# Classes from file: deployments.py
class ListProjectDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class GetASpecificDeployment(BaseModel):
    id: int
    deployment_id: int
class GetDeploymentFrequency(BaseModel):
    id: int
    finished_after: Optional[datetime] = None
class DeploymentDuration(BaseModel):
    created_at: datetime
    finished_at: datetime
class ListProjectDeployment(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsCreate(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeployments(BaseModel):
    id: int
    order_by: Optional[str] = None
    sort: Optional[str] = None
    updated_after: Optional[datetime] = None
    updated_before: Optional[datetime] = None
    finished_after: Optional[datetime] = None
    finished_before: Optional[datetime] = None
    environment: Optional[str] = None
    status: Optional[str] = None
class ProjectsIdDeploymentsDeploymentid(BaseModel):
    id: int
    deployment_id: int
class CreateADeployment(BaseModel):
    id: int
    environment: str
    sha: str
    ref: str
    tag: bool
    status: str
class ProjectsIdDeploymentsDeploymentidUpdate(BaseModel):
    id: int
    deployment_id: int
    status: str
class ProjectsIdDeploymentsDeploymentidDelete(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidMergerequests(BaseModel):
    id: int
    deployment_id: int
class ProjectsIdDeploymentsDeploymentidApproval(BaseModel):
    id: int
    deployment_id: int
    status: str
    comment: Optional[str] = None
    represented_as: Optional[str] = None

# Classes from file: snippet_repository_storage_moves.py

# Classes from file: notification_settings.py

# Classes from file: iterations_(group).py

# Classes from file: search.py

# Classes from file: project_aliases.py

# Classes from file: http_wrapper_privatetoken.py

# Classes from file: group_badges.py
class GroupsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class GroupsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesAdd(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class GroupsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class GroupsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class GroupsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str

# Classes from file: external_status_checks.py
class ProjectsIdExternalstatuschecks(BaseModel):
    id: Union[int, str] = Field(description='ID of a project')
class CreateUpdateExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    name: Optional[str] = Field(description=
        'Display name of external status check service')
    external_url: Optional[str] = Field(description=
        'URL of external status check service')
    protected_branch_ids: Optional[List[int]] = Field(description=
        'IDs of protected branches to scope the rule by')
class UpdateExternalStatusCheckService(BaseModel):
    id: Union[int, str]
    check_id: int
    name: Optional[str] = None
    external_url: Optional[str] = None
    protected_branch_ids: Optional[List[int]] = None
class DeleteExternalStatusCheckService(BaseModel):
    id: int = Field(description='ID of a project')
    check_id: int = Field(description='ID of an external status check service')
class MergeRequestStatusChecks(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
class SetStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    sha: str = Field(description='SHA at HEAD of the source branch')
    external_status_check_id: int = Field(description=
        'ID of an external status check')
    status: Optional[str] = Field(description=
        'Set to passed to pass the check or failed to fail it')
class RetryFailedStatusCheck(BaseModel):
    id: int = Field(description='ID of a project')
    merge_request_iid: int = Field(description='IID of a merge request')
    external_status_check_id: int = Field(description=
        'ID of a failed external status check')

# Classes from file: access_requests.py
class ProjectsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequests(BaseModel):
    id: int
class GroupsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class ProjectsIdAccessRequestsUseridApprove(BaseModel):
    id: int
    user_id: int
    access_level: Optional[int] = None
class GroupsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int
class ProjectsIdAccessRequestsUserid(BaseModel):
    id: int
    user_id: int

# Classes from file: project_templates.py

# Classes from file: sidekiq_metrics.py

# Classes from file: group_level_protected_environments.py

# Classes from file: invitations.py

# Classes from file: go_proxy.py

# Classes from file: license.py

# Classes from file: project_repository_storage_moves.py

# Classes from file: merge_trains.py

# Classes from file: vulnerabilities.py
class VulnerabilitiesId(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdConfirm(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdResolve(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdDismiss(BaseModel):
    id: Union[int, str]
class VulnerabilitiesIdRevert(BaseModel):
    id: Union[int, str]

# Classes from file: variables_group.py
class ListGroupVariables(BaseModel):
    id: Union[int, str]
class VariableType(str, Enum):
    env_var = 'env_var'
    file = 'file'
class ShowGroupVariableDetails(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
class CreateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class UpdateGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')
    value: str
    variable_type: Optional[VariableType] = None
    protected: Optional[bool] = None
    masked: Optional[bool] = None
    raw: Optional[bool] = None
    environment_scope: Optional[str] = None
    description: Optional[str] = None
class RemoveGroupVariable(BaseModel):
    id: Union[int, str]
    key: str = Field(..., max_length=255, regex='^[A-Za-z0-9_]+$')

# Classes from file: pypi.py

# Classes from file: maven.py

# Classes from file: group_access_tokens.py

# Classes from file: projects.py
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
    custom_attributes: Optional[Dict[str, str]] = Field(None, description=
        'A dictionary of custom attributes to filter by')
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
class CreateProjectRequest(BaseModel):
    name: Optional[str] = Field(None, description=
        'The name of the new project. Equals path if not provided.')
    path: Optional[str] = Field(None, description=
        'Repository name for new project. Generated based on name if not provided (generated as lowercase with dashes). Starting with GitLab 14.9, path must not start or end with a special character and must not contain consecutive special characters.'
        )
    allow_merge_on_skipped_pipeline: Optional[bool] = Field(None,
        description=
        'Set whether or not merge requests can be merged with skipped jobs.')
    only_allow_merge_if_all_status_checks_passed: Optional[bool] = Field(None,
        description=
        'Indicates that merges of merge requests should be blocked unless all status checks have passed. Defaults to false. Introduced in GitLab 15.5 with feature flag only_allow_merge_if_all_status_checks_passed disabled by default.'
        )
    analytics_access_level: Optional[str] = Field(None, description=
        'One of disabled, private or enabled.')
    approvals_before_merge: Optional[int] = Field(None, description=
        'How many approvers should approve merge requests by default. To configure approval rules, see Merge request approvals API. Deprecated in GitLab 16.0.'
        )
    auto_cancel_pending_pipelines: Optional[str] = Field(None, description=
        'Auto-cancel pending pipelines. This action toggles between an enabled state and a disabled state; it is not a boolean.'
        )
    auto_devops_deploy_strategy: Optional[str] = Field(None, description=
        'Auto Deploy strategy (continuous, manual or timed_incremental).')
    auto_devops_enabled: Optional[bool] = Field(None, description=
        'Enable Auto DevOps for this project.')
    autoclose_referenced_issues: Optional[bool] = Field(None, description=
        'Set whether auto-closing referenced issues on default branch.')
    avatar: Optional[Union[str, Any]] = Field(None, description=
        'Image file for avatar of the project.')
    build_git_strategy: Optional[str] = Field(None, description=
        'The Git strategy. Defaults to fetch.')
    build_timeout: Optional[int] = Field(None, description=
        'The maximum amount of time, in seconds, that a job can run.')
    builds_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    ci_config_path: Optional[str] = Field(None, description=
        'The path to CI configuration file.')
    container_expiration_policy_attributes: Optional[dict] = Field(None,
        description='Update the image cleanup policy for this project.')
    container_registry_access_level: Optional[str] = Field(None,
        description=
        'Set visibility of container registry, for this project, to one of disabled, private or enabled.'
        )
    container_registry_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable container registry for this project. Use container_registry_access_level instead.'
        )
    default_branch: Optional[str] = Field(None, description=
        'The default branch name. Requires initialize_with_readme to be true.')
    description: Optional[str] = Field(None, description=
        'Short project description.')
    emails_disabled: Optional[bool] = Field(None, description=
        'Disable email notifications.')
    external_authorization_classification_label: Optional[str] = Field(None,
        description='The classification label for the project.')
    forking_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    group_with_project_templates_id: Optional[int] = Field(None,
        description=
        'For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true.'
        )
    import_url: Optional[str] = Field(None, description=
        'URL to import repository from. When the URL value isn’t empty, you must not set initialize_with_readme to true. Doing so might result in the following error: not a git repository.'
        )
    initialize_with_readme: Optional[bool] = Field(None, description=
        'Whether to create a Git repository with just a README.md file. Default is false.'
        )
    issues_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    issues_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable issues for this project. Use issues_access_level instead.'
        )
    jobs_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable jobs for this project. Use builds_access_level instead.'
        )
    lfs_enabled: Optional[bool] = Field(None, description='Enable LFS.')
    merge_method: Optional[str] = Field(None, description=
        'Set the merge method used.')
    merge_pipelines_enabled: Optional[bool] = Field(None, description=
        'Enable or disable merge pipelines.')
    merge_requests_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    merge_requests_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable merge requests for this project. Use merge_requests_access_level instead.'
        )
    merge_trains_enabled: Optional[bool] = Field(None, description=
        'Enable or disable merge trains.')
    mirror_trigger_builds: Optional[bool] = Field(None, description=
        'Pull mirroring triggers builds.')
    mirror: Optional[bool] = Field(None, description=
        'Enables pull mirroring in a project.')
    namespace_id: Optional[int] = Field(None, description=
        'Namespace for the new project (defaults to the current user’s namespace).'
        )
    only_allow_merge_if_all_discussions_are_resolved: Optional[bool] = Field(
        None, description=
        'Set whether merge requests can only be merged when all the discussions are resolved.'
        )
    only_allow_merge_if_pipeline_succeeds: Optional[bool] = Field(None,
        description=
        'Set whether merge requests can only be merged with successful pipelines.'
        )
    packages_enabled: Optional[bool] = Field(None, description=
        'Enable or disable packages repository feature.')
    pages_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, enabled, or public.')
    printing_merge_request_link_enabled: Optional[bool] = Field(None,
        description=
        'Show link to create/view merge request when pushing from the command line.'
        )
    public_builds: Optional[bool] = Field(None, description=
        'If true, jobs can be viewed by non-project members.')
    releases_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    environments_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    feature_flags_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    infrastructure_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    monitor_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    remove_source_branch_after_merge: Optional[bool] = Field(None,
        description=
        'Enable Delete source branch option by default for all new merge requests.'
        )
    repository_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    repository_storage: Optional[str] = Field(None, description=
        'Which storage shard the repository is on. (administrator only)')
    request_access_enabled: Optional[bool] = Field(None, description=
        'Allow users to request member access.')
    requirements_access_level: Optional[str] = Field(None, description=
        'One of disabled, private or enabled')
    resolve_outdated_diff_discussions: Optional[bool] = Field(None,
        description=
        'Automatically resolve merge request diffs discussions on lines changed with a push.'
        )
    security_and_compliance_access_level: Optional[str] = Field(None,
        description=
        '(GitLab 14.9 and later) Security and compliance access level. One of disabled, private, or enabled.'
        )
    shared_runners_enabled: Optional[bool] = Field(None, description=
        'Enable shared runners for this project.')
    group_runners_enabled: Optional[bool] = Field(None, description=
        'Enable group runners for this project.')
    snippets_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    snippets_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable snippets for this project. Use snippets_access_level instead.'
        )
    squash_option: Optional[str] = Field(None, description=
        'One of never, always, default_on, or default_off.')
    tag_list: Optional[list] = Field(None, description=
        '(Deprecated in GitLab 14.0) The list of tags for a project; put array of tags, that should be finally assigned to a project. Use topics instead.'
        )
    template_name: Optional[str] = Field(None, description=
        'When used without use_custom_template, name of a built-in project template.'
        )
    template_project_id: Optional[int] = Field(None, description=
        'When used with use_custom_template, project ID of a custom project template.'
        )
    topics: Optional[list] = Field(None, description=
        'The list of topics for a project; put array of topics, that should be finally assigned to a project. (Introduced in GitLab 14.0.)'
        )
    use_custom_template: Optional[bool] = Field(None, description=
        'Use either custom instance or group (with group_with_project_templates_id) project template.'
        )
    visibility: Optional[str] = Field(None, description=
        'See project visibility level.')
    wiki_access_level: Optional[str] = Field(None, description=
        'One of disabled, private, or enabled.')
    wiki_enabled: Optional[bool] = Field(None, description=
        '(Deprecated) Enable wiki for this project. Use wiki_access_level instead.'
        )
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
    container_expiration_policy_attributes: Optional[
        ContainerExpirationPolicyAttributes] = None
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

# Classes from file: merge_requests.py
class ProjectsMergeRequestCreate(BaseModel):
    id: Union[int, str] = Field(description=
        'The ID or URL-encoded path of the project owned by the authenticated user.'
        )
    source_branch: str = Field(description='The source branch name.')
    target_branch: str = Field(description='The target branch name.')
    title: str = Field(description='The title of merge request.')
    allow_collaboration: Optional[bool] = Field(None, description=
        'Allow commits from members who can merge to the target branch.')
    approvals_before_merge: Optional[int] = Field(None, description=
        'The amount of approvals required before merging.')
    allow_maintainer_to_push: Optional[bool] = Field(None, description=
        'Allow users who can merge to the target branch to push to the source branch.'
        )
    assignee_id: Optional[int] = Field(None, description=
        'The ID of a user to assign merge request.')
    assignee_ids: Optional[List[int]] = Field(None, description=
        'The IDs of users to assign merge request.')
    description: Optional[str] = Field(None, description=
        'The description of merge request.')
    labels: Optional[str] = Field(None, description=
        'Comma-separated list of label names.')
    milestone_id: Optional[int] = Field(None, description=
        'The global ID of a milestone to assign merge request.')
    remove_source_branch: Optional[bool] = Field(None, description=
        'Flag indicating if a merge request should remove the source branch when merging.'
        )
    reviewer_ids: Optional[List[int]] = Field(None, description=
        'The IDs of users to request review from when merge request created.')
    squash: Optional[bool] = Field(None, description=
        'Squash commits into a single commit when merging.')
    squash_on_merge: Optional[bool] = Field(None, description=
        'Squash commits into a single commit after merging.')
    target_project_id: Optional[int] = Field(None, description=
        'The target project ID. If the user is a maintainer of the target project, the source project is set as the target_project_id.'
        )

# Classes from file: member_roles.py

# Classes from file: resource_weight_events.py

# Classes from file: search_migrations.py

# Classes from file: integrations.py

# Classes from file: emoji_reactions.py
class AwardEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
class SingleEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class NewEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    name: str
class DeleteEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: Optional[int]
    merge_request_iid: Optional[int]
    snippet_id: Optional[int]
    award_id: int
class ListCommentEmojiReactionsParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
class GetCommentEmojiReactionParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int
class AwardCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    name: str
class DeleteCommentEmojiParams(BaseModel):
    id: Union[int, str]
    issue_iid: int
    note_id: int
    award_id: int

# Classes from file: settings_(application).py

# Classes from file: pipelines.py
class Scope(str, Enum):
    running = 'running'
    pending = 'pending'
    finished = 'finished'
    branches = 'branches'
    tags = 'tags'
class Status(str, Enum):
    created = 'created'
    waiting_for_resource = 'waiting_for_resource'
    preparing = 'preparing'
    pending = 'pending'
    running = 'running'
    success = 'success'
    failed = 'failed'
    canceled = 'canceled'
    skipped = 'skipped'
    manual = 'manual'
    scheduled = 'scheduled'
class Source(str, Enum):
    push = 'push'
    web = 'web'
    trigger = 'trigger'
    schedule = 'schedule'
    api = 'api'
    external = 'external'
    pipeline = 'pipeline'
    chat = 'chat'
    webide = 'webide'
    merge_request_event = 'merge_request_event'
    external_pull_request_event = 'external_pull_request_event'
    parent_pipeline = 'parent_pipeline'
    ondemand_dast_scan = 'ondemand_dast_scan'
    ondemand_dast_validation = 'ondemand_dast_validation'
class OrderBy(str, Enum):
    id = 'id'
    status = 'status'
    ref = 'ref'
    updated_at = 'updated_at'
    user_id = 'user_id'
class Sort(str, Enum):
    asc = 'asc'
    desc = 'desc'
class ListProjectPipelinesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    scope: Optional[Scope]
    status: Optional[Status]
    source: Optional[Source]
    ref: Optional[str]
    sha: Optional[str]
    yaml_errors: Optional[bool]
    username: Optional[str]
    updated_after: Optional[datetime]
    updated_before: Optional[datetime]
    name: Optional[str]
    order_by: Optional[OrderBy]
    sort: Optional[Sort]
class GetPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineVariablesInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetPipelineTestReportSummaryInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class GetLatestPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    ref: Optional[str] = Field(None, description=
        'The branch or tag to check for the latest pipeline. Defaults to the default branch when not specified.'
        )
class CreatePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    ref: str = Field(..., description=
        'The branch or tag to run the pipeline on.')
    variables: Optional[List[Dict[str, Union[str, Dict[str, str]]]]] = Field(
        None, description=
        'An array of hashes containing the variables available in the pipeline.'
        )
class RetryJobsInPipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class CancelPipelineJobsInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')
class DeletePipelineInput(BaseModel):
    id: Union[int, str] = Field(..., description=
        'The ID or URL-encoded path of the project.')
    pipeline_id: int = Field(..., description='The ID of a pipeline.')

# Classes from file: lint_.gitlab_ci.yml.py

# Classes from file: service_data.py

# Classes from file: dependencies.py
class ProjectsIdDependencies(BaseModel):
    id: Union[int, str]
    package_manager: Optional[str] = None

# Classes from file: project_badges.py
class ProjectsIdBadges(BaseModel):
    id: Union[int, str]
    name: Optional[str] = None
class ProjectsIdBadgesBadgeid(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesCreate(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidEdit(BaseModel):
    id: Union[int, str]
    badge_id: int
    link_url: Optional[str] = None
    image_url: Optional[str] = None
    name: Optional[str] = None
class ProjectsIdBadgesBadgeidDelete(BaseModel):
    id: Union[int, str]
    badge_id: int
class ProjectsIdBadgesRender(BaseModel):
    id: Union[int, str]
    link_url: str
    image_url: str

# Classes from file: helm.py

# Classes from file: namespaces.py

# Classes from file: links_(issue).py

# Classes from file: deploy_keys.py
class Deploykeys(BaseModel):
    public: Optional[bool] = None
class ProjectsIdDeploykeys(BaseModel):
    id: int
class UsersIdorusernameProjectdeploykeys(BaseModel):
    id_or_username: str
class ProjectsIdDeploykeysKeyidSingle(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysAdd(BaseModel):
    id: int
    key: str
    title: str
    can_push: Optional[bool] = None
    expires_at: Optional[datetime] = None
class ProjectsIdDeploykeysKeyidUpdate(BaseModel):
    id: int
    can_push: Optional[bool] = None
    title: Optional[str] = None
class ProjectsIdDeploykeysKeyidDelete(BaseModel):
    id: int
    key_id: int
class ProjectsIdDeploykeysKeyidEnable(BaseModel):
    id: int
    key_id: int

# Classes from file: issue_boards_(project).py

# Classes from file: job_token_scopes.py
class GetProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
class PatchProjectCICDJobTokenAccessSettingsInput(BaseModel):
    id: Union[int, str]
    enabled: bool
class GetProjectCICDJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
class CreateNewProjectToJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int
class RemoveProjectFromJobTokenInboundAllowlistInput(BaseModel):
    id: Union[int, str]
    target_project_id: int

# Classes from file: merge_request_context_commits.py

