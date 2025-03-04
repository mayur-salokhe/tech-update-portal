import httpx

# Define API URLs here to avoid repetition
API_URLS = {
    "python": "https://dev.to/api/articles?tag=python&top=5",
    "programming": "https://dev.to/api/articles?tag=programming&top=5"
}

async def fetch_articles(category: str):
    """Fetch articles from Dev.to based on category ('python' or 'programming')."""
    url = API_URLS.get(category)
    if not url:
        return []  # Return empty list if category is invalid

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json() if response.status_code == 200 else []
