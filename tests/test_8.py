import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

def test_button_interactions_and_message_verification(driver):
    """
    Test interaction with buttons and verification of associated messages.
    Args:
        driver (WebDriver): The Selenium WebDriver instance.
    """
    # Define the base URL
    base_url = "https://demoqa.com/buttons"
    
    # Navigate to the base URL and maximize the window
    driver.get(base_url)
    driver.maximize_window()

    # Find and perform a double-click action on the 'Double Click' button
    action = ActionChains(driver)
    double_click_button = driver.find_element(By.XPATH, '//*[@id="doubleClickBtn"]')
    action.double_click(double_click_button).perform()
    print('Performed a double click on the button')
    
    # Verify the message after double-click
    double_click_message = driver.find_element(By.XPATH, '//*[@id="doubleClickMessage"]')
    result = double_click_message.text
    assert result == 'You have done a double click'
    print('Double click action verified')
    
    # Find and perform a right-click action on the 'Right Click' button
    right_click_button = driver.find_element(By.XPATH, '//*[@id="rightClickBtn"]')
    action.context_click(right_click_button).perform()
    print('Performed a right click on the button')
    
    # Verify the message after right-click
    right_click_message = driver.find_element(By.XPATH, '//*[@id="rightClickMessage"]')
    result = right_click_message.text
    assert result == 'You have done a right click'
    print('Right click action verified')

