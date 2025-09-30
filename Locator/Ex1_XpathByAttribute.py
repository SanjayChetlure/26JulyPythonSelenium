import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)
# driver.find_element(locatorType)

#enter UN
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("abcd")

#enter pwd
driver.find_element(By.XPATH,"//input[@class='inputtext _55r1 _6luy _9npi']").send_keys("xyz")

#click on login btn
driver.find_element(By.XPATH,"//button[@name='login']").click()


time.sleep(5)
