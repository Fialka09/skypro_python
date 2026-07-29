import pytest
from project_api import ProjectAPI


def pytest_configure(config):
    config.addinivalue_line("markers", "positive: позитивные тесты")
    config.addinivalue_line("markers", "negative: негативные тесты")


@pytest.fixture(scope="function")
def api():
    """Фикстура: авторизованный API-клиент."""
    project = ProjectAPI()
    project.auth()
    return project
