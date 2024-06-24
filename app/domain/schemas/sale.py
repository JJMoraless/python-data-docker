from pydantic import BaseModel
from typing import Optional, List


class SaleSchema(BaseModel):
    id: Optional[int] = None
    currency: str

    items_quantity: int
    sub_total_amount: float
    total_discount_amount: float
    total_tax_amount: float
    total: float


class ItemDetailSchema(BaseModel):
    item_id: int
    quantity: int


class SalePaginatedQuerySchema(BaseModel):
    page: int = 1
    limit: int = 10