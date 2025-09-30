import time
from selenium import webdriver

driver=webdriver.Chrome()
time.sleep(3)
driver.get("https://www.facebook.com/")
time.sleep(3)
driver.fullscreen_window()
time.sleep(3)