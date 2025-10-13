import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://skpatro.github.io/demo/links/")
time.sleep(2)

#click on newTab from main page
driver.find_element(By.XPATH,"//input[@name='NewTab']").click()

#get Address of main page & child window
ls=driver.window_handles         #[addressOfMainPage[0], addressOfChildWindow[1]]
mainWindowAddress=ls[0]
childWindowAddress=ls[1]


#switch to child window
driver.switch_to.window(childWindowAddress)

time.sleep(2)
#click on Training link from child window
driver.find_element(By.XPATH,"(//span[text()='Training'])[1]").click()

time.sleep(10)