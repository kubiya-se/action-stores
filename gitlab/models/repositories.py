from typing import List, Any, Optional, Union, Dict, Union
from pydantic import BaseModel, Field
from datetime import datetime

class ListDict(BaseModel):
    response: List[dict]

class SingleDict(BaseModel):
    response: dict

class ProjectStatInput(BaseModel):
    id: Union[int,str]

class Repository(BaseModel):
    id: Optional[str]
    name: Optional[str]
    type: Optional[str]
    path: Optional[str]
    mode: Optional[str]

class Commit(BaseModel):
    id: str
    short_id: str
    title: str
    author_name: str
    author_email: str
    created_at: str

class Diff(BaseModel):
    old_path: str
    new_path: str
    a_mode: Optional[str] = None
    b_mode: str
    diff: str
    new_file: bool
    renamed_file: bool
    deleted_file: bool

class Compare(BaseModel):
    commit: Commit
    commits: List[Commit]
    diffs: List[Diff]
    compare_timeout: bool
    compare_same_ref: bool
    web_url: str

class User(BaseModel):
    name: str
    email: str
    commits: int
    additions: int
    deletions: int

class Users(BaseModel):
    users: List[User]


class MergeBase(BaseModel):
    id: str
    short_id: str
    title: str
    created_at: str
    parent_ids: List[str]
    message: str
    author_name: str
    author_email: str
    authored_date: str
    committer_name: str
    committer_email: str
    committed_date: str

class ProjectsIdRepositoryTree(BaseModel):
    id: int
    page_token: Optional[str] = None
    pagination: Optional[str] = None
    path: Optional[str] = None
    per_page: Optional[str] = None
    recursive: bool = Field(False)
    ref: Optional[str] = None
class ProjectsIdRepositoryBlobsSha(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user')
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryBlobsShaRaw(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user')
    sha: str = Field(description='The blob SHA')
class ProjectsIdRepositoryArchive(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    path: Optional[str] = Field(None, description='The subpath of the repository to download. Defaults to the whole repository.')
    sha: Optional[str] = Field(None, description='The commit SHA to download. A tag, branch reference, or SHA can be used. Defaults to the tip of the default branch.')
    format: Optional[str] = Field(None, description="The archive format. Options are: 'bz2', 'tar', 'tar.bz2', 'tar.gz', 'tb2', 'tbz', 'tbz2', 'zip'. Defaults to 'tar.gz'.")
class ProjectsIdRepositoryCompare(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    from_commit_or_branch: str = Field(..., alias='from', description='The commit SHA or branch name.')
    to: str = Field(..., description='The commit SHA or branch name.')
    from_project_id: Optional[int] = Field(None, description='The ID to compare from.')
    straight: Optional[bool] = Field(False, description='Comparison method: true for direct comparison between from and to (from..to), false to compare using merge base (from…to)’. Default is false.')
class ProjectsIdRepositoryContributors(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    order_by: Optional[str] = Field(None, description='Return contributors ordered by name, email, or commits (orders by commit date) fields. Default is commits.')
    sort: Optional[str] = Field(None, description='Return contributors sorted in asc or desc order. Default is asc.')
class ProjectsIdRepositoryMergebase(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    refs: List[str] = Field(description='The refs to find the common ancestor of. Accepts multiple refs.')
class ProjectsIdRepositoryChangelog(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    version: str = Field(description='The version to generate the changelog for. The format must follow semantic versioning.')
    branch: Optional[str] = Field(None, description='The branch to commit the changelog changes to. Defaults to the project’s default branch.')
    config_file: Optional[str] = Field(None, description='Path to the changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.')
    date: Optional[datetime] = Field(None, description='The date and time of the release. Defaults to the current time.')
    file: Optional[str] = Field(None, description='The file to commit the changes to. Defaults to CHANGELOG.md.')
    from_: Optional[str] = Field(None, alias='from', description='The SHA of the commit that marks the beginning of the range of commits to include in the changelog. This commit isn’t included in the changelog.')
    message: Optional[str] = Field(None, description='The commit message to use when committing the changes. Defaults to Add changelog for version X, where X is the value of the version argument.')
    to: Optional[str] = Field(None, description='The SHA of the commit that marks the end of the range of commits to include in the changelog. This commit is included in the changelog. Defaults to the branch specified in the branch attribute. Limited to 15000 commits unless the feature flag changelog_commits_limitation is disabled.')
    trailer: Optional[str] = Field(None, description='The Git trailer to use for including commits. Defaults to Changelog. Case-sensitive: Example does not match example or eXaMpLE.')
class GenerateChangelogData(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project.')
    version: str = Field(description='The version to generate the changelog for. The format must follow semantic versioning.')
    config_file: Optional[str] = Field(description='The path of changelog configuration file in the project’s Git repository. Defaults to .gitlab/changelog_config.yml.')
    date: Optional[datetime] = Field(description='The date and time of the release. Uses ISO 8601 format. Defaults to the current time.')
    from_: Optional[str] = Field(alias='from', description='The start of the range of commits (as a SHA) to use for generating the changelog. This commit itself isn’t included in the list.')
    to: Optional[str] = Field(description='The end of the range of commits (as a SHA) to use for the changelog. This commit is included in the list. Defaults to the HEAD of the default project branch.')
    trailer: Optional[str] = Field(description='The Git trailer to use for including commits. Defaults to Changelog.')