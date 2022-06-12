install:
	python3 -m venv .venv
	poetry install

start:
	python3 src/main.py

stop:
	echo stop
