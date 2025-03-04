from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.api.routes import programming, python, news

app = FastAPI(title="Tech Update Portal")
templates = Jinja2Templates(directory="app/templates")

# Mount the static directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
app.include_router(programming.router)
app.include_router(python.router)
app.include_router(news.router)

@app.get("/", summary="Home Page")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
