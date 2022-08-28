import logging

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()
logger = logging.getLogger(__name__)


class TranslationFindParameter(BaseModel):
    letter: str = Field(..., example="a", min_length=1, max_length=1)
    lang2: str = Field(..., example="ja", min_length=2, max_length=2)


class TranslationFindResponse(BaseModel):
    lang2: str = Field(..., example="ja")


@router.post('/find', response_model=TranslationFindResponse, tags=["translation"])
def find_translations(body: TranslationFindParameter):
    """Example endpoint returning a list of colors by palette
       This is using docstrings for specifications.
    """

    logger.info("find_translations")
    lang2 = body.lang2
    letter = body.letter

    return TranslationFindResponse(lang2=lang2)
