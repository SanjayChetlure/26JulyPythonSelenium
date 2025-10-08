import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
time.sleep(2)

try:
    result = driver.find_element(By.XPATH, "//img[@class='fb_logo _8ilh img']").is_displayed()
    print(result)
    print("Element Present")
except:
    print("Element not present")
