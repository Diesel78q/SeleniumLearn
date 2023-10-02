import pytest
from selenium.webdriver.common.by import By

def test_failed_login_with_invalid_credentials(driver):
    # Define the base URL
    base_url = 'https://www.saucedemo.com/'
    
    # Navigate to the base URL
    driver.get(base_url)
    driver.maximize_window()

    # Define incorrect login credentials
    login_standard_user = 'standard_use'  # Typo in username
    password_all = 'secret_sauce'

    # Find the username field and input the incorrect username
    username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    username.send_keys(login_standard_user)
    print('Input login')

    # Find the password field and input the correct password
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys(password_all)
    print('Input password')

    # Find and click the login button
    button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    button_login.click()
    print('Click login button')

    # Find the warning text indicating incorrect login
    warning_text = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    
    # Get the text from the element
    value_warning_text = warning_text.text
    
    # Assert that the warning text is as expected
    assert value_warning_text == 'Epic sadface: Username and password do not match any user in this service'
    print('Test accepted')
