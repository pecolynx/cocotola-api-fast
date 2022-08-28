import logging

import uvicorn
from fastapi import FastAPI

from config.container import Container
from controller import translation_controller, workbook_controller
from domain.workbook import Workbook
from gateway.workbook_repository import WorkbookDBEntity
from log.app_logger_formatter import CustomFormatter
from log.uvicorn_log_config import UVICORN_LOG_CONFIG

formatter = CustomFormatter('%(asctime)s')
log_handler = logging.StreamHandler()
log_handler.setFormatter(formatter)

logging.basicConfig(handlers=[log_handler], level=logging.INFO)

logger = logging.getLogger(__name__)

# sqlalchemy.engine.Engine
sql_logger = logging.getLogger('sqlalchemy.engine.Engine')
sql_logger.handlers.clear()
sql_logger.propagate = False
sql_logger.addHandler(log_handler)
sql_logger.setLevel(logging.INFO)


def create_app() -> FastAPI:
    fastapi = FastAPI()
    fastapi.include_router(translation_controller.router)
    fastapi.include_router(workbook_controller.router)
    fastapi.container = Container()
    db = fastapi.container.db()
    db.create_database()
    # session=
    # session.query(WorkbookDBEntity).all()

    with db.session() as session:
        # session.add(WorkbookDBEntity(name='hiro'))
        # session.commit()
        logger.info([x.name for x in session.query(WorkbookDBEntity).all()])
        session.commit()

    return fastapi


app: FastAPI = create_app()

workbook: Workbook = Workbook(name='test',lang2='ja')


# workbook.name = 'hello'


# logger.info("INFO")


@app.get("/")
async def root():
    return {"message": "Hello World"}


def main():
    # logger.info("Server started listening on port: 8000")
    uvicorn.run("cocotola_api_fast.main:app", host="0.0.0.0", port=8000, reload=True,
                log_config=UVICORN_LOG_CONFIG)


if __name__ == "__main__":
    main()
