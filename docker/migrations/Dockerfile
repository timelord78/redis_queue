FROM python:3.10

ENV TZ='Europe/Moscow'
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /migrations
COPY pyproject.toml /migrations
COPY poetry.lock /migrations

RUN apt-get update && apt-get install -y --no-install-recommends dos2unix

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
WORKDIR /migrations
RUN poetry install --no-dev

COPY /migrations /migrations/migrations
COPY /scripts /migrations/scripts
COPY /app /migrations/app

RUN dos2unix scripts/*