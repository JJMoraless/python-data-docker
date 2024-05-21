from pydantic import BaseModel, Field
from typing import Optional


class Country(BaseModel):
    id: Optional[int] = None
    name: str = Field(max_length=15, min_length=5)
    code_iso_3: str
    code_phone: str
