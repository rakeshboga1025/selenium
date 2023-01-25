from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver.get("https://demo.nopcommerce.com/")
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

# is displayed()
searchbox=driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Display status:",searchbox.is_displayed()) #true

# is enabled()
print("Display status:", searchbox.is_enabled()) #true

# is selected() - for radio buttons and check boxes
rd_male=driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH, "//input[@id='gender-female']")

# print ( default status for radio buttons )
print(rd_male.is_selected()) # false
print(rd_female.is_selected()) #false

#rd_male.click()

# print ( after selecting male radio buttons )
#print(rd_male.is_selected()) # true
#print(rd_female.is_selected()) # false

rd_female.click()
print(rd_male.is_selected()) # False
print(rd_female.is_selected()) #True







#driver.close()

