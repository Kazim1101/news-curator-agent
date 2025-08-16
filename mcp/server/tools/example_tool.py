"""
Example tool to demonstrate how to add new tools to the MCP server.

This is a template that shows the recommended pattern for creating new tools.
"""

from typing import Any
from datetime import datetime

def get_current_time() -> str:
    """
    Get the current timestamp.

    Returns:
        str: Current timestamp in ISO format
    """
    return datetime.now().isoformat()

def perform_calculation(a: float, b: float, operation: str = "add") -> float:
    """
    Perform a basic mathematical calculation.

    Args:
        a: First number
        b: Second number
        operation: Operation to perform (add, subtract, multiply, divide)

    Returns:
        float: Result of the calculation
    """
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else 0
    }

    return operations.get(operation, operations["add"])(a, b)

def register_tools(mcp_instance: Any) -> None:
    """Register example tools with the MCP instance."""

    @mcp_instance.tool()
    def get_current_time_tool() -> str:
        """
        Get the current timestamp in ISO format.

        This tool provides the current date and time which can be useful for
        timestamping operations, logging, or time-sensitive calculations.

        Returns:
            str: Current timestamp in ISO 8601 format (e.g., "2025-08-15T14:30:45.123456")

        Use Cases:
            - Add timestamps to generated content
            - Calculate time differences
            - Log when operations occurred
            - Provide current time context to users
        """
        return get_current_time()

    @mcp_instance.tool()
    def calculator_tool(a: float, b: float, operation: str = "add") -> float:
        """
        Perform basic mathematical calculations between two numbers.

        This tool provides fundamental arithmetic operations and handles
        division by zero gracefully by returning 0.

        Args:
            a (float): The first number in the calculation
            b (float): The second number in the calculation
            operation (str, optional): The mathematical operation to perform.
                Valid options: "add", "subtract", "multiply", "divide"
                Defaults to "add" if not specified or invalid operation provided.

        Returns:
            float: The result of the mathematical operation

        Examples:
            - calculator_tool(5, 3, "add") returns 8.0
            - calculator_tool(10, 2, "divide") returns 5.0
            - calculator_tool(7, 4, "multiply") returns 28.0
            - calculator_tool(15, 6, "subtract") returns 9.0

        Error Handling:
            - Division by zero returns 0.0 instead of raising an exception
            - Invalid operations default to addition

        Use Cases:
            - Perform calculations requested by users
            - Process numerical data in workflows
            - Support mathematical reasoning tasks
        """
        return perform_calculation(a, b, operation)
