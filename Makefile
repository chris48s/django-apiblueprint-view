.PHONY: help build-drafter format install lint test

help:
	@grep '^\.PHONY' Makefile | cut -d' ' -f2- | tr ' ' '\n'

build-drafter:
	./build-drafter.sh

format:
	poetry run isort .
	poetry run black .

install:
	poetry install

lint:
	poetry run isort -c --diff .
	poetry run black --check .
	poetry run flake8 .

test:
	poetry run coverage run --source=apiblueprint_view --omit=apiblueprint_view/tests/*.py ./run_tests.py
	poetry run coverage report
	poetry run coverage xml
