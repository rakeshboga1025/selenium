from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/login/")
driver.maximize_window()

#Login

driver.find_element(By.XPATH, "//input[@aria-label='Email address or phone number']").send_keys("Admin")