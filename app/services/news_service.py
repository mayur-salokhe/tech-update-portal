import asyncio
import httpx
import feedparser

# Dictionary of RSS sources
RSS_FEEDS = {
    "thehindu":"https://www.thehindu.com/sci-tech/science/feeder/default.rss", 
    # "https://www.thehindu.com/news/feeder/default.rss",
    "toi": "https://timesofindia.indiatimes.com/rssfeeds/66949542.cms",
    # "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
    "ndtv": "https://feeds.feedburner.com/gadgets360-latest"
    # https://feeds.feedburner.com/ndtvnews-top-stories
}

async def fetch_rss_news(source: str):
    """Fetch news from a specific RSS source asynchronously."""
    rss_url = RSS_FEEDS.get(source)
    if not rss_url:
        return []  # Return empty list if source is invalid

    async with httpx.AsyncClient() as client:
        response = await client.get(rss_url)
        if response.status_code != 200:
            return []  # Return empty list if fetching fails

    feed = feedparser.parse(response.text)
    return [
        {
            "source": source.replace("_", " ").title(),
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        }
        for entry in feed.entries[:5]  # Fetch first 5 articles
    ]

async def fetch_all_rss_news():
    """Fetch news from all sources asynchronously."""
    tasks = [fetch_rss_news(source) for source in RSS_FEEDS]
    results = await asyncio.gather(*tasks)
    return [article for result in results for article in result]  # Flatten the list
