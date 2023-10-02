import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import datetime
import os
import time
from selenium.webdriver import ActionChains


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

    url = "https://www.saucedemo.com/inventory.html"
    get_url = driver.current_url
    print(get_url)
    assert url == get_url
    print("Url actual")

    text_products = driver.find_element(
        By.XPATH, '//*[@id="header_container"]/div[2]/span'
    )
    value_text_products = text_products.text
    print(value_text_products)
    assert value_text_products == "Products"
    print("products passed")

    # driver.execute_script("window.scrollTo(0, 600)")
    action = ActionChains(driver)
    T_shirt = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]')
    action.move_to_element(T_shirt).perform()
    time.sleep(5)

    now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
    name_screenshot = "screenshot" + now_date + ".png"
    folder_path = (
        "C:\\Users\\danii\\Python Automation\\selenium\\SeleniumLearn\\Screens"
    )
    screenshot_path = os.path.join(folder_path, name_screenshot)
    driver.save_screenshot(screenshot_path)
