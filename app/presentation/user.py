from fastapi import APIRouter, Depends, Request, Query
from .middlewares.role_middleware import verify_role
from ..domain.enums.user_role import RoleEnum

from .middlewares.jwt_middleware import JWTBearerMiddleware

from ..domain.responses.api_response import ResApi
from .services.sale_service import SaleService


user_router = APIRouter(dependencies=[Depends(JWTBearerMiddleware())])
