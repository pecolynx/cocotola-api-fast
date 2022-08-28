from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import Session

from domain.workbook import Workbook
from gateway.database import Base
from service.iworkbook_repository import IWorkbookRepository


class WorkbookNotFoundError(Exception):
    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value


class WorkbookDBEntity(Base):
    __tablename__ = "workbook"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

    def to_model(self) -> Workbook:
        return Workbook(name=self.name)


class WorkbookRepository(IWorkbookRepository):
    def __init__(self, session: Session):
        self.__session = session

    def add_workbook(self, workbook: Workbook) -> None:
        workbook_entity: WorkbookDBEntity = WorkbookDBEntity(name=workbook.name)
        self.__session.add(workbook_entity)

    def find_workbook_by_id(self, workbook_id: int) -> Workbook:
        # workbook = self.__session.query(WorkbookDBEntity).filter(WorkbookDBEntity.id == workbook_id).first()
        workbook_entity: WorkbookDBEntity = self.__session.query(WorkbookDBEntity) \
            .filter(WorkbookDBEntity.id == workbook_id).first()
        # workbook = Workbook('hello')
        if workbook_entity is None:
            raise WorkbookNotFoundError('id', str(workbook_id))
        return workbook_entity.to_model()
