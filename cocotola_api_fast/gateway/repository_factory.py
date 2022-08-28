from sqlalchemy.orm import Session

from gateway.workbook_repository import WorkbookRepository
from service.irepository_factory import IRepositoryFactory, IWorkbookRepository


class RepositoryFactory(IRepositoryFactory):
    def __init__(self, session: Session):
        self.__session = session

    def new_workbook_repository(self) -> IWorkbookRepository:
        return WorkbookRepository(self.__session)
