"""
Configuration for Casa
"""

from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from typing import Annotated
from sqlalchemy.orm import Session

from db import database
from db import models

templates = Jinja2Templates(directory="templates")


casa = APIRouter(prefix="/casa")


@casa.get("/", tags=["casa"])
async def show_all_casa(
    request: Request, db=Annotated[Session, Depends(database.get_db)]
):
    """Login get Page"""
    return templates.TemplateResponse(
        "kasa.html",
        {"request": request, "title": "Kasa", "kasa": db.query(models.Kasa).all()},
    )


@casa.post("/", tags=["casa"])
async def new_casa():
    """Login Post page"""
    return {"message": "Action POST"}


@casa.put("/{action_id}", tags=["casa"])
async def edit_casa():
    """Login Post page"""
    return {"message": "Action EDIT"}


@casa.delete("/{action_id}", tags=["casa"])
async def delete_delete():
    """Login Post page"""
    return {"message": "Action DELETE"}
