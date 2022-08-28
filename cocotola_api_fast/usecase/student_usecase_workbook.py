import logging

from domain.workbook import Workbook
from service.iworkbook_repository import IWorkbookRepository
from service.iworkbook_repository import WorkbookAddParameter

logger = logging.getLogger(__name__)


class StudentUseCaseWorkbook(object):
    def __init__(self, session_factory, repository_factory_func) -> None:
        self._session_factory = session_factory
        self._repository_factory_func = repository_factory_func

    def find_workbook_by_id(self, operator_id: int, workbook_id: int) -> Workbook:
        logger.info('find_workbook_by_id')
        with self._session_factory() as session:
            rf = self._repository_factory_func(session)
            workbook_repo: IWorkbookRepository = rf.new_workbook_repository()
            workbook: Workbook = workbook_repo.find_workbook_by_id(workbook_id)
            session.commit()
            return workbook

    def add_workbook(self, operator_id: int, workbook_add_param: WorkbookAddParameter) -> None:
        with self._session_factory() as session:
            rf = self._repository_factory_func(session)
            workbook_repo: IWorkbookRepository = rf.new_workbook_repository()
            workbook_repo.add_workbook(workbook_add_param)
            session.commit()
