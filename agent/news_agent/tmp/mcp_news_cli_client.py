from mcp.client.sse import sse_client
from strands import Agent
from strands.tools.mcp import MCPClient

# Create an MCP client for your HTTP server
mcp_client = MCPClient(lambda: sse_client("http://localhost:8000/mcp/"))
#(
#     MCPClient(
#     transport_type="sse",  # Server-Sent Events transport
#     url="http://localhost:8000/mcp/"  # Your MCP server URL
# ))

# Alternative: Direct SSE client connection
# sse_client = sse_mcp_client("http://localhost:8000/mcp/")

# Create your Strands agent
agent = Agent(
    name="NewsAgent",
    description="An agent that uses MCP tools for news curation",
    tools=[mcp_client],  # Add the MCP client as a tool
    model="claude-3-5-sonnet-20241022"  # or your preferred model
)

# Run the agent
if __name__ == "__main__":
    try:
        # Start the MCP connection
        with mcp_client:
            # Your agent logic here
            response = agent.run("What news tools are available?")
            print(response)
    except Exception as e:
        print(f"Error connecting to MCP server: {e}")
        print("Make sure your MCP server is running at http://localhost:8000/mcp/")