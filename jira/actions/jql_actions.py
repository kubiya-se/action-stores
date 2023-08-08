from ..models.jql import RunJQLParams, RunJQLResponse
from .jira_wrapper import get_jira_instance
from .issue_actions import get_jira_url
from .. import action_store as action_store

@action_store.kubiya_action()
def run_jql(request: RunJQLParams) -> RunJQLResponse:
    """
    Runs a JQL query and returns the issues
    """
    jira = get_jira_instance()
    raw_response = jira.jql(request.jql_query)
    raw_issues = raw_response['issues']

    # Limit the issues to max_results
    raw_issues = raw_issues[:request.max_results]

    # Only select the fields that the user specified and generate the web URL
    issues = [{**{field.value: issue.get(field.value) for field in request.fields_selection.fields}, "url": get_jira_url(issue.get('key'), jira)} for issue in raw_issues]

    return RunJQLResponse(issues=issues)