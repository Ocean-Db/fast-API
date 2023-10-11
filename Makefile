build:
	docker build . --progress=plain --no-cache

linting:
	pre-commit run -a

test:
	PYTHONPATH=${PYTHONPATH}:./app poetry run pytest --doctest-modules --junitxml=junit/test-results.xml --cov=com --cov-report=xml --cov-report=html
