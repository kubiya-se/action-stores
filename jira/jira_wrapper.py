from atlassian import Jira
from .actions.secrets import get_jira_secrets


def get_jira_instance() -> Jira:
    url, username, password = get_jira_secrets()
    return Jira(url=url, username=username, password=password, cloud=True)