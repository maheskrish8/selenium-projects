import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Ser = Service(executable_path="D:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=Ser)
driver.get("http://www.fb.com")
driver.maximize_window()
time.sleep(3)

#id

driver.find_element(By.ID, "email").send_keys("pythonselenium")

#name
driver.find_element(By.NAME, "pass").send_keys("Javaselenium")

#class name
f1 = driver.find_element(By.CLASS_NAME, "_8eso").text

print(f1)

#link text
f2 = driver.find_element(By.LINK_TEXT, "Forgotten password?").text
print(f2)

#partial link text
f3 = driver.find_element(By.PARTIAL_LINK_TEXT,"got").text
print(f3)

time.sleep(10)