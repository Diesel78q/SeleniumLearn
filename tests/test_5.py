import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def test_login(driver):
    base_url = "https://www.saucedemo.com/"
    driver.get(base_url)
    driver.maximize_window()

    login_standard_user = "standard_user"
    password_all = "secret_sauce"

    username = driver.find_element(
        By.XPATH, '//*[@id="user-name"]'
    )  # Most useful, by XPATH
    username.send_keys(login_standard_user)
    print("Input login")

    password = driver.find_element(By.CSS_SELECTOR, "#password")  # By CSS selector
    password.send_keys(password_all)
    print("Input password")

    button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    button_login.click()
    print("Click login button")
    
    menu = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
    menu.click()
    print('Click menu button')
    time.sleep(5)
    
    link_about = driver.find_element(By.XPATH, '//*[@id="about_sidebar_link"]')
    link_about.click()
    print("Click about button")
    
    default_url = 'https://saucelabs.com/'
    get_url = driver.current_url
    print(get_url)
    assert default_url == get_url
    print("Url actual")
    
    driver.back()
    print('Go back')
    time.sleep(2)
    driver.forward()
    print('Go forward')