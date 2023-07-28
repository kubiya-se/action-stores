from typing import List, Any, Optional, Union
from pydantic import BaseModel, Field
from ..action_store_init import action_store as action_store
from datetime import datetime

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def graphql_wrapper(query: str, endpoint: str = "https://gitlab.example.com/graphql", headers: dict = None):
    """
    Execute a GraphQL query.
    
    Arguments:
        query (str): The GraphQL query to execute.
        endpoint (str, optional): The URL of the GraphQL API.
        headers (dict, optional): Any additional headers the request needs.
    """
    # Define the transport
    transport = RequestsHTTPTransport(
        url=endpoint,
        headers=headers,
        use_json=True,
    )
    # Initialize the client
    client = Client(
        transport=transport,
        fetch_schema_from_transport=True,
    )

    # Parse and execute the query
    query = gql(query)
    result = client.execute(query)

    return result


class VulnerabilityQueryInput(BaseModel):
    id: str  # The ID of the vulnerability to query.

@action_store.kubiya_action()
def query_vulnerability(input: VulnerabilityQueryInput):
    query = f"""
    {{
        vulnerability(id: "{input.id}") {{
            title
            description
            state
            severity
            reportType
            project {{
                id
                name
                fullPath
            }}
            detectedAt
            confirmedAt
            resolvedAt
            resolvedBy {{
                id
                username
            }}
        }}
    }}
    """
    # replace the URL and headers as per your requirement
    return graphql_wrapper(query, "https://gitlab.example.com/graphql", {"Authorization": "Bearer <authenticate_token>"})
