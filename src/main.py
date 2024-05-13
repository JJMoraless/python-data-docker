from fastapi import FastAPI
from src.presentation.schemas.item import Item

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, World!"}


@app.post("/items")
def index_hola(item: Item):
    return {"message": "Hello, World!"}
