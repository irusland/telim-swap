ENV_FILE = .env/dev.env

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

start:
	python3 main.py


stop:
	torchserve --stop
