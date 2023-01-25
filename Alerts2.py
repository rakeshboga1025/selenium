from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#open alert window
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
alertwindow=driver.switch_to.alert


print(alertwindow.text)
alertwindow.send_keys("welcome")
time.sleep(5)
alertwindow.accept()