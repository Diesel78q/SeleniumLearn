import pytest
from selenium import webdriver
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(2)
    driver.quit()
