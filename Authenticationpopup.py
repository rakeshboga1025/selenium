from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver.get("https://the-internet.herokuapp.com/basic_auth")

driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()

