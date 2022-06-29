FROM base:latest as base
#FROM pytorch/torchserve:latest

WORKDIR /code

COPY /docker/pull-mar.sh /code
COPY /serve_models.sh /code
COPY /ts-config.properties /code
COPY /modelstore /code/modelstore

CMD ["sh", "-c", "./serve_models.sh"]
