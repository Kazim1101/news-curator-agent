import os
from fastmcp import FastMCP
from tools import register_all_tools

from starlette.requests import Request
from starlette.responses import JSONResponse

mcp = FastMCP("AI news curator")

# Register all tools from the tools module
register_all_tools(mcp)

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request):
    return JSONResponse({"status": "healthy"})


if __name__ == "__main__":

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    # path of the MCP server add in the client
    path = os.environ.get("MCP_PATH", "/mcp")
    transport = os.environ.get("MCP_TRANSPORT", "http")
    mcp.run(transport=transport, host=host, port=port, path=path)
