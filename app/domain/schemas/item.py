from pydantic import BaseModel, Field
from typing import Optional


class ItemSchema(BaseModel):
    id: Optional[int] = None
    description: str
    price: float
    img: str
