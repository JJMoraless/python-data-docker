from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, World!"}


@app.get("/hola")
def index_hola():
    return {"message": "Hello, World!"}
