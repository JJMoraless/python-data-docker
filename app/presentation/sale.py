from fastapi import APIRouter, Depends
from .middlewares.jwt_middleware import JWTBearerMiddleware
from fastapi import Request

from ..domain.schemas.sale import SaleSchema
from ..domain.responses.api_response import ResApi

from .services.sale_service import SaleService
from ..config.database import Session


sale_router = APIRouter(dependencies=[Depends(JWTBearerMiddleware())])
sale_service = SaleService(Session())


@sale_router.post("", tags=["sales"])
def create_sale(sale: SaleSchema, request: Request):
    user = request.state.user
    sale_created = sale_service.create_sale(sale=sale, user_id=user["id"])
    return ResApi.created(data=sale_created)

@sale_router.post("/{sale_id}/items/{item_id}", tags=["sales"])
def add_item_to_sale(sale_id: int, item_id: int):
    sale_created = sale_service.add_item_to_sale(sale_id=sale_id, item_id=item_id)
    return ResApi.created(data=sale_created)

