from typing import List, Any, Optional, Union, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime


class ProjectIdRepositoryFiles(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user")
    file_path: str = Field(description="URL encoded full path to new file")
    ref: str = Field(description="The name of branch, tag or commit")

@action_store.kubiya_action()
def get_file_from_repository(input: ProjectIdRepositoryFiles):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/files/{input.file_path}", args=input.dict(exclude_none=True))

class ProjectIdRepositoryFilesBlame(BaseModel):
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user.")
    file_path: str = Field(description="URL-encoded full path to new file, such as lib%2Fclass%2Erb.")
    ref: str = Field(description="The name of branch, tag or commit.")
    range_start: int = Field(description="The first line of the range to blame.")
    range_end: int = Field(description="The last line of the range to blame.")
    range: Optional[dict] = Field(description="Blame range.")

@action_store.kubiya_action()
def get_file_blame_from_repository(input: ProjectIdRepositoryFilesBlame):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/files/{input.file_path}/blame", args=input.dict(exclude_none=True))



class ProjectsIdRepositoryFilesFilepathRaw(BaseModel):
  id: Union[int, str] = Field(..., description="The ID or URL-encoded path of the project owned by the authenticated user.")
  file_path: str = Field(..., description="URL-encoded full path to new file, such as lib%2Fclass%2Erb.")
  ref: str = Field(..., description="The name of branch, tag or commit. Default is the HEAD of the project.")
  lfs: Optional[bool] = Field(None, description="Determines if the response should be Git LFS file contents, rather than the pointer. If the file is not tracked by Git LFS, ignored. Defaults to false.")

@action_store.kubiya_action()
def get_raw_file_from_repository(input: ProjectsIdRepositoryFilesFilepathRaw):
    return get_wrapper(endpoint=f"/projects/{input.id}/repository/files/{input.file_path}/raw", args=input.dict(exclude_none=True))


class ProjectsIdRepositoryFilesFilepathCreate(BaseModel):
    branch: str = Field(description="Name of the new branch to create. The commit is added to this branch.")
    commit_message: str = Field(description="The commit message.")
    content: str = Field(description="The file’s content.")
    file_path: str = Field(description="URL-encoded full path to new file. For example: lib%2Fclass%2Erb.")
    id: Union[int, str] = Field(description="The ID or URL-encoded path of the project owned by the authenticated user.")
    author_email: Optional[str] = Field(None, description="The commit author’s email address.")
    author_name: Optional[str] = Field(None, description="The commit author’s name.")
    encoding: Optional[str] = Field(None, description="Change encoding to base64. Default is text.")
    execute_filemode: Optional[bool] = Field(None, description="Enables or disables the execute flag on the file. Can be true or false.")
    #start_branch: Optional[str] = Field(None, description="Name of the base branch to create the new branch from.")
    start_branch: str = Field(None, description="Name of the base branch to create the new branch from.")


@action_store.kubiya_action()
def create_new_file_in_repository(input: ProjectsIdRepositoryFilesFilepathCreate):
    return post_wrapper(endpoint=f"/projects/{input.id}/repository/files/{input.file_path}", args=input.dict(exclude_none=True))


class ProjectsIdRepositoryFilesFilepathUpdate(BaseModel):

    branch: str # Name of the new branch to create. The commit is added to this branch.

    commit_message: str # The commit message.

    content: str # The file’s content.

    file_path: str # URL-encoded full path to new file. For example: lib%2Fclass%2Erb.

    id: Union[int, str]  # The ID or URL-encoded path of the project owned by the authenticated user

    author_email: Optional[str] = None # The commit author’s email address.

    author_name: Optional[str] = None # The commit author’s name.

    encoding: Optional[str] = None # Change encoding to base64. Default is text.

    execute_filemode: Optional[bool] = None # Enables or disables the execute flag on the file. Can be true or false.

    last_commit_id: Optional[str] = None # Last known file commit ID.

    #start_branch: Optional[str] = None # Name of the base branch to create the new branch from.
    start_branch: str = Field(None, description="Name of the base branch to create the new branch from.")


@action_store.kubiya_action()
def update_existing_file_in_repository(input: ProjectsIdRepositoryFilesFilepathUpdate):
    return put_wrapper(endpoint=f"/projects/{input.id}/repository/files/{input.file_path}", args=input.dict(exclude_none=True))


class ProjectsIdRepositoryFilesFilepathDelete(BaseModel):

    branch: str # Name of the new branch to create. The commit is added to this branch.

    commit_message: str # The commit message.

    file_path: str # URL-encoded full path to new file. For example: lib%2Fclass%2Erb.

    id: int # The ID or URL-encoded path of the project owned by the authenticated user.

    author_email: Optional[str] = None # The commit author’s email address.

    author_name: Optional[str] = None # The commit author’s name.

    last_commit_id: Optional[str] = None # Last known file commit ID.

    #start_branch: Optional[str] = None # Name of the base branch to create the new branch from.
    start_branch: str = Field(None, description="Name of the base branch to create the new branch from.")


@action_store.kubiya_action()
def delete_existing_file_in_repository(input: ProjectsIdRepositoryFilesFilepathDelete):
    return delete_wrapper(endpoint=f"/projects/{input.id}/repository/files/{input.file_path}", args=input.dict(exclude_none=True))


class ProjectsIdRepositorySubmodulesSubmodule(BaseModel):

    id: int # The ID or URL-encoded path of the project owned by the authenticated user

    submodule: str # URL-encoded full path to the submodule. For example, lib%2Fclass%2Erb

    branch: str # Name of the branch to commit into

    commit_sha: str # Full commit SHA to update the submodule to

    commit_message: Optional[str] = None # Commit message. If no message is provided, a default is set
