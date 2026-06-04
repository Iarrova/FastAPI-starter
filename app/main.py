from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel

from app.database import engine
from app.exceptions.handlers import register_exception_handlers
from app.routers import user


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(user.router)
register_exception_handlers(app)


@app.get("/")
def health():
    return {"status": "ok"}
