.PHONY: run isort black test flake8

format: isort black

run:
	poetry run
	#uvicorn cocotola_api_fast.main:app --reload

isort:
	isort -rc .

black:
	black

flake8:
	flake8 cocotola_py_api

test:
	poetry run pytest --cov=cocotola_py_api --cov-branch --cov-report=html

docker-build:
	docker build --file docker/Dockerfile -t cocotola-fast-api .

docker-run:
	docker run -p 8000:8000 cocotola-fast-api
