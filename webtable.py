from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

noOfRows=len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
noOfColumns=len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th"))

print(noOfColumns) #4
print(noOfRows) #7

#Read specific row & column data-Master in selenium
data=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(data)

#Read specific row & column data
print("Printing all throws and column data  data.........")

for r in range(2,noOfRows+1):
    for c in range(1,noOfColumns+1):
        data=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data)