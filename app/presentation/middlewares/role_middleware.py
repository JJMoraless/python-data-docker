from fastapi import Request
from starlette.responses import Response
from typing import List
from ...domain.errors.api_error import ApiError


def verify_role(allowed_roles: List[int]):
    def role_middleware(request: Request) -> Response:
        user = request.state.user

        if user["role_id"] not in allowed_roles:
            raise ApiError.forbiden(f"recurso no permitido")

        return request

    return role_middleware
