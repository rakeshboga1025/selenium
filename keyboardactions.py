#ctrl+A
#ctrl+c
#tab
#ctrl+v


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains, Keys

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
act=ActionChains(driver)
driver.maximize_window()

driver.get("https://text-compare.com/")

input1=driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

input1.send_keys("welcome to selenium")

#input1---- ctrl+A select the text

act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#input1-----ctrl+c copy text

act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#press Tab keys to Navigate to input--2

act.send_keys(Keys.TAB)
act.perform()
act.send_keys(Keys.TAB).perform()

#input2 ctrl+v pree the text

act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()