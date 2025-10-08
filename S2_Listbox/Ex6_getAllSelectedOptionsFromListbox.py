import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("file:///D:/26th%20July%202025/Selenium/Html%20files/S2_Listbox.html")

UN=driver.find_element(By.XPATH,"//select[@id='1234']")
s=Select(UN)

allSOptionsAddress=s.options     #[1stOptionWebElement, 2ndOptionWebElement,3rdOptionWebElement]

for eachOptioAddress in allSOptionsAddress:
    print(eachOptioAddress.text)



time.sleep(10)