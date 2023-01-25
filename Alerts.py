from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@value='Login']").click()
time.sleep(5)
myalert=driver.switch_to.alert
myalert.accept()

