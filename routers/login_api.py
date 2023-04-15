from fastapi import APIRouter


login_app = APIRouter(prefix="/login")


@login_app.get("/login", tags=["login"])
async def get_login():
    """Login get Page"""
    return {"message": "Login GET"}


@login_app.post("/login", tags=["login"])
async def post_login():
    """Login Post page"""
    return {"message": "Login POST"}


@login_app.post("/logout", tags=["login"])
async def logout():
    """Logout url"""
    return {"message": "Logout page"}
