from pydantic import BaseModel
from typing import Optional


class Invoice(BaseModel):
    id: Optional[int] = None
    items_quantity: int
    total: float
    total_discount: float
    total_tax: float
    currency: str
    created_at: str
  
