from fastapi import APIRouter, Query
from .services.ia_service import IaService
from ..domain.responses.api_response import ResApi

ia_router = APIRouter()
ia_service = IaService()


@ia_router.get(
    "/prompt-template",
    tags=["ia"],
)
def prompt(phrase: str = Query("feliz")):
    prompt_res = ia_service.prompt_template(phrase)
    return ResApi.ok(data=prompt_res)


@ia_router.get(
    "/prompt-template-chains",
    tags=["ia"],
)
def prompt_chains(phrase: str = Query("")):
    prompt_res = ia_service.prompt_template_chains(phrase)
    return ResApi.ok(data=prompt_res)


@ia_router.post(
    "/save-model",
    tags=["ia"],
)
def save_model():
    model_saved = ia_service.save_model()
    return ResApi.ok(data=model_saved)


@ia_router.post(
    "/mistral",
    tags=["ia"],
)
def mistral():
    mistral_res = ia_service.mistral_ia()
    return ResApi.ok(data=mistral_res)

  