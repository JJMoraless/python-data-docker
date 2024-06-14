from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    email: str
    name: str = Field(max_length=15, min_length=5)
    password: str = Field(max_length=100, min_length=5)


class UserLoginSchema(BaseModel):
    email: str
    password: str = Field(max_length=100, min_length=5)
