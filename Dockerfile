# https://snyk.io/blog/best-practices-containerizing-python-docker/

FROM python:3.11-alpine


WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /app .

ENV USER=docker
ENV UID=12345
ENV GID=23456

RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup "$USER" \
    --no-create-home \
    --uid "$UID" \
    "$USER"


USER docker
