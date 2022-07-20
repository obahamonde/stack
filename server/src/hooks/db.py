from sqlmodel import SQLModel, create_engine, Session
from fastapi import FastAPI
from src.conf import env

engine = create_engine(
    url=f"{env.DB_ENGINE}://{env.DB_USER}:{env.DB_PASSWORD}@{env.DB_HOST}:{env.DB_PORT}/{env.DB_NAME}",
    echo=False,
    pool_size=20,
    max_overflow=0)


session = Session(engine)


def useDB(app: FastAPI) -> FastAPI:

    @app.on_event("startup")
    async def startup():
        try:
            session = Session(engine)
            SQLModel.metadata.create_all(engine)
            print(session)
        except Exception as e:
            raise e

    @app.on_event("shutdown")
    async def shutdown():
        try:
            session.close()
        except Exception as e:
            raise e

    return app