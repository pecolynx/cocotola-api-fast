from abc import ABC, abstractmethod

from domain.workbook import Workbook


class IWorkbookRepository(ABC):
    @abstractmethod
    def find_workbook_by_id(self, workbook_id: int) -> Workbook:
        pass
