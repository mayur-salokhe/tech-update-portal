from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.services.article_service import fetch_articles

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/python/", summary="Python")
async def python_articles(request: Request):
    python_articles = await fetch_articles("python")
    return templates.TemplateResponse("python.html", {"request": request, "python_articles": python_articles})
