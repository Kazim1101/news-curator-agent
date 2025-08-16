"""
Tools module for MCP server.

This module provides a centralized registry for all tools that can be easily extended.
Each tool module should implement a `register_tools(mcp_instance)` function.
"""

from typing import Any
from . import news_fetcher
from . import example_tool

def register_all_tools(mcp_instance: Any) -> None:
    """
    Register all tools with the MCP instance.

    This function imports and registers all available tools.
    To add a new tool module:
    1. Create a new tool file in the tools/ directory
    2. Implement a register_tools(mcp_instance) function in that file
    3. Import the module and call its register_tools function here

    Args:
        mcp_instance: The FastMCP instance to register tools with
    """
    # Register news fetcher tools
    news_fetcher.register_tools(mcp_instance)

    # Register example tools (demonstrates extensibility)
    example_tool.register_tools(mcp_instance)

    # Add more tool registrations here as needed
    # Example:
    # from . import another_tool
    # another_tool.register_tools(mcp_instance)
