from mcp.client.streamable_http import streamablehttp_client
from strands.tools.mcp.mcp_client import MCPClient

def create_streamable_http_transport():
   return streamablehttp_client("http://localhost:8000/mcp/")

STREAMABLE_HTTP_MCP_CLIENT = MCPClient(create_streamable_http_transport)

STANDARD_MODEL = "arn:aws:bedrock:eu-central-1:998978876161:inference-profile/eu.anthropic.claude-sonnet-4-20250514-v1:0"