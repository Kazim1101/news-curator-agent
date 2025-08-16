import requests
from typing import Any

def fetch_news_articles() -> list:
    try:
        response = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=KEY_HERE")
        response.raise_for_status()  # Raise error if bad response

        data = response.json()
        if data.get("status") != "ok" or "articles" not in data:
            return []

        simplified_articles = []
        for article in data["articles"]:
            simplified = {
                "source": {
                    "name": article.get("source", {}).get("name")
                },
                "author": article.get("author"),
                "title": article.get("title"),
                "description": article.get("description"),
                "url": article.get("url"),
                "urlToImage": article.get("urlToImage"),
                "publishedAt": article.get("publishedAt"),
                "content": article.get("content")
            }
            simplified_articles.append(simplified)

        return simplified_articles

    except requests.RequestException as e:
        print(f"HTTP error: {e}")
        return []
    except ValueError as e:
        print(f"JSON decode error: {e}")
        return []

def register_tools(mcp_instance: Any) -> None:
    """Register news fetcher tools with the MCP instance."""

    @mcp_instance.tool()
    def fetch_news_articles_tool() -> list:
        """
        Fetch and retrieve current news articles from a news API endpoint.

        This tool connects to a news API service to retrieve current news articles
        and returns them in a standardized, simplified format. The function handles
        API communication, error management, and data transformation automatically.

        Returns:
            list: A list of simplified news article dictionaries. Each article contains:
                - source (dict): News source information with 'name' field
                - author (str|None): Article author name, if available
                - title (str|None): Article headline/title
                - description (str|None): Brief article summary/description
                - url (str|None): Direct link to the full article
                - urlToImage (str|None): URL to article's featured image
                - publishedAt (str|None): Article publication timestamp (ISO format)
                - content (str|None): Article content preview/snippet

        Returns an empty list [] if:
            - API request fails (network issues, timeout, etc.)
            - API returns error status (not "ok")
            - Response doesn't contain articles data
            - JSON parsing fails

        Use Cases:
            - Retrieve latest news articles for content curation
            - Gather news data for analysis and processing
            - Provide fresh content for news aggregation systems
            - Support research and information gathering workflows

        Example Return:
            [
                {
                    "source": {"name": "BBC News"},
                    "author": "John Doe",
                    "title": "Breaking: Major Technology Breakthrough",
                    "description": "Scientists announce revolutionary discovery...",
                    "url": "https://example.com/article",
                    "urlToImage": "https://example.com/image.jpg",
                    "publishedAt": "2025-08-03T10:30:00Z",
                    "content": "In a groundbreaking development..."
                }
            ]

        Note: This tool fetches US top headlines and never raises exceptions.
        """
        return fetch_news_articles()
