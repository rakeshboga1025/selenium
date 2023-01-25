from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to.default_content()#go back to main page

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to.default_content()#go back to main page

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "//div[@class='topNav']//ul[@title='Navigation']//li//a[@href='help-doc.html'][normalize-space()='Help").click()

