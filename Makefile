.ONESHELL:

.PHONY: clean install dev prod all

clean:
	rm -rf .venv
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

install:
	[ ! -d .venv ] && python3 -m venv .venv; \
	. .venv/bin/activate; \
	pip3 install -r requirements.txt;

dev:
	. .venv/bin/activate; \
	export FLASK_ENV=development; \
	python3 simple_app.py

prod:
	. .venv/bin/activate; \
	export FLASK_ENV=production; \
	python3 simple_app.py

all: clean install dev
