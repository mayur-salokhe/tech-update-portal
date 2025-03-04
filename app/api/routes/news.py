from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.services.news_service import fetch_all_rss_news

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/news/", summary="News")
async def news_articles(request: Request):
    rss_news = await fetch_all_rss_news()
    return templates.TemplateResponse("news.html", {"request": request, "news_articles": rss_news})
