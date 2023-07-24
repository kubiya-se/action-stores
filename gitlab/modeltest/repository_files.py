from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class ProjectIdRepositoryFiles(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user')
    file_path: str = Field(description='URL encoded full path to new file')
    ref: str = Field(description='The name of branch, tag or commit')
class ProjectIdRepositoryFilesBlame(BaseModel):
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    file_path: str = Field(description='URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(description='The name of branch, tag or commit.')
    range_start: int = Field(description='The first line of the range to blame.')
    range_end: int = Field(description='The last line of the range to blame.')
    range: Optional[dict] = Field(description='Blame range.')
class ProjectsIdRepositoryFilesFilepathRaw(BaseModel):
    id: Union[int, str] = Field(..., description='The ID or URL-encoded path of the project owned by the authenticated user.')
    file_path: str = Field(..., description='URL-encoded full path to new file, such as lib%2Fclass%2Erb.')
    ref: str = Field(..., description='The name of branch, tag or commit. Default is the HEAD of the project.')
    lfs: Optional[bool] = Field(None, description='Determines if the response should be Git LFS file contents, rather than the pointer. If the file is not tracked by Git LFS, ignored. Defaults to false.')
class ProjectsIdRepositoryFilesFilepathCreate(BaseModel):
    branch: str = Field(description='Name of the new branch to create. The commit is added to this branch.')
    commit_message: str = Field(description='The commit message.')
    content: str = Field(description='The file’s content.')
    file_path: str = Field(description='URL-encoded full path to new file. For example: lib%2Fclass%2Erb.')
    id: Union[int, str] = Field(description='The ID or URL-encoded path of the project owned by the authenticated user.')
    author_email: Optional[str] = Field(None, description='The commit author’s email address.')
    author_name: Optional[str] = Field(None, description='The commit author’s name.')
    encoding: Optional[str] = Field(None, description='Change encoding to base64. Default is text.')
    execute_filemode: Optional[bool] = Field(None, description='Enables or disables the execute flag on the file. Can be true or false.')
    start_branch: str = Field(None, description='Name of the base branch to create the new branch from.')
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
    start_branch: str = Field(None, description='Name of the base branch to create the new branch from.')
class ProjectsIdRepositoryFilesFilepathDelete(BaseModel):
    branch: str
    commit_message: str
    file_path: str
    id: int
    author_email: Optional[str] = None
    author_name: Optional[str] = None
    last_commit_id: Optional[str] = None
    start_branch: str = Field(None, description='Name of the base branch to create the new branch from.')
class ProjectsIdRepositorySubmodulesSubmodule(BaseModel):
    id: int
    submodule: str
    branch: str
    commit_sha: str
    commit_message: Optional[str] = None