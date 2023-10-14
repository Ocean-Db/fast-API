# Setup virtual environment

###### [Install poetry](https://python-poetry.org/docs/#installation) first

cd into cloned repository, then run

```
poetry init
poetry update
```

###### Install pre-commit hooks

```
sudo apt install pre-commit
```

```
pre-commit install
```

###### Run backend with command

```
uvicorn app.main:app --host 0.0.0.0 --port 80
```
