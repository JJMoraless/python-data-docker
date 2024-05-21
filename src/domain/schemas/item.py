from pydantic import BaseModel, Field
from typing import Optional


class Item(BaseModel):
    id: Optional[int] = None
    name: str = Field(max_length=15, min_length=5, default="Generico")
    description: str
    price: float
    quantity: int
    is_offer: bool
    category: str
