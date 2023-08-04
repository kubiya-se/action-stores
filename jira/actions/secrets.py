from . import action_store

def get_jira_secrets():
    url = action_store.secrets.get("JIRA_URL")
    username = action_store.secrets.get("JIRA_USERNAME")
    password = action_store.secrets.get("JIRA_PASSWORD")
    return url, username, password