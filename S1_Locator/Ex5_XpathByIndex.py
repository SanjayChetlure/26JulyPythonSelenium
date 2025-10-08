import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/r.php?entry_point=login")
time.sleep(2)


#enter FN
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("abc")
time.sleep(5)

#enter surname
driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("xyz")
time.sleep(5)

#mobile num
driver.find_element(By.XPATH,"(//input[@type='text'])[5]").send_keys("xyz")
time.sleep(5)
