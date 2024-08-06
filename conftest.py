import pytest
from selenium import webdriver


@pytest.fixture
def driver_setup():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
