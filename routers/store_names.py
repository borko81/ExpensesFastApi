from fastapi import APIRouter

# Store for name's of type's: Salary, depozite, EVN, Water Supply...

names_of_store = APIRouter()


@names_of_store.get("/names", tags=["names"])
async def show_all_names():
    return {"message": "Show all names of stores"}


@names_of_store.post("/name", tags=["names"])
async def new_name():
    return {"message": "Create New name of stores"}


@names_of_store.put("/name/{name_id}", tags=["names"])
async def change_name():
    return {"message": "Edit Name"}


@names_of_store.delete("/name/{name_id}", tags=["names"])
async def delete_name():
    return {"message": "Delete Name"}
