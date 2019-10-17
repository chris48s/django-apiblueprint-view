# django-apiblueprint-view

This project uses:

* [poetry](https://poetry.eustace.io/) for dependency management
* [flake8](https://pypi.org/project/flake8/) for linting and
* [black](https://github.com/psf/black) for code formatting
* [isort](https://github.com/timothycrosley/isort) for import sorting

Development Tasks:

* Install dependencies: `poetry install`
* Run the test suite: `./run_tests.py`
* Sort imports: `isort **/*.py`
* Run lint checks: `flake8 .`
* Auto-format: `black .`
