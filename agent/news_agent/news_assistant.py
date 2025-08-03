from strands import Agent, tool
from news_agent.mcp_client import STREAMABLE_HTTP_MCP_CLIENT,STANDARD_MODEL

DOCUMENT_ASSISTANT_PROMPT = """
You can call on other agents or tools to:
Fetch the latest news
Analyze news topics
Detect sentiment, bias, or trends
Extract key events or timelines
You are only allowed to do the given news related information coming on the data coming from the mcp tools, deny all other requests.
Follow the instructions cafully and stick to the workflows. Answer in json format.
"""

@tool
def news_assistant(query: str) -> str:
    """
    This is a news assistant that helps users retrieve and summarize news articles.

    Args:
        query: Input from agent comprising of some natural language describing the news articles to be retrieved or summarized.


    Returns:
        A summary of the news articles or relevant information based on the query.
    """
    with STREAMABLE_HTTP_MCP_CLIENT:
        # Get the tools from the MCP server
        tools = STREAMABLE_HTTP_MCP_CLIENT.list_tools_sync()
        kundenangaben_tools = [*tools]
        try:
            case_agent = Agent(
                system_prompt=DOCUMENT_ASSISTANT_PROMPT,
                tools=[*kundenangaben_tools],
                model=STANDARD_MODEL,
            )

            # Call the agent and return its response
            response = case_agent(query)
            return str(response)
        except Exception as e:
            return f"Error in case assistant: {str(e)}"