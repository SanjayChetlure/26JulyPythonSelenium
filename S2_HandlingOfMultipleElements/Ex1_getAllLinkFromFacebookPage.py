import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

allLinksAddress=driver.find_elements(By.XPATH,"//a")

print(len(allLinksAddress))

for eachLinkAddress in allLinksAddress:
    textValue=eachLinkAddress.text
    print(textValue)