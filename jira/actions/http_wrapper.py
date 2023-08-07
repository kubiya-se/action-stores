import requests
from .secrets import get_jira_secrets
import logging
import json

logging.basicConfig(level=logging.INFO)


def get_wrapper(path: str, args: dict = None):
    url, username, password = get_jira_secrets()
    ret = requests.get(f"{url}{path}", auth = (username, password), data=json.dumps(args))
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type","").startswith("application/json"):
        return ret.json()
    else:
        return ret.text
    
def post_wrapper(endpoint: str, args: dict=None):
    url, username, password = get_jira_secrets()
    ret = requests.post(f"{url}{endpoint}", auth=(username, password), data=json.dumps(args))
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type","").startswith("application/json"):
        return ret.json()
    else:
        return ret.text

def patch_wrapper(endpoint: str, args: dict=None):
    url, username, password = get_jira_secrets()
    ret = requests.patch(f"{url}{endpoint}", auth=(username, password), data=json.dumps(args))
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type","").startswith("application/json"):
        return ret.json()
    else:
        return ret.text
    
def delete_wrapper(path: str, args: dict=None):
    url, username, password = get_jira_secrets()
    ret = requests.delete(f"{url}{path}", auth = (username, password), data=json.dumps(args))
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type","").startswith("application/json"):
        return ret.json()
    else:
        return ret.text
    
def put_wrapper(endpoint: str, args: dict=None):
    url, username, password = get_jira_secrets()
    ret = requests.put(f"{url}{endpoint}", auth=(username, password), data=json.dumps(args))
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type","").startswith("application/json"):
        return ret.json()
    else:
        return ret.text