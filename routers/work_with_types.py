from fastapi import APIRouter


types_app = APIRouter(prefix="/types")


@types_app.get("/types", tags=["types"])
async def show_types():
    """
    Show all types, income, excome, mixed
    """
    return {"message": "Show Types "}


@types_app.post("/types", tags=["types"])
async def create_new_type():
    """
    Create new types
    """
    return {"message": "New Types "}


@types_app.put("/type/{type_id}", tags=["types"])
async def edit_type():
    """
    Create new types
    """
    return {"message": "Change Type "}


@types_app.delete("/type/{type_id}", tags=["types"])
async def delete_type():
    """
    Create new types
    """
    return {"message": "Delete Type "}
