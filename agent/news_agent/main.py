"""
News Curator Agent - Main Module

This module creates a Strands agent for news curation that can fetch,
analyze, and summarize news articles using MCP tools.
"""

from strands import Agent, tool

from news_agent.news_assistant import news_assistant
from news_agent.mcp_client import STANDARD_MODEL

# User identifier for the news curator agent
USER_ID = "news_curator_user"

# System prompt that defines the agent's role and capabilities
CUSTOMER_INTERACTION_PROMPT = """
You are a News Curator Assistant.

Your primary responsibilities:
- Summarize current news articles in a concise, human-friendly way
- Present news information clearly and accurately
- Help users discover relevant news content

Available capabilities through MCP tools:
- Fetch the latest news from various sources
- Analyze news topics and content
- Detect sentiment, bias, or trends in articles
- Extract key events or create timelines

Guidelines:
- Respond clearly, accurately, and briefly
- Always rely on factual content returned by tools
- Do not fabricate or invent news information
- Provide helpful context when presenting news summaries
"""


def customer_interaction_agent():
    """
    Creates a Strands agent for news curation and customer interaction.

    This agent uses the news_assistant tool to fetch and process news
    through MCP server integration, providing intelligent news curation
    capabilities to users.

    Returns:
        Agent: Configured Strands agent with news tools and system prompt
    """
    return Agent(
        model=STANDARD_MODEL,  # AWS Bedrock Claude model
        tools=[news_assistant],  # MCP-based news processing tool
        system_prompt=CUSTOMER_INTERACTION_PROMPT
    )
