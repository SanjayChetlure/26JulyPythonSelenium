import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

#capture SS of specific element
logo=driver.find_element(By.XPATH,"//img[@class='fb_logo _8ilh img']")
logo.screenshot("D:\\26th July 2025\\Selenium\\Screenshots\\abc.png")


#capture SS of complete webpage
driver.save_screenshot("D:\\26th July 2025\\Selenium\\Screenshots\\xyz.png")