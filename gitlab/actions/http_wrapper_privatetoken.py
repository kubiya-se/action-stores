import requests
from typing import Dict, Any, Optional
from .secrets import get_secrets


def request_wrapper(method: str, endpoint: str, args: Optional[Dict[str, Any]] = None):
    host, token = get_secrets()
    headers = {"PRIVATE-TOKEN": "<personal_access_token>", "Content-Type": "application/json"}

    # Dispatch to the appropriate requests function based on the method
    requests_func = getattr(requests, method.lower())

    ret = requests_func(f"{host}{endpoint}", headers=headers, json=args if method.lower() != 'get' else None, params=args if method.lower() == 'get' else None)

    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")

    if ret.headers.get("Content-Type", "").startswith("application/json"):
        return ret.json()
    else:
        return ret.text

def get_wrapper(endpoint: str, args: Optional[Dict[str, Any]] = None):
    return request_wrapper("GET", endpoint, args)

def post_wrapper(endpoint: str, args: Optional[Dict[str, Any]] = None):
    return request_wrapper("POST", endpoint, args)

def put_wrapper(endpoint: str, args: Optional[Dict[str, Any]] = None):
    return request_wrapper("PUT", endpoint, args)

def delete_wrapper(endpoint: str, args: Optional[Dict[str, Any]] = None):
    return request_wrapper("DELETE", endpoint, args)

def patch_wrapper(endpoint: str, args: Optional[Dict[str, Any]] = None):
    return request_wrapper("PATCH", endpoint, args)
