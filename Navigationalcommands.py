from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.com/")

driver.back()
driver.forward()

driver.refresh()

driver.quit()