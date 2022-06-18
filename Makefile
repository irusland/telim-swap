ENV_FILE = .env/dev.env

include ${ENV_FILE}
$(eval export $(shell sed -ne 's/ *#.*$$//; /./ s/=.*$$// p' ${ENV_FILE}))


install:
	poetry install

start:
	python3 main.py

stop:
	echo stop
