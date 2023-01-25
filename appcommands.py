from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

print(driver.title) #OrangeHRM
print(driver.current_url) #https://opensource-demo.orangehrmlive.com/
print(driver.page_source)

driver.quit()