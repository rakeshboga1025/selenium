from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
act=ActionChains(driver)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

min_slider=driver.find_element(By.XPATH, "//div[@id='slider']")

print(min_slider.location) #{'x': 825, 'y': 1376}

act.drag_and_drop_by_offset(min_slider,50,0).perform()

print("Location of slider after sliding..... ")
