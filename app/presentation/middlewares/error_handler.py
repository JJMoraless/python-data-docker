from fastapi import FastAPI, status
from fastapi.responses import JSONResponse, Response
from fastapi.requests import Request

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp


class ErrorHandler(BaseHTTPMiddleware):

    def __init__(self, app: ASGIApp | FastAPI) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            content = f"ecxeption: {str(e)}"
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return JSONResponse(content=content, status_code=status_code)
