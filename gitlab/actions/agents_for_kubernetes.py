from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from .http_wrapper import *
from datetime import datetime

class ListTheAgentsForAProject(BaseModel):
    id: Union[int, str] = Field(description = "ID or URL-encoded path of the project maintained by the authenticated user")

@action_store.kubiya_action()
def list_the_agents_for_a_project(input: ListTheAgentsForAProject):
    return get_wrapper(endpoint=f"/projects/{input.id}/cluster_agents", args=input.dict(exclude_none=True))

#Get details about an agent
class GetDetailsAboutAnAgent(BaseModel):
    id: Union[int, str] = Field(description = "ID or URL-encoded path of the project maintained by the authenticated user")
    agent_id: int = Field(description = "ID of the agent")

@action_store.kubiya_action()
def get_details_about_an_agent(input: GetDetailsAboutAnAgent):
    return get_wrapper(endpoint=f"/projects/{input.id}/cluster_agents/{input.agent_id}", args=input.dict(exclude_none=True))


class RegisterAnAgentWithAProject(BaseModel):
    id: Union[int, str] = Field(description = "ID or URL-encoded path of the project maintained by the authenticated user")
    name: str = Field(description = "Name for the agent")

@action_store.kubiya_action()
def register_an_agent_with_a_project(input: RegisterAnAgentWithAProject):
    return post_wrapper(endpoint=f"/projects/{input.id}/cluster_agents", args=input.dict(exclude_none=True))


class DeleteARegisteredAgent(BaseModel):
    id: Union[int, str] = Field(description = "ID or URL-encoded path of the project maintained by the authenticated user")
    agent_id: int = Field(description = "ID of the agent")

@action_store.kubiya_action()
def delete_a_registered_agent(input: DeleteARegisteredAgent):
    return delete_wrapper(endpoint=f"/projects/{input.id}/cluster_agents/{input.agent_id}", args=input.dict(exclude_none=True))


class ListTokensForAnAgent(BaseModel):
    id: Union[int, str] = Field(description = "ID or URL-encoded path of the project maintained by the authenticated user")
    agent_id: int = Field(description = "ID of the agent")

@action_store.kubiya_action()
def list_tokens_for_an_agent(input: ListTokensForAnAgent):
    return get_wrapper(endpoint=f"/projects/{input.id}/cluster_agents/{input.agent_id}/tokens", args=input.dict(exclude_none=True))


class GetSingleAgentToken(BaseModel):
    id: Union[int, str] = Field(description = "ID or URL-encoded path of the project maintained by the authenticated user")
    agent_id: int = Field(description = "ID of the agent")
    token_id: int = Field(description = "ID of the token")


@action_store.kubiya_action()
def get_a_single_agent_token(input: GetSingleAgentToken):
    return get_wrapper(endpoint=f"/projects/{input.id}/cluster_agents/{input.agent_id}/tokens/{input.token_id}", args=input.dict(exclude_none=True))


class CreateAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description = "ID or URL-encoded path of the project maintained by the authenticated user")
    agent_id: int = Field(description = "ID of the agent")
    name: int = Field(description = "Name for the token")
    description: Optional[int] = Field(None, description = "Description for the token")

@action_store.kubiya_action()
def create_an_agent_token(input: CreateAnAgentToken):
    return post_wrapper(endpoint=f"/projects/{input.id}/cluster_agents/{input.agent_id}/tokens", args=input.dict(exclude_none=True))


class RevokeAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description = "ID or URL-encoded path of the project maintained by the authenticated user")
    agent_id: int = Field(description = "ID of the agent")
    token_id: int = Field(description = "ID of the token")

@action_store.kubiya_action()
def revoke_an_agent_token(input: RevokeAnAgentToken):
    return delete_wrapper(endpoint=f"/projects/{input.id}/cluster_agents/{input.agent_id}/tokens/{input.token_id}", args=input.dict(exclude_none=True))