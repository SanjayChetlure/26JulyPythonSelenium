import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()


driver.get("file:///D:/26th%20July%202025/Html%20Files/MultipleCheckboxes.html")
time.sleep(2)

allCheckboxesAddress=driver.find_elements(By.XPATH,"//input[@type='checkbox']")

#select checkboxes in forward direct
for eachCheckboxAddres in allCheckboxesAddress:
    eachCheckboxAddres.click()
    time.sleep(1)


#De-Select checkboxes in reverse direct
for eachCheckboxAddres in reversed(allCheckboxesAddress):
    eachCheckboxAddres.click()
    time.sleep(1)