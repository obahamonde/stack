from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

def useServer(app: FastAPI)->FastAPI:
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
    app.mount("/tmp", StaticFiles(directory="tmp"))
    return app