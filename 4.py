from selenium.webdriver.chrome.service import service
from selenium.webdriver.common.by import By
from selenium import webdriver

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")


driver.get("https://www.google.co.in/")
driver.maximize_window()