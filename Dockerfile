# https://snyk.io/blog/best-practices-containerizing-python-docker/

FROM python:3.11-alpine


WORKDIR /app
COPY /app .
COPY pyproject.toml .

RUN pip install poetry
RUN poetry install --no-interaction --no-ansi --no-cache --no-root --no-directory --only main

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

ENTRYPOINT ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
