from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#Locators matching with single element
element=driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
element.send_keys("Apple MacBook Pro 13-inch")

#Locators matching with multiple elements
elements=driver.find_elements(By.XPATH, "//div[@class='footer-upper']//a")
print(len(elements)) # 22