from dependency_injector import containers, providers
import logging
from gateway.database import Database
from gateway.repository_factory import RepositoryFactory
from usecase.student_usecase_workbook import StudentUseCaseWorkbook

logger = logging.getLogger(__name__)


def repository_factory_func(session):
    return RepositoryFactory(session)


class Container(containers.DeclarativeContainer):
    logger.info("Container")
    wiring_config = containers.WiringConfiguration(packages=["controller"])

    # config = providers.Configuration(yaml_files=["config.yml"])

    # engine = create_engine('sqlite:///:memory:', echo=False)
    db = providers.Singleton(Database, db_url='sqlite:///sample_db.sqlite3')

    student_usecase_workbook = providers.Factory(
        StudentUseCaseWorkbook,
        session_factory=db.provided.session,
        repository_factory_func=repository_factory_func,
    )
