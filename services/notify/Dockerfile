FROM python:3.11-slim-buster

WORKDIR /usr/src/notify

ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH=/usr/src

COPY poetry.lock pyproject.toml ./

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY app app/

WORKDIR ./app