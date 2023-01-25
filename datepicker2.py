from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

#date of birth
driver.find_element(By.XPATH, "//input[@id='dob']").click()
datepicker_month=Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
datepicker_month.select_by_visible_text("Dec")

datepicker_year=Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
datepicker_year.select_by_visible_text("1994")

alldates=driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for date in alldates:
    if date.text=="25":
        date.click()
        berak
