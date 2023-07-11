from . import action_store


def get_secrets():
    host = action_store.secrets.get("GITLAB_URL")
    token = action_store.secrets.get("GITLAB_TOKEN")
    return host, token
