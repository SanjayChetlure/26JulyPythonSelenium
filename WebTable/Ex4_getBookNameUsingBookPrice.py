import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///D:/26th%20July%202025/Selenium/Html%20files/Sample3.html")
time.sleep(2)

value=driver.find_element(By.XPATH,"//table[@id='1234']//tr//td[text()='100']//parent::tr/td[2]").text
print(value)