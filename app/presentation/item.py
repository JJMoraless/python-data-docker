from fastapi import APIRouter
from ..domain.responses.api_response import ResApi

from app.domain.schemas.item import ItemSchema
from fastapi import Request
from ..presentation.services.item_service import ItemService
from ..config.database import Session

from .middlewares.jwt_middleware import JWTBearerMiddleware
from fastapi import Depends

item_router = APIRouter(dependencies=[Depends(JWTBearerMiddleware())])
item_service = ItemService(Session())


@item_router.post("", tags=["items"])
def create_item(item: ItemSchema, request: Request):
    item_created = item_service.create_item(item=item)
    return ResApi.created(data=item_created)


@item_router.get("", tags=["items"])
def get_items():
    items = item_service.get_items()
    return ResApi.ok(data=items)
