import logging
import traceback

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import BaseModel, Field

from config.container import Container
from domain.workbook import Workbook
from service.iworkbook_repository import WorkbookNotFoundError
from service.iworkbook_repository import WorkbookAddParameter
from usecase.student_usecase_workbook import StudentUseCaseWorkbook

router = APIRouter()
logger = logging.getLogger(__name__)


class WorkbookResponseHTTPEntity(BaseModel):
    name: str = Field(..., example='workbook')
    lang2: str = Field(..., example='ja')


class WorkbookAddParameterHTTPEntity(BaseModel):
    name: str = Field(..., min_length=1, max_length=20)
    lang2: str = Field(..., min_lengh=2, max_length=2, example="ja")


@router.get('/{workbook_id}', response_model=WorkbookResponseHTTPEntity, tags=["Workbook"])
@inject
def get_workbook(
        workbook_id: int,
        student_usecase_workbook: StudentUseCaseWorkbook = Depends(Provide[Container.student_usecase_workbook])
):
    logger.info('get_workbook')
    operator_id = 1
    try:
        workbook: Workbook = student_usecase_workbook.find_workbook_by_id(operator_id, workbook_id)
        workbook_http_entity = WorkbookResponseHTTPEntity(name=workbook.name, lang2=workbook.lang2)
        return workbook_http_entity
    except WorkbookNotFoundError as e:
        raise HTTPException(status_code=404, detail="item_not_found")
    except Exception as e:
        logger.error(str(e))
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail='internal server error')


@router.post('/', tags=["Workbook"], responses={204: {"model": None}})
@inject
def add_workbook(
        body: WorkbookAddParameterHTTPEntity,
        student_usecase_workbook: StudentUseCaseWorkbook = Depends(Provide[Container.student_usecase_workbook])
):
    logger.info('add_workbook')
    operator_id = 1
    try:
        workbook_add_parameter = WorkbookAddParameter(name=body.name)
        student_usecase_workbook.add_workbook(operator_id, workbook_add_parameter)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        logger.error(str(e))
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail='internal server error')


@router.get('/abc/def', response_model=WorkbookResponseHTTPEntity, tags=["Workbook"])
def abc_def():
    logger.info('abc_def')
    return {"lang2": "hello"}
