SHELL := /bin/bash


install_dev:
	pip3 install -r requirements/requirements.dev.txt

test:
	python -m pytest tests/test*.py
