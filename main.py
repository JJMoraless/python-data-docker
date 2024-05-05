import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "docker update 2"}


@app.get("/categories", response_class=HTMLResponse)
def read_categories():
    categories = store.get_categories()
    return categories
