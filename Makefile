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
	[ ! -d logs ] && mkdir logs; \
	. .venv/bin/activate; \
	export FLASK_ENV=development; \
	python3 simple_app.py

prod:
	[ ! -d logs ] && mkdir logs; \
	. .venv/bin/activate; \
	export FLASK_ENV=production; \
	python3 simple_app.py

db_upgrade:
	[ ! -d logs ] && mkdir logs; \
	[ ! -d migrations/versions ] && mkdir migrations/versions; \
	. .venv/bin/activate; \
	export FLASK_ENV=development; \
	export FLASK_APP=simple_app.py; \
	flask db migrate; \
	flask db upgrade

db_downgrade:
	[ ! -d logs ] && mkdir logs; \
	[ ! -d migrations/versions ] && mkdir migrations/versions; \
	. .venv/bin/activate; \
	export FLASK_ENV=development; \
	export FLASK_APP=simple_app.py; \
	flask db downgrade

all: clean install dev
