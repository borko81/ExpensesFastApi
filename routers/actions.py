"""
Real action is here
"""

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

actions = APIRouter(prefix="/action")


@actions.get("/", tags=["actions"])
async def show_all_action(request: Request):
    """Login get Page"""
    return templates.TemplateResponse(
        "action.html", {"request": request, "title": "Действие"}
    )


@actions.post("/", tags=["actions"])
async def new_action(request: Request):
    """Login Post page"""
    return templates.TemplateResponse(
        "action.html", {"request": request, "title": "Действие"}
    )


@actions.put("/{action_id}", tags=["actions"])
async def edit_action():
    """Login Post page"""
    return {"message": "Action EDIT"}


@actions.delete("/{action_id}", tags=["actions"])
async def delete_action():
    """Login Post page"""
    return {"message": "Action DELETE"}
