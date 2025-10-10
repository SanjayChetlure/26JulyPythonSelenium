import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/delete_customer.php")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@name='cusid']").send_keys("123")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='submit']").click()


#get text from alert popup
textValue=driver.switch_to.alert.text
print(textValue)

#click on cancel btn from alert popup
# driver.switch_to.alert.dismiss()

#click on OK btn from 1st alert popup
driver.switch_to.alert.accept()

#click on OK btn from 2nd alert popup
driver.switch_to.alert.accept()


time.sleep(10)