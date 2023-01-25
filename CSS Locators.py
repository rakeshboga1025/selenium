from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/")

#tag & id combination
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")

#tag & class combination
#driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc")

#tag attribute
#driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("abc")

#tag class attribute
#driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass").send_keys("abcd")
