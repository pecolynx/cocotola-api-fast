import logging
import traceback

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from container import Container
from domain.workbook import Workbook
from gateway.workbook_repository import WorkbookNotFoundError
from usecase.student_usecase_workbook import StudentUseCaseWorkbook

router = APIRouter()
logger = logging.getLogger(__name__)


class WorkbookResponse(BaseModel):
    lang2: str = Field(..., example="ja")


@router.get('/{workbook_id}', response_model=WorkbookResponse, tags=["Workbook"])
@inject
def get_workbook(
        workbook_id,
        student_usecase_workbook: StudentUseCaseWorkbook = Depends(Provide[Container.student_usecase_workbook])
):
    logger.info('get_workbook')
    operator_id = 1
    try:
        workbook: Workbook = student_usecase_workbook.find_workbook_by_id(operator_id, workbook_id)
        return {"lang2": workbook.name}
    except WorkbookNotFoundError as e:
        raise HTTPException(status_code=404, detail="item_not_found")
    except Exception as e:
        logger.error(str(e))
        logger.error(traceback.format_exc())


@router.get('/abc/def', response_model=WorkbookResponse, tags=["Workbook"])
def abc_def():
    logger.info('abc_def')
    return {"lang2": "hello"}
