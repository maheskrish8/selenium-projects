import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service(executable_path="D:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.rediff.com")
driver.maximize_window()
time.sleep(5)
height = driver.execute_script("document.documentElement.scrollHeight")
print(height)
driver.execute_script("window.scroll(0,2000)")
time.sleep(5)
driver.execute_script("window.scroll(0,-2000)")
time.sleep(5)