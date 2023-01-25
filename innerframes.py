from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[.='Iframe with in an Iframe']").click()

outerframe=driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe=driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcome")

#driver.switch_to.parent_frame()  #directly switch to parent frame(outer frame)
