import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

#Apr1
# driver.find_element(By.XPATH,"//input[@name='email']").send_keys("abc")

#Apr2
UN=driver.find_element(By.XPATH,"//input[@name='email']")
UN.send_keys("abc")



time.sleep(10)