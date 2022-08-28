# cocotola-api-fast

```
source ./venv/bin/activate
```

```shell
make flake8
```

```shell
docker build --file docker/Dockerfile -t cocotola-fast-api .
```

```shell
docker run 
```

```shell
# poetry new cocotola-py-api
# cd cocotola-py-api
poetry add pyproject-flake8 --dev
poetry add black --dev
poetry add mypy --dev
poetry add pytest --dev
poetry add pytest-cov --dev
poetry add fastapi
poetry add uvicorn
poetry add gunicorn
poetry add sqlalchemy
# poetry add flask
## poetry add flask-restplus
# poetry add flasgger
# poetry add marshmallow
# poetry add apispec
# poetry add apispec_webframeworks
```
