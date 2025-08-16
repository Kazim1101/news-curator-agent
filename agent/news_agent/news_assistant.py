"""
News Assistant Tool for Strands Agent
"""

from strands import Agent, tool
from news_agent.mcp_client import STREAMABLE_HTTP_MCP_CLIENT,STANDARD_MODEL

# System prompt for the document/news assistant
DOCUMENT_ASSISTANT_PROMPT = """
You are a News Assistant that helps users find, analyze, and summarize news articles.

Your capabilities:
- Fetch latest news articles from various sources
- Analyze news content for sentiment, topics, and trends
- Summarize news articles in a concise, readable format
- Search for specific news topics or keywords

Guidelines:
- Provide accurate, factual information only
- Be concise and clear in your responses
- Use the available MCP tools to fetch and analyze news
- Always cite sources when presenting news information
"""

@tool
def news_assistant(query: str) -> str:
    """
    News assistant tool that processes natural language queries about news.

    Args:
        query: Input from agent comprising of some natural language describing the news articles to be retrieved or summarized.

    Returns:
        A summary of the news articles or relevant information based on the query.
    """
    with STREAMABLE_HTTP_MCP_CLIENT:
        # Get the tools from the MCP server
        tools = STREAMABLE_HTTP_MCP_CLIENT.list_tools_sync()
        news_assistant_tools = [*tools]
        try:
            case_agent = Agent(
                system_prompt=DOCUMENT_ASSISTANT_PROMPT,
                tools=[*news_assistant_tools],
                model=STANDARD_MODEL,
            )

            # Call the agent and return its response
            response = case_agent(query)
            return str(response)
        except Exception as e:
            return f"Error in case assistant: {str(e)}"
