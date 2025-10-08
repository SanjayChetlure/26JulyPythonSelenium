import time
from selenium import webdriver

driver=webdriver.Chrome()
time.sleep(3)
driver.get("https://www.facebook.com/")
urlValue=driver.current_url
print(urlValue)

print(driver.current_url)
