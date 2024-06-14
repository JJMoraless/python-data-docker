FROM python:3.10

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y libpq-dev build-essential cargo
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["python3.10","-m","app.main"]