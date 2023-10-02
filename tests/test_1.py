import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import datetime
import os
from selenium.webdriver.remote.webdriver import WebDriver

def test_successful_login_and_screenshot(driver):
    # Define the base URL
    base_url = "https://www.saucedemo.com/"
    
    # Navigate to the base URL
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

    # Define the expected URL after login
    url = "https://www.saucedemo.com/inventory.html"
    
    # Get the current URL
    get_url = driver.current_url
    print(get_url)
    
    # Assert that the current URL matches the expected URL
    assert url == get_url
    print("URL is as expected")

    # Find the text indicating successful login
    text_products = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    
    # Get the text from the element
    value_text_products = text_products.text
    print(value_text_products)
    
    # Assert that the text indicates successful login
    assert value_text_products == "Products"
    print("Login successful, products page displayed")

    # Get the current date and time for creating a screenshot file name
    now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
    
    # Define the file name for the screenshot
    name_screenshot = "screenshot" + now_date + ".png"
    
    # Define the folder path for saving the screenshot
    folder_path = "C:\\Users\\danii\\Python Automation\\selenium\\SeleniumLearn\\Screens"
    
    # Create the full path for the screenshot file
    screenshot_path = os.path.join(folder_path, name_screenshot)
    
    # Save the screenshot
    driver.save_screenshot(screenshot_path)
