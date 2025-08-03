from strands import Agent, tool

from news_agent.news_assistant import news_assistant
from news_agent.mcp_client import STANDARD_MODEL

USER_ID = "mem0_user"

CUSTOMER_INTERACTION_PROMPT = """
You are a News Curator Assistant.
Your job is to summarize current news articles and present them in a concise, human-friendly way.
You can call on other agents or tools to:
Fetch the latest news
Analyze news topics
Detect sentiment, bias, or trends
Extract key events or timelines

Respond clearly, accurately, and briefly.
Do not fabricate news. Always rely on factual content returned by tools.
"""
# Use the MCP server in a context manager
# Get the tools from the MCP server


def customer_interaction_agent():
    """
    Creates an agent that can interact with the customer and use the tools to create and manage cases.
    """
    return Agent(
        model=STANDARD_MODEL,
        tools=[news_assistant],
        system_prompt=CUSTOMER_INTERACTION_PROMPT
    )