FROM python:3.9.7

ARG ENV

ENV ENV=${ENV} \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.8 \
    POETRY_NO_INTERACTION=1

RUN mkdir /app
WORKDIR /app

RUN apt update && apt install -y cron

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml ./
COPY poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .

EXPOSE ${WEB_PORT}
