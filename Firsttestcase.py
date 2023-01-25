from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

act_title=driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
    print("Test case is passed")

else:
    print("Test case is failed")

driver.close()