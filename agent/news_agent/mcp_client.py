"""
MCP Client for News Curator Agent using Strands Framework
"""

from mcp.client.streamable_http import streamablehttp_client
from strands.tools.mcp.mcp_client import MCPClient

def create_streamable_http_transport():
    """Creates streamable HTTP transport for MCP server connection"""
    return streamablehttp_client("http://localhost:8000/mcp/")

# Initialize global MCP client using Strands framework
STREAMABLE_HTTP_MCP_CLIENT = MCPClient(create_streamable_http_transport)

# AI model configuration
STANDARD_MODEL = "arn:aws:bedrock:eu-central-1:998978876161:inference-profile/eu.anthropic.claude-sonnet-4-20250514-v1:0"
