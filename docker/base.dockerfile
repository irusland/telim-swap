FROM python:3.10

ENV YOUR_ENV=production
#  PYTHONFAULTHANDLER=1 \
#  PYTHONUNBUFFERED=1 \
#  PYTHONHASHSEED=random \
#  PIP_NO_CACHE_DIR=off \
#  PIP_DISABLE_PIP_VERSION_CHECK=on \
#  PIP_DEFAULT_TIMEOUT=100 \
#  POETRY_VERSION=1.0.0

RUN pip install poetry

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi
