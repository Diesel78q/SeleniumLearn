import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

def test_full_smoke_test_functionality(driver):
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

    # Begin testing the product information page
    """Product #1 Information"""
    
    # Find the name of product #1 and store it in a variable
    product_1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    value_product_1 = product_1.text
    print(value_product_1)
    
    # Find the price of product #1 and store it in a variable
    product_1_price = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
    value_product_1_price = product_1_price.text
    print(value_product_1_price)
    
    # Select product #1 and add it to the cart
    select_product_1 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    select_product_1.click()
    print('Select product #1')
    
    # Click the cart button to view the cart
    cart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart.click()
    print('Click cart button')
    
    # Verify that the product information matches in the cart
    """Cart Product #1 Information"""
    
    # Find the name of the product in the cart
    cart_product_1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    value_cart_product_1 = cart_product_1.text
    print(value_cart_product_1)
    assert value_product_1 == value_cart_product_1
    print('Name accepted')
    
    # Find the price of the product in the cart
    cart_product_1_price = driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
    value_cart_product_1_price = cart_product_1_price.text
    print(value_cart_product_1_price)
    assert value_product_1_price == value_cart_product_1_price
    print('Price accepted')
    
    # Proceed to the checkout page
    checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
    checkout.click()
    print('Click checkout')
    
    # Fill in user information for checkout
    """User Information"""
    
    # Input the first name
    first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
    first_name.send_keys('John')
    print('Input first name')
    
    # Input the last name
    last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
    last_name.send_keys('Smith')
    print('Input last name')
    
    # Input the postal code
    postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
    postal_code.send_keys('420')
    print('Input postal code')
    
    # Continue to the next step of the checkout
    continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_button.click()
    print('Click continue button')
    
    # Verify that the product information matches on the final page
    """Finish Product #1 Information"""
    
    # Find the name of the product on the final page
    finish_cart_product_1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    finish_value_cart_product_1 = finish_cart_product_1.text
    print(finish_value_cart_product_1)
    assert value_product_1 == finish_value_cart_product_1
    print('Name accepted #2')
    
    # Find the price of the product on the final page
    finish_cart_product_1_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')
    finish_value_cart_product_1_price = finish_cart_product_1_price.text
    print(finish_value_cart_product_1_price)
    assert value_product_1_price == finish_value_cart_product_1_price
    print('Price accepted #2')
    
    # Verify the total summary price
    summary_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
    value_summary_price = summary_price.text
    print(value_summary_price)
    item_total = "Item total: " + finish_value_cart_product_1_price
    print(item_total)
    assert value_summary_price == item_total
    print('Total summary price accepted')
