from sqlalchemy.orm import Session
from jwt import encode, decode

from ...config import envs
from ...domain.schemas.user import UserSchema
from ...domain.errors.api_error import ApiError
from ...data.models.user import UserModel

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends

from datetime import datetime
from datetime import timedelta

import bcrypt


class AuthService:

    def __init__(self, db: Session) -> None:
        self.db = db
        self.user = db.query(UserModel)

    # jwt
    def create_token(self, payload: dict) -> str:
        token: str = encode(
            payload=payload, key=envs.JWT_SECRET, algorithm=envs.JWT_ALGORITHM
        )
        return token

    def validate_token(self, token: str) -> dict:
        try:
            payload: dict = decode(
                jwt=token, key=envs.JWT_SECRET, algorithms=envs.JWT_ALGORITHM
            )
            return payload
        except:
            raise ApiError.unauthorized("Invalid token")

    # pass encript
    def encrypt_password(self, password: str) -> str:
        password_bytes = password.encode("utf-8")
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed.decode("utf-8")

    def check_pass(self, password: str, hashed: str):
        password_bytes = password.encode("utf-8")
        hashed_bytes = hashed.encode("utf-8")
        return bcrypt.checkpw(password_bytes, hashed_bytes)

    # user
    def register_user(self, user: UserSchema) -> dict:

        if self.user.filter_by(email=user.email).first():
            raise ApiError.not_found("email already exists")

        pass_encripted = self.encrypt_password(user.password)
        user_dict = {**user.model_dump(), "password": pass_encripted}
        new_user = UserModel(**user_dict)
        self.db.add(new_user)
        self.db.commit()

        user = new_user.to_dict()
        del user["password"]
        token = self.create_token(user)

        
        return {"token": token}

    def login_user(self, email: str, password: str) -> dict:
        user_found = self.db.query(UserModel).filter(UserModel.email == email).first()
        if not user_found:
            raise ApiError.unauthorized("Incorrect credentials")

        if not self.check_pass(password, user_found.password):
            raise ApiError.unauthorized("Incorrect credentials")

        user = user_found.to_dict()
        del user["password"]
        token = self.create_token(user)

        return {"token": token}
