from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from routers import (
    login_api,
    work_with_types,
    clients,
    actions,
    objs,
    kasa,
)


templates = Jinja2Templates(directory="templates")


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
# Login router: Login, Logout
app.include_router(login_api.login_app)
# Type router: is this income or outcome or mixed.
app.include_router(work_with_types.types_app)
# Client router: person, client
app.include_router(clients.clients_app)
# Actions
app.include_router(actions.actions)
# Obj's
app.include_router(objs.obj_app)
# Kasa: Bank, Cash and so on
app.include_router(kasa.casa)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "base.html", {"request": request, "title": "Expensive Base Page"}
    )
