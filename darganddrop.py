from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
act=ActionChains(driver)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

boxx_ele=driver.find_element(By.XPATH, "//p[normalize-space()='Drag me to my target']")
box_ele=driver.find_element(By.XPATH, "//div[@id='droppable']")

act.drag_and_drop(boxx_ele,box_ele).perform()