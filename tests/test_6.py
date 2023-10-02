import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def test_login(driver):
    base_url = "https://demoqa.com/"
    driver.get(base_url)
    driver.maximize_window()

    elements_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[2]')
    elements_button.click()
    print('Click elements button')
    
    check_box = driver.find_element(By.XPATH, '//*[@id="item-1"]/span')
    check_box.click()
    print('Click check box')
    time.sleep(5)
    
    expand_all = driver.find_element(By.XPATH, '//*[@id="tree-node"]/div/button[1]')
    expand_all.click()