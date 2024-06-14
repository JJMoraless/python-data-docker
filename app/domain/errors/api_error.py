from typing import Dict
from fastapi import HTTPException, status


class ApiError(HTTPException):
    def __init__(
        self,
        status_code: int,
        msg: str | None = None,
        headers: Dict[str, str] | None = None,
    ) -> None:

        detail = {
            "ok": False,
            "status": status_code,
            "msg": msg,
        }

        super().__init__(status_code, detail, headers)

    @staticmethod
    def not_found(msg: str | None):
        return ApiError(status_code=status.HTTP_404_NOT_FOUND, msg=msg)

    @staticmethod
    def bad_request(msg: str | None):
        return ApiError(status_code=status.HTTP_400_BAD_REQUEST, msg=msg)

    @staticmethod
    def unauthorized(msg: str | None):
        return ApiError(status_code=status.HTTP_401_UNAUTHORIZED, msg=msg)
