from fastapi import APIRouter
from fastapi.responses import FileResponse
from fastapi import Request


import pandas as pd
import matplotlib.pyplot as plt

import os
import csv

from app.config.database import Session
from app.presentation.services.country_service import CountryService

from ..domain.schemas.country import CountrySchema
from ..domain.responses.api_response import ResApi
from ..domain.errors.api_error import ApiError

from fastapi import Depends
from .middlewares.jwt_middleware import JWTBearerMiddleware

country_service = CountryService(Session())
country_router = APIRouter(dependencies=[Depends(JWTBearerMiddleware())])


@country_router.post("", tags=["countries"])
def create_countrie(country: CountrySchema):
    country_created = country_service.create_country(country)
    return ResApi.created({"country": country_created.to_dict()})


@country_router.get("/csv", tags=["countries"])
def get_countries_csv(request: Request):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "../storage/paises.csv")

    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        countries = list(reader)

    user = request.state.user

    return ResApi.ok({"countries": user})


@country_router.get("/pandas", tags=["countries"])
def get_countries_pandas():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "../store/paises.csv")

    df = pd.read_csv(file_path, index_col=0)
    df.plot(kind="bar")
    plt.savefig("df.png")

    return FileResponse("df.png", media_type="image/png")


@country_router.get("", tags=["countries"])
def get_countries():
    countries_found = country_service.get_countries()
    return ResApi.ok({"countries": [country.to_dict() for country in countries_found]})


@country_router.get("/{id}", tags=["countries"])
def get_country_by_id(id):
    country_found = country_service.get_country_by_id(id)

    if not country_found:
        raise ApiError.not_found("Country not found")

    return ResApi.ok({"country": country_found.to_dict()})
