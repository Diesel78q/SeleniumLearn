import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains

def test_change_price_slider_position(driver):
    # Define the base URL
    base_url = "http://www.automationpractice.pl/index.php?id_category=3&controller=category#"
    
    # Navigate to the base URL
    driver.get(base_url)
    
    # Maximize the browser window
    driver.maximize_window()

    # Create an ActionChains instance for performing actions
    action = ActionChains(driver)
    
    # Find the price slider element using its XPath
    price = driver.find_element(By.XPATH, '//*[@id="layered_price_slider"]')
    
    # Click, hold, move, and release the price slider to change its position
    action.click_and_hold(price).move_by_offset(12, 0).release().perform()
    
    # Print a message to indicate that the price-slider position has been changed
    print("Change position of price-slider")
