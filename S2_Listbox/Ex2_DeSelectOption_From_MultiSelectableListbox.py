import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("file:///D:/26th%20July%202025/Selenium/Html%20files/S2_Listbox.html")
time.sleep(2)

element=driver.find_element(By.XPATH,"//select[@id='1234']")

s1=Select(element)

s1.select_by_index(1)
s1.select_by_index(2)
s1.select_by_index(3)
time.sleep(2)

# s1.deselect_by_index(1)
# s1.deselect_by_visible_text("Aus")
# # s1.deselect_by_value()

s1.deselect_all()


time.sleep(10)