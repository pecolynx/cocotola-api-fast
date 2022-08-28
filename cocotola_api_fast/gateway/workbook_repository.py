from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import Session

from domain.workbook import Workbook
from gateway.database import Base
from service.iworkbook_repository import IWorkbookRepository, WorkbookAddParameter
from service.iworkbook_repository import WorkbookNotFoundError


class WorkbookDBEntity(Base):
    __tablename__ = "workbook"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    lang2 = Column(Text, nullable=False)

    def to_model(self) -> Workbook:
        return Workbook(name=self.name, lang2=self.lang2)


class WorkbookRepository(IWorkbookRepository):
    def __init__(self, session: Session):
        self.__session = session

    def find_workbook_by_id(self, workbook_id: int) -> Workbook:
        # workbook = self.__session.query(WorkbookDBEntity).filter(WorkbookDBEntity.id == workbook_id).first()
        workbook_entity: WorkbookDBEntity = self.__session.query(WorkbookDBEntity) \
            .filter(WorkbookDBEntity.id == workbook_id).first()
        if workbook_entity is None:
            raise WorkbookNotFoundError('id', str(workbook_id))
        return workbook_entity.to_model()

    def add_workbook(self, workbook_add_param: WorkbookAddParameter) -> None:
        workbook_entity = WorkbookDBEntity(name=workbook_add_param.name, lang2=workbook_add_param.lang2)
        self.__session.add(workbook_entity)
