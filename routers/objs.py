"""
Type Floor One, Garden and so on
"""

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

obj_app = APIRouter(prefix="/obj")


@obj_app.get("/", tags=["obj"])
async def show_all_objs(request: Request):
    """Return all clients"""
    return templates.TemplateResponse(
        "objs.html", {"request": request, "title": "Обекти"}
    )


@obj_app.post("/", tags=["obj"])
async def new_obj():
    """Return all clients"""
    return {"message": "New clients"}


@obj_app.put("/{obj_id}", tags=["obj"])
async def edit_obj():
    """Return all clients"""
    return {"message": "Edit clients"}


@obj_app.delete("/{obj_id}", tags=["obj"])
async def delete_client():
    """Return all clients"""
    return {"message": "Delete clients"}
