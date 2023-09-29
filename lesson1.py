from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
# username = driver.find_element(By.ID,'user-name')#By ID
# username = driver.find_element(By.NAME,'user-name')#By name
username = driver.find_element(By.XPATH,'//*[@id="user-name"]')#Most useful , by XPATH
username.send_keys('standard_user')
password = driver.find_element(By.CSS_SELECTOR,'#password')#By CSS selector
password.send_keys('secret_sauce')
button_login = driver.find_element(By.XPATH,'//*[@id="login-button"]')
button_login.click()




# time.sleep(10)
# driver.close()