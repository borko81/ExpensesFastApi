"""
Type Floor One, Garden and so on
"""

from fastapi import APIRouter

obj_app = APIRouter(prefix="/obj")


@obj_app.get("/", tags=["obj"])
async def show_all_objs():
    """Return all clients"""
    return {"message": "This is all clients"}


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
