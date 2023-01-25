from selenium import webdriver

from selenium.webdriver.common.by import By

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.gps-coordinates.net/my-location")
driver.maximize_window()


