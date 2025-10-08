import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("file:///D:/26th%20July%202025/Selenium/Html%20files/S2_Listbox.html")
time.sleep(2)

element=driver.find_element(By.XPATH,"//select[@id='1234']")
s1=Select(element)

result=s1.is_multiple
print(result)

if result:
    print("S2_Listbox is of multi selectable")
else:
    print("S2_Listbox is of single selectable")

