from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()
# or
#driver.find_element(By.XPATH, "//input[@id='search_query_topor' or @ name='search_query' ]").send_keys("T-shirts")
#driver.find_element(By.XPATH, "//button[@type='submit' or @ name='submit_search']").click()

# and
#driver.find_element(By.XPATH, "//button[@type='submit' and @ class='btn btn-default button-search']").click()

# contains
#driver.find_element(By.XPATH, "//input[contains(@id,'search_query_top')]").send_keys("T-shirts")

#start-with
#driver.find_element(By.XPATH, "//button[starts-with(@name, 'submit_')]").click()

#text
driver.find_element(By.XPATH, "//a[text()='women']").click()