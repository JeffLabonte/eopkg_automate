SHELL := /bin/bash


install_dev:
	pip3 install -r requirements/requirements.dev.txt

test:
	python -m pytest tests/test*.py

codestyle:
	flake8

format:
	black **/*.py --exclude .git/ --exclude .venv --line-length 120
