FROM python:3.10.5-slim as python-base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONNUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    \
    POETRY_VERSION=1.6.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.env"
    
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

FROM python-base as builder-base
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential

RUN pip install poetry

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

RUN poetry install --no-dev

RUN poetry install

WORKDIR /app

COPY . /app/

EXPOSE 8000

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]