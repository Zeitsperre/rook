from tests.common import get_tests_project_base_dir
from unittest import mock
import pytest


@pytest.fixture(scope="session", autouse=True)
def mock_base_dirs():
    with mock.patch(
        "daops.utils.consolidate.get_project_base_dir", side_effect=get_tests_project_base_dir
    ):
        yield