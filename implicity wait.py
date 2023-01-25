from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(10)

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME, "q")
searchbox.send_keys("selenium")

searchbox.submit()

driver.find_element(By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']").click()
