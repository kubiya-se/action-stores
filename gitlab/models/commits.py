from typing import List, Any, Optional, Union, Dict, Union
from pydantic import BaseModel, Field
from datetime import datetime


class ListDict(BaseModel):
    response: List[dict]

class SingleDict(BaseModel):
    response: dict
    
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