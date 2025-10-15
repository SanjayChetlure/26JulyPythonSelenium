import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
time.sleep(2)

driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("redmi")
time.sleep(5)

allOptionsAddress=driver.find_elements(By.XPATH,"(//ul[@class='G43f7e'])[1]/li//div[@class='wM6W7d']")

expText="redmi 15 5g"

for eachOptionAddress in allOptionsAddress:
    actText=eachOptionAddress.text       #redmi note 14
    # if actText==expText:
    if actText.__eq__(expText):
        eachOptionAddress.click()
        break


time.sleep(10)
