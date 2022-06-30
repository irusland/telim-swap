FROM --platform=linux/amd64 python:3.10

ENV YOUR_ENV=production


RUN pip install poetry

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi


RUN apt-get update
RUN apt-get install -y openjdk-11-jre-headless
RUN apt-get install git-lfs
