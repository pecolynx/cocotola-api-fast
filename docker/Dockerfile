FROM python:3.8-slim-buster as builder

WORKDIR /opt/app

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.15

RUN python -m venv venv
# RUN source venv/bin/activate
RUN pip install "poetry==$POETRY_VERSION"
COPY poetry.lock pyproject.toml ./
RUN cat ./poetry.lock
RUN poetry config virtualenvs.create false \
   && poetry install --no-dev
RUN ls /usr/local/bin
RUN ls /usr/local/lib/python3.8/site-packages/
RUN which gunicorn

# FROM python:3.8-slim-buster as runner

RUN useradd -r -s /bin/false uvicornuser
WORKDIR /opt/app
# COPY --from=builder /opt/app/venv /opt/app/venv
# COPY --from=builder-base /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY cocotola_api_fast ./cocotola_api_fast
USER uvicornuser
WORKDIR /opt/app/cocotola_api_fast

EXPOSE 8000
CMD ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "--capture-output", "--log-level", "warning", "--access-logfile", "-", "--bind", ":8000", "main:app"]
