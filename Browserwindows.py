from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()

#windowid=driver.current_window_handle
#print(windowid)

