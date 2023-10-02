import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_checkbox_interaction_and_directory_verification(driver):
    # Define the base URL
    base_url = "https://demoqa.com/"
    
    # Navigate to the base URL and maximize the window
    driver.get(base_url)
    driver.maximize_window()

    # Find and click the 'Elements' button
    elements_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[2]')
    elements_button.click()
    print('Click elements button')
    
    # Find and click the 'Check Box' option
    check_box = driver.find_element(By.XPATH, '//*[@id="item-1"]/span')
    check_box.click()
    print('Click check box')
    
    # Pause for 5 seconds to allow the tree to expand
    time.sleep(5)
    
    # Find and click the 'Expand All' button
    expand_all = driver.find_element(By.XPATH, '//*[@id="tree-node"]/div/button[1]')
    expand_all.click()
    
    # Find the last directory name in the tree
    last_directory_name = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[3]/span/label/span[3]')
    
    # Get the text of the last directory name
    current_last_directory_name = last_directory_name.text
    
    # Assert that the current last directory name is 'Downloads'
    assert current_last_directory_name == 'Downloads'
    print('Test accepted')
