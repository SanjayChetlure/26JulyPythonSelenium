import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("file:///D:/26th%20July%202025/Selenium/Html%20files/S2_Listbox.html")

UN=driver.find_element(By.XPATH,"//select[@id='1234']")
s=Select(UN)

s.select_by_index(0)
s.select_by_index(1)
s.select_by_index(2)


allSelectedOptionsAddress=s.all_selected_options     #[1stOptionWebElement, 2ndOptionWebElement,3rdOptionWebElement]

for eachOptioAddress in allSelectedOptionsAddress:
    print(eachOptioAddress.text)



time.sleep(10)