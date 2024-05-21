from fastapi import APIRouter
from fastapi.responses import JSONResponse

from src.domain.schemas.invoice import Invoice

invoice_router = APIRouter()


@invoice_router.post("", tags=["invoices"])
def create_item(invoice: Invoice):
    
    return JSONResponse(
        content={"ok": True, "status": 201, "data": "oko"},
        status_code=201,
    )
