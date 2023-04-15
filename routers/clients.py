from fastapi import APIRouter

clients_app = APIRouter(prefix="/clients")


@clients_app.get("/clients", tags=["clients"])
async def show_all_clients():
    """Return all clients"""
    return {"message": "This is all clients"}


@clients_app.post("/client", tags=["clients"])
async def new_client():
    """Return all clients"""
    return {"message": "New clients"}


@clients_app.put("/client/{client_id}", tags=["clients"])
async def edit_client():
    """Return all clients"""
    return {"message": "Edit clients"}


@clients_app.delete("/client/{client_id}", tags=["clients"])
async def delete_client():
    """Return all clients"""
    return {"message": "Delete clients"}
