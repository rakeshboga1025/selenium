from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)
#driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("10/09/2001")

year="2001"
month="august"
date="10"

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

while True:
    mon=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        #driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click() #Next arrow

        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click() #previous arrow

#select date
dates=driver.find_elements(By.XPATH, "//div[id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break


