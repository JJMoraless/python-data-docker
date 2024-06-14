from pydantic import BaseModel
from typing import Optional


class SaleSchema(BaseModel):
    id: Optional[int] = None
    currency: str

    items_quantity: int
    sub_total_amount: float
    total_discount_amount: float
    total_tax_amount: float
    total: float

