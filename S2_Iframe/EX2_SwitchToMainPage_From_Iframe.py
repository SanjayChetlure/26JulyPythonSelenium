import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_myfirst")
time.sleep(2)

#switch to frame
driver.switch_to.frame("iframeResult")         #using frame name/id

#click on date & time btn
driver.find_element(By.XPATH,"//button[contains(text(),'Click')]").click()


#switch to main page
driver.switch_to.default_content()
# driver.switch_to.parent_frame()

#click on Open Menu link from main page
driver.find_element(By.XPATH,"//a[@id='menuButton']").click()



time.sleep(10)
