from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.domain.schemas.item import Item

item_router = APIRouter()


@item_router.post("", tags=["items"])
def create_item(item: Item):
    return JSONResponse(
        content={"ok": True, "status": 201, "data": {"country": item.model_dump()}},
        status_code=201,
    )
