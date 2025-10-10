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

#switch to alert
alt=driver.switch_to.alert


#get text from alert popup
textValue=alt.text
print(textValue)

#click on cancel btn from alert popup
# alt.dismiss()

#click on OK btn from 1st alert popup
alt.accept()

#click on OK btn from 2nd alert popup
alt.accept()

#enter input in alert popup
# alt.send_keys("")

time.sleep(10)