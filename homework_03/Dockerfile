FROM python:3.10.8-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry==1.2.2

RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./

RUN poetry install --only main

COPY . /app

EXPOSE 8000

CMD uvicorn main:app --host 0.0.0.0 --port 8000