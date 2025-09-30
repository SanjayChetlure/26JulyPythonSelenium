import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("file:///D:/26th%20July%202025/Html%20Files/LinkText_PartialLinkText.html")
time.sleep(2)
# driver.find_element(By.LINK_TEXT,"facebook").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"face").click()

time.sleep(10)

