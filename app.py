from fastapi import FastAPI

from routers import login_api, work_with_types, clients


app = FastAPI()
app.include_router(login_api.login_app)
app.include_router(work_with_types.types_app)
app.include_router(clients.clients_app)


@app.get("/index")
async def index():
    return {"message": "Index Page"}
