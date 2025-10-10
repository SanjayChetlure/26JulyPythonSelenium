import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.mobikwik.com/")
time.sleep(2)

#click on login btn
driver.find_element(By.XPATH,"(//span[text()='Login'])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("999999")
time.sleep(5)