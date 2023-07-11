
from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime



class ProjectsIdDependencies(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.
    package_manager: Optional[str] = None # Returns dependencies belonging to specified package manager. Valid values: bundler, composer, conan, go, gradle, maven, npm, nuget, pip, pipenv, pnpm, yarn, sbt, or setuptools.


@action_store.kubiya_action()
def list_project_dependencies(input: ProjectsIdDependencies):
    return get_wrapper(endpoint=f"/projects/{input.id}/dependencies", args=input.dict(exclude_none=True))


