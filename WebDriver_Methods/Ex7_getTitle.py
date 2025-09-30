import time
from selenium import webdriver

driver=webdriver.Chrome()
time.sleep(3)
driver.get("https://www.facebook.com/")
titleValue=driver.title
print(titleValue)

# print(driver.title)
