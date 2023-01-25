from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

