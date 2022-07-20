

from fastapi import FastAPI
from src.hooks.db import useDB
from src.hooks.server import useServer
from src.hooks.auth import useAuth


def main():
    app = useAuth(useServer(useDB(FastAPI())))
    return app
