import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service(executable_path="D:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.fb.com")
driver.maximize_window()
driver.save_screenshot("C:\\Users\\pc\\Desktop\\Demo\\fb1.png")
time.sleep(5)