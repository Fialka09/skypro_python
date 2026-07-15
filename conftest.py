import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def pytest_configure(config):
    config.addinivalue_line("markers", "edge: тесты для браузера Edge")
    config.addinivalue_line("markers", "chrome: тесты для браузера Chrome")
    config.addinivalue_line("markers", "firefox: тесты для браузера Firefox")


@pytest.fixture
def edge_driver():
    """Фикстура для браузера Edge."""
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def chrome_driver():
    """Фикстура для браузера Chrome."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    """Фикстура для браузера Firefox."""
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()