import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

driver.find_element(By.XPATH,"//input[contains(@class,'inputtext')]").send_keys("abc")
driver.find_element(By.XPATH,"//input[contains(@class,'6luy _9npi')]").send_keys("xyz")
time.sleep(10)