import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

# driver.find_element(By.XPATH,"//button[text()='Log in']").click()
# driver.find_element(By.XPATH,"//a[text()='Forgotten password?']").click()
driver.find_element(By.XPATH,"//a[text()='Create new account']").click()
time.sleep(10)