from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#click an link
#driver.find_element(By.LINK_TEXT, "Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

#Find no of links in a page
links=driver.find_elements(By.TAG_NAME, 'a')
print("total number of links:", len(links)) #90

#print all the link names

 for link in links:
     print(link.text)