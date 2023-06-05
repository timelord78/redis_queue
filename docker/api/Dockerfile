FROM python:3.10

ENV TZ='Europe/Moscow'

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN pip install poetry

COPY poetry.lock pyproject.toml /usr/src/app/

COPY . /usr/src/app/

RUN poetry install --no-dev
