import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

# driver.find_element(By.XPATH,"//button[contains(text(),'Log')]").click()
# driver.find_element(By.XPATH,"//a[contains(text(),'Forgotten')]").click()
driver.find_element(By.XPATH,"//a[contains(text(),'account')]").click()
time.sleep(10)
