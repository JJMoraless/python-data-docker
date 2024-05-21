from fastapi import FastAPI
from src.data.models import *

from src.config.database import Base, engine
from src.presentation import routes

from src.presentation.middlewares.error_handler import  ErrorHandler

app = FastAPI()
app.title = "fas api IA - TEST"
app.version = "0.0.1"

# DB - DDL
# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# middlewares
app.add_middleware(ErrorHandler)


# routers
app.include_router(prefix="/countries", router=routes.country_router)
app.include_router(prefix="/items", router=routes.item_router)
app.include_router(prefix="/invoices", router=routes.invoice_router)
