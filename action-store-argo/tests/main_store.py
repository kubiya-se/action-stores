from typing import List, Any, Dict
import requests
from kubiya import ActionStore
import os
from requests_wrapper import *

action_store.uses_secrets(["ARGO_TOKEN"])
action_store = ActionStore("argo", version="0.0.3")

@action_store.kubiya_action()
def get_accounts(_:Any=None) -> List:
    return get_wrapper("/account")

@action_store.kubiya_action()
def get_all_apps(_:Any=None) -> List:
    return get_wrapper("/applications")

# Sync an application
@action_store.kubiya_action()
def sync_app(params: Dict) -> str:
    app_name = params.pop("app_name")
    return post_wrapper(f"/applications/{app_name}/sync", args=params)


@action_store.kubiya_action()
def restart_service(params:dict):
    # Argo CD API endpoint for restarting an application
    endpoint = f"{ARGO_SERVER}/api/v1/applications/{params['application_name']}/sync"
    ARGO_SERVER = get_server()

    token = get_token()
    # Set the headers with the authentication token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Send a POST request to the Argo CD API to trigger a sync
    response = requests.post(endpoint, headers=headers)

    # Check if the request was successful
    if response.ok:
        print(f"Successfully triggered a sync for application '{params['application_name']}'.")
    else:
        print(f"Failed to restart the service. Error: {response.text}")

# Promote an application
@action_store.kubiya_action()
def promote_app(params: Dict) -> str:
    app_name = params.pop("app_name")
    return post_wrapper(f"/applications/{app_name}/promote", args=params)

# Rollback an application
@action_store.kubiya_action()
def rollback_app(params: Dict) -> str:
    app_name = params.pop("app_name")
    appNamespace = params.pop("appNamespace")
    payload = {
        "appNamespace": f"{appNamespace}"
    }
    return post_wrapper(f"/applications/{app_name}/rollback", args=params, payload=payload)

# Create an application
@action_store.kubiya_action()
def create_app(params: Dict) -> str:
    app_name = params.pop("app_name")
    return post_wrapper("/applications", args=params)

# Delete an application
@action_store.kubiya_action()
def delete_app(params: Dict) -> str:
    app_name = params.pop("app_name")
    token = get_token()
    ARGO_SERVER = get_server()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    response = requests.delete(f"{ARGO_SERVER}/api/v1/applications/{app_name}", headers=headers, verify=False)
    response.raise_for_status()
    return response.text

# Create a project
@action_store.kubiya_action()
def create_project(params: Dict) -> str:
    project_name = params.pop("project_name")

    payload = {
        "project": {
            "metadata": {"name": f"{project_name}", "finalizers": ["resources-finalizer.argocd.argoproj.io"]},
            "spec": {},
            "status": {}
        },
        "upsert": True
    }

    return post_wrapper(f"/projects", args=payload)

# Delete a project
@action_store.kubiya_action()
def delete_project(params: Dict) -> str:
    project_name = params.pop("project_name")
    token = get_token()
    ARGO_SERVER = get_server()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    return requests.delete(f"{ARGO_SERVER}/api/v1/projects/{project_name}")

# Get all projects
@action_store.kubiya_action()
def get_all_projects(_:Any=None) -> List:
    return get_wrapper("/projects")


