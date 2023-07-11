from typing import List, Any, Optional, Union, Dict
from pydantic import BaseModel, Field
from datetime import datetime
import requests

class ProjectsIdUsers(BaseModel):

    id: Union[int, str] # The ID or URL-encoded path of the project.

    search: Optional[str] = None # Search for specific users.

    skip_users: Optional[int] = None # Filter out users with the specified IDs.


def get_project_users(input: ProjectsIdUsers):
    return get_wrapper(endpoint=f"/projects/{input.id}/users", args=input.dict(exclude_none=True))


def get_wrapper(endpoint: str, args: Optional[Dict[str, Any]] = None):
    host, token = ("https://gitlab.com/api/v4/", "glpat-dvvCyJ_H7Gs-jaUCMHjx")

    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json", }
    ret = requests.get(f"{host}{endpoint}", headers=headers, params=args)

    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type", "").startswith("application/json"):
        return ret.json()
    else:
        return ret.text

testinput = ProjectsIdUsers(id = 45134339)

print(get_wrapper(endpoint=f"/users", args=testinput.dict(exclude_none=True)))
