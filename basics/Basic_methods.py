import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service(executable_path='D:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('http://www.google.com')
driver.maximize_window()
time.sleep(5)
driver.get('http://www.fb.com')
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)
actual_title = driver.title
print(actual_title)
actual_url = driver.current_url
print(actual_url)