import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(2)

act=ActionChains(driver)

targetEle=driver.find_element(By.XPATH,"//a[text()='Terms']")
act.scroll_to_element(targetEle).perform()

time.sleep(5)

