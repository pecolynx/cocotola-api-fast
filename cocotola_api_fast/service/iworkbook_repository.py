from abc import ABC, abstractmethod

from pydantic import BaseModel, Field

from domain.workbook import Workbook


class WorkbookAddParameter(BaseModel):
    name: str = Field(..., min_length=1, max_length=20)
    #
    # def __init__(self, name: str):
    #     self.name = name


class IWorkbookRepository(ABC):
    @abstractmethod
    def find_workbook_by_id(self, workbook_id: int) -> Workbook:
        pass

    @abstractmethod
    def add_workbook(self, workbook_add_param: WorkbookAddParameter) -> None:
        pass
