import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/r.php?entry_point=login")
time.sleep(2)

month=driver.find_element(By.XPATH,"//select[@id='month']")
s1=Select(month)

result=s1.is_multiple
print(result)

if result:
    print("S2_Listbox is of multi selectable")
else:
    print("S2_Listbox is of single selectable")

