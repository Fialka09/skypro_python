import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def pytest_configure(config):
    config.addinivalue_line("markers", "firefox: тесты для Firefox")


@pytest.fixture
def firefox_driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
