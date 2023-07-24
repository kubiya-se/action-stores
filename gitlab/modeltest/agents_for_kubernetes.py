from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from . import action_store as action_store
from ..http_wrapper import *
from datetime import datetime
class ListTheAgentsForAProject(BaseModel):
    id: Union[int, str] = Field(description='ID or URL-encoded path of the project maintained by the authenticated user')
class GetDetailsAboutAnAgent(BaseModel):
    id: Union[int, str] = Field(description='ID or URL-encoded path of the project maintained by the authenticated user')
    agent_id: int = Field(description='ID of the agent')
class RegisterAnAgentWithAProject(BaseModel):
    id: Union[int, str] = Field(description='ID or URL-encoded path of the project maintained by the authenticated user')
    name: str = Field(description='Name for the agent')
class DeleteARegisteredAgent(BaseModel):
    id: Union[int, str] = Field(description='ID or URL-encoded path of the project maintained by the authenticated user')
    agent_id: int = Field(description='ID of the agent')
class ListTokensForAnAgent(BaseModel):
    id: Union[int, str] = Field(description='ID or URL-encoded path of the project maintained by the authenticated user')
    agent_id: int = Field(description='ID of the agent')
class GetSingleAgentToken(BaseModel):
    id: Union[int, str] = Field(description='ID or URL-encoded path of the project maintained by the authenticated user')
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')
class CreateAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description='ID or URL-encoded path of the project maintained by the authenticated user')
    agent_id: int = Field(description='ID of the agent')
    name: int = Field(description='Name for the token')
    description: Optional[int] = Field(None, description='Description for the token')
class RevokeAnAgentToken(BaseModel):
    id: Union[int, str] = Field(description='ID or URL-encoded path of the project maintained by the authenticated user')
    agent_id: int = Field(description='ID of the agent')
    token_id: int = Field(description='ID of the token')