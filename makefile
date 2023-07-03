install:
	python -m pip install -U pip && \
	pip install -r requirements.txt \
	pwd \
	export PYTHONPATH=.
lint:
	pylint --disable=R,C api
tests:
	python -m pytest -vv --cov=api.tests
format:
	black .

all: install lint tests format