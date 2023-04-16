from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


login_app = APIRouter(prefix="/login")
templates = Jinja2Templates(directory="templates")


@login_app.get("/", tags=["login"], response_class=HTMLResponse)
async def get_login(request: Request):
    """Login get Page"""
    return templates.TemplateResponse("login.html", {"request": request})


@login_app.post("/", tags=["login"])
async def post_login(request: Request):
    """Login Post page"""
    return {"message": "Login POST"}


@login_app.get("/exit", tags=["login"])
async def logout(request: Request):
    """Logout url"""
    return templates.TemplateResponse("login.html", {"request": request})
