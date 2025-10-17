import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@class='Pke_EE']").send_keys("redmi 12 5g")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='_2iLD__']").click()
time.sleep(5)

textValue=driver.find_element(By.XPATH,"((//div[@class='tUxRFH'])[1]//span)[7]").text
print(textValue)