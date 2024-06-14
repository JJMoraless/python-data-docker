from fastapi import APIRouter, Depends
from app.config.database import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.domain.schemas.user import UserSchema, UserLoginSchema
from app.domain.responses.api_response import ResApi

from .services.auth_service import AuthService
from ..domain.responses.api_response import ResApi
from ..domain.errors.api_error import ApiError

auth_router = APIRouter()
auth_service = AuthService(Session())


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
