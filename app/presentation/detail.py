from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.domain.schemas.item import ItemSchema

item_router = APIRouter()


@item_router.post("", tags=["items"])
def create_item(item: ItemSchema):
    return JSONResponse(
        content={"ok": True, "status": 201, "data": {"country": item.model_dump()}},
        status_code=201,
    )
