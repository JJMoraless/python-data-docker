from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse

import pandas as pd
import matplotlib.pyplot as plt

import os
import csv

from src.domain.schemas.country import Country
from src.data.models.country import Country as CountryModel
from src.config.database import Session

from src.presentation.services.country import CountryService

country_service = CountryService(Session())
country_router = APIRouter()


@country_router.post("", tags=["countries"])
def create_countrie(country: Country):
    country_created = country_service.create_country(country)
    return JSONResponse(
        content={"ok": True, "status": 201, "data": {"country": country_created.to_dict()}},
        status_code=201,
    )


@country_router.get("/csv", tags=["countries"])
def get_countries_csv():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "../store/paises.csv")

    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        countries = list(reader)

    return JSONResponse(
        content={
            "ok": True,
            "status": 201,
            "data": {"path": file_path, "countries": countries},
        },
        status_code=201,
    )


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

    return JSONResponse(
        content={
            "ok": True,
            "status": 201,
            "data": {"countries": [country.to_dict() for country in countries_found]},
        },
        status_code=201,
    )


@country_router.get("/{id}", tags=["countries"])
def get_country_by_id(id):
    country_found = country_service.get_country_by_id(id)
    
    if(not country_found):
        return JSONResponse(
            content={
                "ok": False,
                "status": 404,
                "data": {"country": None},
            },
            status_code=404,
        )
    

    return JSONResponse(
        content={
            "ok": True,
            "status": 201,
            "data": {"country": country_found.to_dict() or None},
        },
        status_code=201,
    )


