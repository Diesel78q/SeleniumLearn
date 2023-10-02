import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_successful_login_navigation_and_url_verification(driver):
    # Define the base URL
    base_url = "https://www.saucedemo.com/"
    
    # Navigate to the base URL and maximize the window
    driver.get(base_url)
    driver.maximize_window()

    # Define login credentials
    login_standard_user = "standard_user"
    password_all = "secret_sauce"

    # Find the username field and input the username
    username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    username.send_keys(login_standard_user)
    print("Input login")

    # Find the password field and input the password
    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.send_keys(password_all)
    print("Input password")

    # Find and click the login button
    button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    button_login.click()
    print("Click login button")
    
    # Find and click the menu button
    menu = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
    menu.click()
    print('Click menu button')
    
    # Pause for 5 seconds to allow the menu to expand
    time.sleep(5)
    
    # Find and click the 'About' link
    link_about = driver.find_element(By.XPATH, '//*[@id="about_sidebar_link"]')
    link_about.click()
    print("Click about button")
    
    # Define the expected URL after clicking 'About'
    default_url = 'https://saucelabs.com/'
    
    # Get the current URL
    get_url = driver.current_url
    print(get_url)
    
    # Assert that the current URL matches the expected URL
    assert default_url == get_url
    print("URL is as expected")
    
    # Navigate back to the previous page
    driver.back()
    print('Go back')
    
    # Pause for 2 seconds
    time.sleep(2)
    
    # Navigate forward to the 'About' page
    driver.forward()
    print('Go forward')
