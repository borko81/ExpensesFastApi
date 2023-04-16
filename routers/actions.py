"""
Real action is here
"""

from fastapi import APIRouter


actions = APIRouter(prefix="/action")


@actions.get("/", tags=["actions"])
async def show_all_action():
    """Login get Page"""
    return {"message": "Actions GET"}


@actions.post("/", tags=["actions"])
async def new_action():
    """Login Post page"""
    return {"message": "Action POST"}


@actions.put("/{action_id}", tags=["actions"])
async def edit_action():
    """Login Post page"""
    return {"message": "Action EDIT"}


@actions.delete("/{action_id}", tags=["actions"])
async def delete_action():
    """Login Post page"""
    return {"message": "Action DELETE"}
