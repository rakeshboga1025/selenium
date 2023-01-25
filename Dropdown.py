from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

#drpcountry_ele=driver.find_element(By.XPATH, "//select[@id='input-country']")
drpcountry=Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))

#select option from the dropdown
#drpcountry.select_by_visible_text("India")
#country=drpcountry.select_by_value("10")

#capture all the options and print them
alloptions=drpcountry.options
print("total number of options:" ,len(alloptions))

for opt in alloptions:
    print(opt.text)

#select option from dropdown without using built-in method
for opt in alloptions:
    if opt.text=="India":
        opt.click()
        break