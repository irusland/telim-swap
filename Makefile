ENV_FILE = .env

include ${ENV_FILE}
$(eval export $(shell sed -ne 's/ *#.*$$//; /./ s/=.*$$// p' ${ENV_FILE}))


install:
	poetry install

build:
	docker build --progress=plain --tag base:linux -f docker/base.dockerfile --platform linux/x86_64 .
	docker build --progress=plain --tag telim-swap_torchserve:linux -f docker/net-api.dockerfile --platform linux/x86_64 .
	docker build --progress=plain --tag telim-swap_backend:linux -f docker/backend.dockerfile --platform linux/x86_64 .

tag:
	docker tag telim-swap_torchserve:linux irusland/telim-swap_torchserve:linux
	docker tag telim-swap_backend:linux irusland/telim-swap_backend:linux

push:
	docker push irusland/telim-swap_torchserve:linux
	docker push irusland/telim-swap_backend:linux

make run:
	docker run -d --env-file .env --restart on-failure --network="host" irusland/telim-swap_backend:linux
	docker run -d --restart on-failure -p 127.0.0.1:8080:8080 --network="host" --memory="4g" irusland/telim-swap_torchserve:linux

up:
	docker-compose up backend

start:
	python3 main.py

serve:
	./serve_models.sh

stop:
	torchserve --stop
