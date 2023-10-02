import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(2)
    driver.quit()