FROM python:3.10

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y libpq-dev
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]