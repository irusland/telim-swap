ENV_FILE = .env

include ${ENV_FILE}
$(eval export $(shell sed -ne 's/ *#.*$$//; /./ s/=.*$$// p' ${ENV_FILE}))


pre-init:
	apt-get install zip unzip


mac-pre-init:
	brew install wget


install:
	poetry install

serve:
	./serve_models.sh

build:
    docker-compose build

up:
    docker-compose up backend

start:
	python3 main.py


stop:
	torchserve --stop
