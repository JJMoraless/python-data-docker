from typing import Dict, Any
from fastapi import status
from fastapi.responses import JSONResponse


class ResApi(JSONResponse):
    def __init__(
        self,
        data: Any,
        status_code: int = 200,
        headers: Dict[str, str] | None = None,
    ) -> None:

        content = {
            "ok": True,
            "status": status_code,
            "data": data,
        }

        super().__init__(content=content, status_code=status_code, headers=headers)

    @staticmethod
    def ok(data: Any):
        status_code = status.HTTP_200_OK
        return ResApi(data=data, status_code=status_code)

    @staticmethod
    def created(data: Any):
        status_code = status.HTTP_201_CREATED
        return ResApi(data=data, status_code=status_code)
