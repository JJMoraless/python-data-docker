- version de python: 3.10

## ejecucion

la api se peude ejcutar tanto en su maquina tanto como en docker, lo mas reomendable es usar docker

- en local con python 10:
  - `python3.10 -m app.main`
  - `pip install /app/requirements.txt`

- docker:
  - `docker compose build`
  - `docker compose up`

## dependencias

- pandas
- fast api - uvicorn
- bcrypt
