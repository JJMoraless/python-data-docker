from fastapi import APIRouter
from ..domain.responses.api_response import ResApi
from ..presentation.services.item_service import ItemService
from ..config.database import Session
from app.domain.schemas.item import ItemSchema

from .middlewares.jwt_middleware import JWTBearerMiddleware
from fastapi import Depends

item_router = APIRouter(dependencies=[Depends(JWTBearerMiddleware())])
item_service = ItemService(Session())


@item_router.post("", tags=["items"])
def create_item(item: ItemSchema):
    item_created = item_service.create_item(item=item)
    return ResApi.created(data=item_created)


@item_router.get("", tags=["items"])
def get_items():
    items = item_service.get_items()
    return ResApi.ok(data=items)


@item_router.put("/{item_id}", tags=["items"])
def update_item(item_id: int, item: ItemSchema):
    item_updated = item_service.update_item(item_id, item)
    return ResApi.ok(data=item_updated)


@item_router.delete("/{item_id}", tags=["items"])
def delete_item(item_id: int):
    item_deleted = item_service.delete_item(item_id)
    return ResApi.ok(data=item_deleted)
