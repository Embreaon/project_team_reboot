from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("main.html", {"request":request})

@app.get("/menu")
async def menu(request: Request):
    return templates.TemplateResponse("menu.html", {"request":request})