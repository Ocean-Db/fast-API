# Be aware that you need to specify these arguments before the first FROM
# see: https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact
ARG BASE_IMAGE=pfeiffermax/python-poetry:1.7.0-poetry1.6.1-python3.11.6-slim-bookworm
FROM ${BASE_IMAGE} as dependencies-build-stage
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# install [tool.poetry.dependencies]
# this will install virtual environment into /.venv because of POETRY_VIRTUALENVS_IN_PROJECT=true
# see: https://python-poetry.org/docs/configuration/#virtualenvsin-project
WORKDIR /application_root/
COPY ./pyproject.toml /application_root/
RUN poetry install --no-interaction --no-root --without dev

FROM ${BASE_IMAGE} as production-image

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser
USER appuser
WORKDIR /application_root/
COPY --chown=appuser:appuser --from=dependencies-build-stage /application_root/pyproject.toml /application_root/
# Copy virtual environment
COPY --chown=appuser:appuser --from=dependencies-build-stage /application_root/.venv /application_root/.venv
# Copy application files
COPY --chown=appuser:appuser /app /application_root/app/

ENTRYPOINT ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000","--forwarded-allow-ips='*'"]
