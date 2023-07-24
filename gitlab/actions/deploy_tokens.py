#Todo

# from typing import List, Any, Optional, Union
# from pydantic import BaseModel, Field
# from . import action_store as action_store
# from ..http_wrapper import *
# from datetime import datetime
#
#
#
#
# class Deploytokens(BaseModel):
#
#
# @action_store.kubiya_action()
# def list_all_deploy_tokens_(input: Deploytokens):
#     return get_wrapper(endpoint=f"/deploy_tokens", args=input.dict(exclude_none=True))
#
#
# class ProjectsIdDeploytokens(BaseModel):
#
#
# @action_store.kubiya_action()
# def project_deploy_tokens(input: ProjectsIdDeploytokens):
#     return get_wrapper(endpoint=f"/projects/{input.id}/deploy_tokens", args=input.dict(exclude_none=True))
#
#
# class ProjectsIdDeploytokensTokenid(BaseModel):
#
#
# @action_store.kubiya_action()
# def project_deploy_tokens(input: ProjectsIdDeploytokensTokenid):
#     return get_wrapper(endpoint=f"/projects/{input.id}/deploy_tokens/{input.token_id}", args=input.dict(exclude_none=True))
#
#
# class ProjectsIdDeploytokens(BaseModel):
#
#
# @action_store.kubiya_action()
# def project_deploy_tokens(input: ProjectsIdDeploytokens):
#     return post_wrapper(endpoint=f"/projects/{input.id}/deploy_tokens", args=input.dict(exclude_none=True))
#
#
# class ProjectsIdDeploytokensTokenid(BaseModel):
#
#
# @action_store.kubiya_action()
# def project_deploy_tokens(input: ProjectsIdDeploytokensTokenid):
#     return delete_wrapper(endpoint=f"/projects/{input.id}/deploy_tokens/{input.token_id}", args=input.dict(exclude_none=True))
#
#
# class GroupsIdDeploytokens(BaseModel):
#
#
# @action_store.kubiya_action()
# def group_deploy_tokens(input: GroupsIdDeploytokens):
#     return get_wrapper(endpoint=f"/groups/{input.id}/deploy_tokens", args=input.dict(exclude_none=True))
#
#
# class GroupsIdDeploytokensTokenid(BaseModel):
#
#
# @action_store.kubiya_action()
# def group_deploy_tokens(input: GroupsIdDeploytokensTokenid):
#     return get_wrapper(endpoint=f"/groups/{input.id}/deploy_tokens/{input.token_id}", args=input.dict(exclude_none=True))
#
#
# class GroupsIdDeploytokens(BaseModel):
#
#
# @action_store.kubiya_action()
# def group_deploy_tokens(input: GroupsIdDeploytokens):
#     return post_wrapper(endpoint=f"/groups/{input.id}/deploy_tokens", args=input.dict(exclude_none=True))
#
#
# class GroupsIdDeploytokensTokenid(BaseModel):
#
#
# @action_store.kubiya_action()
# def group_deploy_tokens(input: GroupsIdDeploytokensTokenid):
#     return delete_wrapper(endpoint=f"/groups/{input.id}/deploy_tokens/{input.token_id}", args=input.dict(exclude_none=True))
#
