import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")
time.sleep(2)


#switch to frame
# frameElement=driver.find_element(By.XPATH,"//iframe[@id='iframeResult']")
# driver.switch_to.frame(frameElement)           #using frame webElement

# driver.switch_to.frame(0)             #using frame Index

driver.switch_to.frame("iframeResult")         #using frame name/id

#click on date & time btn
driver.find_element(By.XPATH,"//button[contains(text(),'Click')]").click()
time.sleep(10)
