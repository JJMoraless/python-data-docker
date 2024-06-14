from fastapi import APIRouter, Depends
from ..domain.responses.api_response import ResApi
from ..domain.schemas.email import EmailAcountSchema
from ..config.database import Session
from .middlewares.jwt_middleware import JWTBearerMiddleware
from fastapi import Request

from.services.email_service import EmailService

email_service = EmailService(Session())
email_acount_router = APIRouter(dependencies=[Depends(JWTBearerMiddleware())])

# 1. leer csv del correo enviado la id del correo
# 2. una task que lea correos de usuarios que tenga activado el automatico
# 3. sacar estadisticas de los correos leidos
# 4. sacar graficas de los csv sacados de los correos


@email_acount_router.post("/", tags=["emails"])
def save_email_acount(email_acount: EmailAcountSchema, request: Request):
    user_id = request.state.user.get("id")
    email_acount = email_service.save_email_acount(email_acount, user_id)

    return ResApi.created(data=email_acount)

@email_acount_router.get("/", tags=["emails"])
def get_email_acounts(request: Request):
    user_id = request.state.user.get("id")
    email_acounts = email_service.get_email_acounts(user_id)

    return ResApi.ok(data=email_acounts)


@email_acount_router.get("/{email_id}", tags=["emails"])
def read_email(email_id: int):
    data_inbox = email_service.read_email(email_id)
    
    return ResApi.ok(data=data_inbox)