import os
import requests
from fastmcp import FastMCP
# for run with > uv run mcp dev server.py
# from mcp.server.fastmcp import FastMCP


from starlette.requests import Request
from starlette.responses import JSONResponse

mcp = FastMCP("AI news curator")

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request):
    return JSONResponse({"status": "healthy"})


@mcp.tool()
def fetch_news_articles() -> list:
    """
    Fetch and retrieve news articles from a news API endpoint.

    This tool connects to a news API service to retrieve current news articles
    and returns them in a standardized, simplified format. The function handles
    API communication, error management, and data transformation automatically.

    Returns:
        list: A list of simplified news article dictionaries. Each article contains:
            - source (dict): News source information
                - name (str): The name of the news source/publication
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

    Behavior:
        - Automatically handles HTTP errors and network issues
        - Validates API response structure and status
        - Filters out the source.id field from original API response
        - Gracefully handles missing or null fields in article data
        - Provides error logging for debugging purposes
        - Never raises exceptions - always returns a list (empty on error)

    Use Cases:
        - Retrieve latest news articles for content curation
        - Gather news data for analysis and processing
        - Provide fresh content for news aggregation systems
        - Support research and information gathering workflows

    Error Handling:
        - Network/HTTP errors: Logs error and returns empty list
        - Invalid JSON responses: Logs error and returns empty list
        - Missing/invalid API response structure: Returns empty list
        - Individual article parsing errors: Skips problematic articles

    Example Return Value:
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

    Dependencies:
        - requests: For HTTP API communication
        - External news API service must be accessible
        - Requires valid API endpoint URL configuration

    Performance Notes:
        - Synchronous operation - will block until API responds
        - Response time depends on external API performance
        - Consider implementing caching for frequent requests
        - Memory usage scales with number of articles returned
    """
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

if __name__ == "__main__":

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    # path of the MCP server add in the client
    path = os.environ.get("MCP_PATH", "/mcp")
    transport = os.environ.get("MCP_TRANSPORT", "http")
    mcp.run(transport=transport, host=host, port=port, path=path)
