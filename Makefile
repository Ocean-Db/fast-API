build:
	docker build . --progress=plain --no-cache

linting:
	pre-commit run -a

test:
	PYTHONPATH=${PYTHONPATH}:./app pytest
