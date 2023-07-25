import requests
from .secrets import get_secrets
import logging
import json

logging.basicConfig(level=logging.INFO)

url, username, password = get_secrets()
def get_wrapper(path: str, args: dict = None):
    ret = requests.get(f"{url}{path}", auth = (username, password), data=json.dumps(args))
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type","").startswith("application/json"):
        return ret.json()
    else:
        return ret.text
    
def post_wrapper(endpoint: str, args: dict=None):
    ret = requests.post(f"{url}{endpoint}", auth=(username, password), data=json.dumps(args))
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type","").startswith("application/json"):
        return ret.json()
    else:
        return ret.text

def patch_wrapper(endpoint: str, args: dict=None):
    ret = requests.patch(f"{url}{endpoint}", auth=(username, token), data=json.dumps(args))
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type","").startswith("application/json"):
        return ret.json()
    else:
        return ret.text
    
def delete_wrapper(path: str, args: dict=None):
    ret = requests.delete(f"{url}{path}", auth = (username, token), data=json.dumps(args))
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type","").startswith("application/json"):
        return ret.json()
    else:
        return ret.text
    
def put_wrapper(endpoint: str, args: dict=None):
    ret = requests.put(f"{url}{endpoint}", auth=(username, token), data=json.dumps(args))
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type","").startswith("application/json"):
        return ret.json()
    else:
        return ret.text