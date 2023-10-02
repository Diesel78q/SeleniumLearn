import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_radio_button_interaction_and_choice_verification(driver):
    # Define the base URL
    base_url = "https://demoqa.com/radio-button"
    
    # Navigate to the base URL and maximize the window
    driver.get(base_url)
    driver.maximize_window()

    # Find and click the 'Radio Button' menu item
    radio_button_menu = driver.find_element(By.XPATH, '//*[@id="item-2"]')
    radio_button_menu.click()
    print('Click radio button menu')
    
    # Find and click the 'Yes' radio button
    choose_radio_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label')
    choose_radio_button.click()
    print('Click yes')
    
    # Pause for 5 seconds to allow the choice to be confirmed
    time.sleep(5)
    
    # Find the element that displays the current choice
    chek_if_you_choose_yes = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/p/span')
    
    # Get the text of the current choice
    current_choice = chek_if_you_choose_yes.text
    
    # Assert that the current choice is 'Yes'
    assert current_choice == 'Yes'
    print('Test accepted')
