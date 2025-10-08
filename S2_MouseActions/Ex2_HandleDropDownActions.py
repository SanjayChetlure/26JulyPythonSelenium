import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(2)

login=driver.find_element(By.XPATH,"//span[text()='Login']")

act=ActionChains(driver)

act.move_to_element(login).perform()

time.sleep(5)
driver.find_element(By.XPATH,"//li[text()='Rewards']").click()

time.sleep(5)