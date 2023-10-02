import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_handle_button_exceptions_and_verify_message(driver):
    # Define the base URL
    base_url = "https://demoqa.com/dynamic-properties"
    
    # Navigate to the base URL and maximize the window
    driver.get(base_url)
    driver.maximize_window()

    try:
        # Try to find and click the visible button
        visible_button = driver.find_element(By.XPATH, '//*[@id="visibleAfter"]')
        visible_button.click()

    except NoSuchElementException as exception:
        # Handle the NoSuchElementException by waiting and trying again
        print('NoSuchElementException')
        time.sleep(6)
        visible_button = driver.find_element(By.XPATH, '//*[@id="visibleAfter"]')
        visible_button.click()
        print('Click visible button')


