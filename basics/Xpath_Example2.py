import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Ser = Service(executable_path="D:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=Ser)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
time.sleep(3)

# contains attribute
cna1 = driver.find_element(By.XPATH, "//a[contains(@id,'_0_0')]").text
print(cna1)
time.sleep(5)

#starts-with attribute
cna2 = driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0')]").text
print(cna2)
time.sleep(5)