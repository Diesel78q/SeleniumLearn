from selenium import webdriver
import time
import random
from fake_useragent import UserAgent

# url = "https://www.instagram.com/"
# user_agents_list = [
#     
# ]

# Change useragent
useragent = UserAgent()



# Options
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
driver = webdriver.Chrome(
    options=options
)
# Set proxy
options.add_argument()

try:
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
    time.sleep(5)


except Exception as ex:
    print(ex)


finally:
    driver.close()
    driver.quit()
