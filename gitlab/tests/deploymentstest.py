from typing import List, Any, Optional, Union, Dict
from pydantic import BaseModel, Field
import requests

from datetime import datetime


class ProjectsIdDeployments(BaseModel):
    id: Union[int,str]  # The ID or URL-encoded path of the project owned by the authenticated user.
    order_by: Optional[str] = None  # Return deployments ordered by either one of id, iid, created_at, updated_at, finished_at or ref fields. Default is id.
    sort: Optional[str] = None  # Return deployments sorted in asc or desc order. Default is asc.
    updated_after: Optional[datetime] = None #Field(None, example="2019-03-15T08:00:00Z")  # Return deployments updated after the specified date. Expected in ISO 8601 format.
    updated_before: Optional[datetime] = None #Field(None, example="2019-03-15T08:00:00Z")  # Return deployments updated before the specified date. Expected in ISO 8601 format.
    finished_after: Optional[datetime] = None #Field(None, example="2019-03-15T08:00:00Z")  # Return deployments finished after the specified date. Expected in ISO 8601 format.
    finished_before: Optional[datetime] = None #Field(None, example="2019-03-15T08:00:00Z")  # Return deployments finished before the specified date. Expected in ISO 8601 format.
    environment: Optional[str] = None  # The name of the environment to filter deployments by.
    status: Optional[str] = None


def list_project_deployments(input: ProjectsIdDeployments):
    print(input.dict(exclude_none = True))
    return get_wrapper(endpoint=f"/projects/{input.id}/deployments", args=input.dict(exclude_none=True))


# when do we use gitlab.com/api/v4 vs. gitlab.com/api/v4/kubiya-test?


def get_wrapper(endpoint: str, args: Optional[Dict[str, Any]] = None):
    host, token = ("https://gitlab.com/api/v4", "glpat-dvvCyJ_H7Gs-jaUCMHjx")

    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json", }
    ret = requests.get(f"{host}{endpoint}", headers=headers, params=args)

    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type", "").startswith("application/json"):
        return ret.json()
    else:
        return ret.text

def get_wrapper2(endpoint: str, args: Optional[Dict[str, Any]] = None):
    host, token = ("https://gitlab.com/api/v4", "glpat-dvvCyJ_H7Gs-jaUCMHjx")

    headers = {"PRIVATE-TOKEN": f"{token}", "Content-Type": "application/json", }
    ret = requests.get(f"{host}{endpoint}", headers=headers, params=args)

    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type", "").startswith("application/json"):
        return ret.json()
    else:
        return ret.text

testinput = ProjectsIdDeployments(id = 47216062)

print(testinput.dict(exclude_none = True))
print(get_wrapper(endpoint=f"/projects/{testinput.id}/deployments", args=testinput.dict(exclude_none=True)))
