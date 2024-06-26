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


## variables de entorno
- JWT_SECRET="123"
- JWT_ALGORITHM="HS256"
- PORT=5000
- HOST="0.0.0.0" 
- DB_URL="postgresql://jhon:123@posgrest:5432/ia_facilpos" // depende de si modifico su contenedor de docker, pero, por default esta asi
