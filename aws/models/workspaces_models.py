from pydantic import BaseModel
from typing import List  ,Optional


class CreateWorkspaceRequest(BaseModel):

    #When working with multiple accounts, you can specify the account ID and role name to use for the action.
    account_id: Optional[str]
    role_name: Optional[str]

    directory_id: str
    user_name: str
    bundle_id: str


class CreateWorkspaceResponse(BaseModel):
    workspaces_ids: List[str]