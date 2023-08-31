from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Define the link to the website
link = "https://rozetka.com.ua/ua/"

# Initialize the Chrome WebDriver
browser = webdriver.Chrome()
browser.get(link)

# Find the search input field and enter the search query "Мебель"
search_string = browser.find_element(
    By.XPATH, "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/div/div[1]/input")
search_string.send_keys("Мебель")

# Find the search button and click it
button = browser.find_element(
    By.XPATH, "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/div/form/button").click()

# Wait for a moment to let the page load
time.sleep(3)

# Check the text of the main heading on the search results page
check_item1 = browser.find_element(
    By.XPATH, "/html/body/app-root/div/div/rz-super-portal/div/main/section/div[1]/h1").text

# Define the expected heading text
check_item2 = "Меблі"

# Compare the actual and expected heading text
if check_item1 == check_item2:
    print("Test accepted")
else:
    print("Test failed")

# Close the browser
browser.quit()
