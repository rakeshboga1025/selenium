from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_comditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException

import time

mywait=WebDriverWait(driver,10)

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME, "q")
searchbox.send_keys("selenium")

searchbox.submit()

searchlink=mywait.until(EC.presence_of_element_located(By.XPATH, "//h3[@class='LC20lb MBeuO DKV0Md']"))
searchlink.click()