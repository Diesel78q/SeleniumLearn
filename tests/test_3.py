from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
import time

def test_login(driver):
    base_url = 'https://www.saucedemo.com/'
    driver.get(base_url)
    driver.maximize_window()

    login_standard_user = 'standard_user'
    password_all = 'secret_sauce'

    username = driver.find_element(
        By.XPATH, '//*[@id="user-name"]')  # Most useful, by XPATH
    username.send_keys(login_standard_user)
    print('Input login')
    username.send_keys(Keys.BACKSPACE)
    time.sleep(5)
    username.send_keys(Keys.BACKSPACE)
    time.sleep(5)
    

    # password = driver.find_element(By.CSS_SELECTOR, '#password')  # By CSS selector
    # password.send_keys(password_all)
    # print('Input password')

    # button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    # button_login.click()
    # print('Click login button')
