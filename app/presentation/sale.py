from fastapi import APIRouter, Depends, Request, Query
from .middlewares.role_middleware import verify_role
from ..domain.enums.user_role import RoleEnum


from .middlewares.jwt_middleware import JWTBearerMiddleware


from typing import List
from ..domain.schemas.sale import SaleSchema, ItemDetailSchema
from ..domain.responses.api_response import ResApi

from .services.sale_service import SaleService
from ..config.database import Session


sale_router = APIRouter(dependencies=[Depends(JWTBearerMiddleware())])
sale_service = SaleService(Session())


@sale_router.post(
    "",
    tags=["sales"],
    dependencies=[Depends(verify_role(RoleEnum.ALL.value))],
)
def create_sale(sale: SaleSchema, request: Request):
    auth_user = request.state.user
    sale_created = sale_service.create_sale(sale, auth_user["id"])
    return ResApi.created(data=sale_created)


@sale_router.post("/{sale_id}/details", tags=["sales"])
def add_items_to_sale(sale_id: int, items: List[ItemDetailSchema], request: Request):
    user_id = request.state.user["id"]

    sale = sale_service.add_items_to_sale(sale_id, items, user_id)
    return ResApi.ok(data=sale)


@sale_router.get(
    "/{sale_id}/details",
    tags=["sales"],
    dependencies=[Depends(verify_role(RoleEnum.ALL.value))],
)
def get_sale_by_id(sale_id: int, request: Request):
    user_id = request.state.user["id"]

    sale = sale_service.get_sale_with_details(sale_id, user_id)
    return ResApi.ok(data=sale)


@sale_router.delete(
    "/{sale_id}/cancel",
    tags=["sales"],
    dependencies=[Depends(verify_role(RoleEnum.ALL.value))],
)
def cancel_sale(sale_id: int, request: Request):
    user_id = request.state.user["id"]
    sale = sale_service.cancel_sale(sale_id, user_id)
    return ResApi.ok(data=sale)


@sale_router.put(
    "/{sale_id}/complete",
    tags=["sales"],
    dependencies=[Depends(verify_role(RoleEnum.ALL.value))],
)
def complete_sale(sale_id: int, request: Request):
    user_id = request.state.user["id"]
    sale = sale_service.complete_sale(sale_id, user_id)
    return ResApi.ok(data=sale)


@sale_router.get(
    "",
    tags=["sales"],
    dependencies=[Depends(verify_role([RoleEnum.ADMIN.value, [RoleEnum.ROOT.value]]))],
)
def get_sales(
    request: Request,
    page: int = Query(1, description="Page number of the results"),
    page_size: int = Query(10, description="Number of results per page", le=50),
):
    user_id = request.state.user["id"]
    sales = sale_service.get_sales(user_id, page, page_size)
    return ResApi.ok(data=sales)
