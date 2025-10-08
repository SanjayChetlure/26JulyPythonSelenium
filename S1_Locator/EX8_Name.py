import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///D:/26th%20July%202025/Html%20Files/Name.html")
time.sleep(2)
driver.find_element(By.NAME,"abc123").send_keys("abc")
time.sleep(2)
driver.find_element(By.NAME,"abc123").send_keys("xyz")
time.sleep(10)

