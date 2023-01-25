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

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

#scroll down by pixel:
#driver.execute_script("window.scrollBy(0,3000)","")
#value=driver.execute_script("return window.pageYoffset;")
#print("Number of pixels moved:",value)

#scroll down page till the element is visible
#flag=driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
#driver.execute_script("arguments[0].scrollIntoView();",flag)
#value=driver.execute_script("return widow.pageYoffset;")
#print("Number of pixels moved:",value)

#scroll down page till end
#driver.execute_script(("window.scrollBy(0,document.body.scrollHeight)")
#value=driver.execute_script("return window.pageYoffset;")
#print("Number of pixels moved:",value)

#scrollup to starting position
driver.execute_script(("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYoffset;")
print("Number of pixels moved:",value)
