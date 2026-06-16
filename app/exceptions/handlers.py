from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.exceptions.exceptions import (
    ConflictException,
    NotFoundException,
    UnauthorizedException,
)


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(UnauthorizedException)
    async def unauthorized_handler(request: Request, exc: UnauthorizedException):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": exc.detail, **exc.context},
        )

    @app.exception_handler(NotFoundException)
    async def not_found_handler(request: Request, exc: NotFoundException):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": exc.detail, **exc.context},
        )

    @app.exception_handler(ConflictException)
    async def conflict_handler(request: Request, exc: ConflictException):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": exc.detail, **exc.context},
        )
