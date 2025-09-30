import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///D:/26th%20July%202025/Html%20Files/Tagname.html")
time.sleep(2)
driver.find_element(By.TAG_NAME,"input").send_keys("abc")
time.sleep(2)
driver.find_element(By.TAG_NAME,"input").send_keys("xyz")
time.sleep(10)

