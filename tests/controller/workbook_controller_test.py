import logging
from unittest import mock

import pytest
from fastapi.testclient import TestClient

from domain.workbook import Workbook
from main import app
from service.iworkbook_repository import WorkbookNotFoundError
from usecase.student_usecase_workbook import StudentUseCaseWorkbook

logger = logging.getLogger(__name__)


@pytest.fixture
def client():
    yield TestClient(app)


def test_get_workbook_200(client):
    student_usecase_workbook_mock = mock.Mock(spec=StudentUseCaseWorkbook)
    student_usecase_workbook_mock.find_workbook_by_id.return_value = Workbook(name='test', lang2='ja')

    with app.container.student_usecase_workbook.override(student_usecase_workbook_mock):
        response = client.get("/1")

    assert response.status_code == 200
    resp_json = response.json()
    logger.info("{}".format(resp_json))
    assert 'test' == resp_json['name']
    assert 'ja' == resp_json['lang2']


def test_get_workbook_404(client):
    student_usecase_workbook_mock = mock.Mock(spec=StudentUseCaseWorkbook)
    student_usecase_workbook_mock.find_workbook_by_id.side_effect = WorkbookNotFoundError(key='id', value='1000')

    with app.container.student_usecase_workbook.override(student_usecase_workbook_mock):
        response = client.get("/1")

    assert response.status_code == 404
