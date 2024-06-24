from fastapi import APIRouter, Depends
from app.config.database import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.domain.schemas.user import UserSchema, UserLoginSchema
from app.domain.responses.api_response import ResApi

from .services.auth_service import AuthService
from .services.user_service import UserService

from ..domain.responses.api_response import ResApi
from ..domain.errors.api_error import ApiError
from fastapi import Request

from fastapi import Depends
from .middlewares.jwt_middleware import JWTBearerMiddleware


auth_router = APIRouter()
auth_service = AuthService(Session())
user_service = UserService(Session())


@auth_router.post("/register", tags=["auth"])
def register_user(user: UserSchema):
    login_data = auth_service.register_user(user)
    return ResApi.ok(login_data)


@auth_router.post("/login", tags=["auth"])
def login_user(user: UserLoginSchema):
    login_data = auth_service.login_user(email=user.email, password=user.password)
    token = login_data.get("token")
    data = auth_service.validate_token(token)
    return ResApi.ok({"token": token, "cosa": data})


@auth_router.post("/token", tags=["auth"])
def get_access_token(self, form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        access_token = self.userService.get_access_token(form_data)
        if access_token["access_token"] is None:
            raise ApiError.unauthorized("Invalid credentials")
        return access_token
    except Exception as e:
        raise ApiError.unauthorized("Invalid credentials") from e


@auth_router.get("/me", tags=["auth"], dependencies=[Depends(JWTBearerMiddleware())])
def get_access_token(request: Request):
    user_id = request.state.user.get("id")
    user_found = user_service.get_user_by_id(user_id)
    user_found = user_found.to_dict()
    user_found.pop("password")
    return ResApi.ok({"user": user_found})
