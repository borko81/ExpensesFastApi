from fastapi import APIRouter

"""
Type income, outcoume
"""

types_app = APIRouter(prefix="/type")


@types_app.get("/", tags=["type"])
async def show_types():
    """
    Show all types, income, excome, mixed
    """
    return {"message": "Show Types "}


@types_app.post("/", tags=["type"])
async def create_new_type():
    """
    Create new types
    """
    return {"message": "New Types "}


@types_app.put("/{type_id}", tags=["type"])
async def edit_type():
    """
    Create new types
    """
    return {"message": "Change Type "}


@types_app.delete("/{type_id}", tags=["type"])
async def delete_type():
    """
    Create new types
    """
    return {"message": "Delete Type "}
