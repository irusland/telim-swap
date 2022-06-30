FROM --platform=linux/amd64 base:linux

WORKDIR /code

COPY /main.py /code
COPY /src /code/src
COPY /models_backend /code/models_backend

CMD ["python", "main.py"]
