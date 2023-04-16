from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

clients_app = APIRouter(prefix="/client")


@clients_app.get("/", tags=["client"])
async def show_all_clients(request: Request):
    """Return all clients"""
    return templates.TemplateResponse(
        "contragents.html", {"request": request, "title": "Клиенти"}
    )


@clients_app.post("/", tags=["client"])
async def new_client():
    """Return all clients"""
    return {"message": "New clients"}


@clients_app.put("/{client_id}", tags=["client"])
async def edit_client():
    """Return all clients"""
    return {"message": "Edit clients"}


@clients_app.delete("/{client_id}", tags=["client"])
async def delete_client():
    """Return all clients"""
    return {"message": "Delete clients"}
