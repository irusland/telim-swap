ENV_FILE = .env

include ${ENV_FILE}
$(eval export $(shell sed -ne 's/ *#.*$$//; /./ s/=.*$$// p' ${ENV_FILE}))


install:
	poetry install

build:
	docker build --tag base:linux -f docker/base.dockerfile --platform linux/x86_64 .
	docker build --tag telim-swap_torchserve:linux -f docker/net-api.dockerfile --platform linux/x86_64 .
	docker build --tag telim-swap_backend:linux -f docker/backend.dockerfile --platform linux/x86_64 .

tag:
	docker tag telim-swap_torchserve:linux irusland/telim-swap_torchserve:linux
	docker tag telim-swap_backend:linux irusland/telim-swap_backend:linux

push:
	docker push irusland/telim-swap_torchserve:linux
	docker push irusland/telim-swap_backend:linux

up:
	docker-compose up backend

start:
	python3 main.py

serve:
	./serve_models.sh

stop:
	torchserve --stop
