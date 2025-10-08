import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/r.php?entry_point=login")
time.sleep(2)


#Step1- identify listbox
month=driver.find_element(By.XPATH,"//select[@id='month']")

#Step2: Create object of select with webElement object as a input
s1=Select(month)

#step3: call select class methods
# s1.select_by_visible_text("Dec")               #String text
# s1.select_by_value("3")                          #String value
s1.select_by_index(3)                    #int index
time.sleep(10)