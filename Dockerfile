# Be aware that you need to specify these arguments before the first FROM
# see: https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact
ARG BASE_IMAGE=pfeiffermax/python-poetry:1.7.0-poetry1.6.1-python3.11.6-slim-bookworm
FROM ${BASE_IMAGE} as dependencies-build-stage
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
# install [tool.poetry.dependencies]
# this will install virtual environment into /.venv because of POETRY_VIRTUALENVS_IN_PROJECT=true
# see: https://python-poetry.org/docs/configuration/#virtualenvsin-project
COPY ./pyproject.toml /application_root/
WORKDIR /application_root/
RUN poetry install --no-interaction --no-root --without dev

FROM ${BASE_IMAGE} as production-image

# Copy virtual environment
COPY --chown=python_application:python_application --from=dependencies-build-stage /application_root/.venv /application_root/.venv

# Copy application files
COPY --chown=python_application:python_application /app /application_root/app/
