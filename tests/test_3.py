from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time

def test_successful_login_and_filter_selection(driver):
    # Define the base URL
    base_url = 'https://www.saucedemo.com/'
    
    # Navigate to the base URL and maximize the window
    driver.get(base_url)
    driver.maximize_window()

    # Define login credentials
    login_standard_user = 'standard_user'
    password_all = 'secret_sauce'

    # Find the username field and input the username
    username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    username.send_keys(login_standard_user)
    print('Input login')

    # Find the password field and input the password
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys(password_all)
    print('Input password')

    # Simulate pressing the 'Enter' key to submit the form
    password.send_keys(Keys.RETURN)
    
    # Find and click the filter element
    filter = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    filter.click()
    print('Click filter')
    
    # Pause for 5 seconds to allow the filter options to load
    time.sleep(5)
    
    # Use the 'DOWN' key to navigate through filter options
    filter.send_keys(Keys.DOWN)
    
    # Pause for 5 seconds to allow the selection to update
    time.sleep(5)
    
    # Use the 'RETURN' key to confirm the selection
    filter.send_keys(Keys.RETURN)
