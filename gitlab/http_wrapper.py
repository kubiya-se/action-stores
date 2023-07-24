import requests
from typing import Dict, Any, Optional
from .secrets import get_secrets


def get_wrapper(endpoint: str, args: Optional[Dict[str, Any]] = None):
    host, token = get_secrets()

    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json", }
    ret = requests.get(f"{host}{endpoint}", headers=headers, params=args)

    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type", "").startswith("application/json"):
        return ret.json()
    else:
        return ret.text


def post_wrapper(endpoint: str, args: dict = None):
    host, token = get_secrets()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    ret = requests.post(f"{host}{endpoint}", headers=headers, json=args)
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type", "").startswith("application/json"):
        return ret.json()
    else:
        return ret.text


def put_wrapper(endpoint: str, args: dict = None):
    host, token = get_secrets()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    ret = requests.put(f"{host}{endpoint}", headers=headers, json=args)
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type", "").startswith("application/json"):
        return ret.json()
    else:
        return ret.text


def delete_wrapper(endpoint: str, args: dict = None):
    host, token = get_secrets()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    ret = requests.delete(f"{host}{endpoint}", headers=headers, json=args)
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type", "").startswith("application/json"):
        return ret.json()
    else:
        return ret.text


def patch_wrapper(endpoint: str, args: dict = None):
    host, token = get_secrets()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    ret = requests.patch(f"{host}{endpoint}", headers=headers, json=args)
    if not ret.ok:
        raise Exception(f"Error: {ret.status_code} {ret.text}")
    if ret.headers.get("Content-Type", "").startswith("application/json"):
        return ret.json()
    else:
        return ret.text