from src.hooks.auth import Auth, useAuth
from src.hooks.server import useServer
from fastapi import FastAPI, Request, Response
from src.model.collections import User
from starlette.responses import JSONResponse
from src.router.api import api

app = useAuth(useServer(FastAPI()))
app.include_router(api)
@app.get("/api")
async def api_root(request: Request)->Response:
    user = User(**request.state.user).create()
    return JSONResponse(user)