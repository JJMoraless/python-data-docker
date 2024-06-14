from fastapi import Request
from fastapi.security import HTTPBearer

from ...domain.errors.api_error import ApiError
from ...domain.responses.api_response import ResApi
from ..services.auth_service import AuthService
from ..services.user_service import UserService

from app.config.database import Session


auth_service = AuthService(Session())
user_service = UserService(Session())


class JWTBearerMiddleware(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        if not auth:
            raise ApiError.unauthorized("Invalid token")

        payload = auth_service.validate_token(auth.credentials)
        

        if not user_service.get_user_by_id(payload.get("id")):
            raise ApiError.unauthorized("Invalid token *user")

        request.state.user = payload
