from pydantic import BaseModel, EmailStr

class EmailAcountSchema(BaseModel):
    provider: str
    email: EmailStr
    password: str
