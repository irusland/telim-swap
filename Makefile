ENV_FILE = env/env.env

include ${ENV_FILE}
$(eval export $(shell sed -ne 's/ *#.*$$//; /./ s/=.*$$// p' ${ENV_FILE}))


install:
	python3 -m venv .venv
	poetry install

start:
	python3 src/main.py

stop:
	echo stop
