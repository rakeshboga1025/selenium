from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button=driver.find_element(By.XPATH, "//span[.='right click me']")
act=ActionChains(driver)
act.context_click(button).perform()