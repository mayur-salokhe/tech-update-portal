from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.services.article_service import fetch_articles

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/programming/", summary="Programming")
async def programming_articles(request: Request):
    programming_articles = await fetch_articles("programming")
    return templates.TemplateResponse("programming.html", {"request": request, "programming_articles": programming_articles})
