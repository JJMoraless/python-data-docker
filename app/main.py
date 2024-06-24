from fastapi import FastAPI
import uvicorn
from .config import envs

from .config.database import Base, engine
from .presentation.middlewares.error_handler import ErrorHandler
from .presentation import routes
from .data.models import *
from .data.seeders.user_roles import seed_user_roles

app = FastAPI()
app.title = "fas api IA - TEST"
app.version = "0.0.1"

# DB - DDL
# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# seeders
seed_user_roles()



# middlewares
app.add_middleware(ErrorHandler)


# routers
app.include_router(prefix="/countries", router=routes.country_router)
app.include_router(prefix="/items", router=routes.item_router)
app.include_router(prefix="/sales", router=routes.sale_router)
app.include_router(prefix="/auth", router=routes.auth_router)
app.include_router(prefix="/emails-acounts", router=routes.email_acount_router)


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=envs.HOST,
        port=envs.PORT,
        reload=True,
    )
