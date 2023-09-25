# Setup virtual environment

[Install poetry](https://python-poetry.org/docs/#installation) first

cd into cloned repository, then run

```
poetry init
poetry update
```

Run backend with command

```
uvicorn main:app --host 0.0.0.0 --port 80
```
