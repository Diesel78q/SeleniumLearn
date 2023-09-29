import pytest
from selenium.webdriver.common.by import By

def test_login(driver):
    base_url = 'https://www.saucedemo.com/'
    driver.get(base_url)
    driver.maximize_window()

    login_standard_user = 'standard_use'
    password_all = 'secret_sauce'

    username = driver.find_element(By.XPATH, '//*[@id="user-name"]')  # Most useful, by XPATH
    username.send_keys(login_standard_user)
    print('Input login')

    password = driver.find_element(By.CSS_SELECTOR, '#password')  # By CSS selector
    password.send_keys(password_all)
    print('Input password')

    button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    button_login.click()
    print('Click login button')

    warring_text = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    value_warring_text = warring_text.text
    assert value_warring_text == 'Epic sadface: Username and password do not match any user in this service'
    print('Test accepted')
