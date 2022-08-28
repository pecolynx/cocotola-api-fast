from abc import ABC, abstractmethod

from service.iworkbook_repository import IWorkbookRepository


class IRepositoryFactory(ABC):
    @abstractmethod
    def new_workbook_repository(self) -> IWorkbookRepository:
        pass
