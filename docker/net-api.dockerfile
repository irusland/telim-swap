FROM --platform=linux/amd64 base:linux as base

WORKDIR /code

COPY /docker/pull-mar.sh /code
COPY /serve_models.sh /code
COPY /ts-config.properties /code
#COPY /modelstore /code/modelstore

CMD ["sh", "-c", "./pull-mar.sh && ./serve_models.sh"]
