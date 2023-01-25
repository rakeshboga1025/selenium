from selenium import webdriver

from selenium.webdriver.common.by import By

driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get('http://automationpractice.com/index.php')

driver.maximize_window()

#driver.find_element(By.ID, "search_query_top").send_keys("T-shirts")
#driver.find_element(By.NAME, "submit_search").click()

#driver.find_element(By.LINK_TEXT, "Printed Chiffon Dress").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Chiffon Dress").click()

sliders=driver.find_elements(By.CLASS_NAME, "homeslider-container")
print(len(sliders))

links=driver.find_elements(By.TAG_NAME, "a")
print(len(links))