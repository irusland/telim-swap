FROM --platform=linux/amd64 python:3.10

ENV YOUR_ENV=production


RUN pip install poetry

WORKDIR /code

RUN apt-get update -y
RUN apt-get install -y gfortran libopenblas-dev liblapack-dev

COPY poetry.lock pyproject.toml /code/

RUN apt-get install -y ca-certificates-java \
    && apt-get install -y openjdk-11-jre-headless \
    && apt-get install -y git-lfs

RUN pip install scipy==1.8.1

RUN poetry config virtualenvs.create false \
    && poetry config experimental.new-installer false \
    && poetry install --no-interaction --no-ansi
