from selenium import webdriver
from selenium.webdriver.firefox.service import Service

s = Service(executable_path='D:\\SeleniumDrivers\\geckodriver-v0.33.0-win64\\geckodriver.exe')
driver = webdriver.Firefox(service= s)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.minimize_window()
driver.maximize_window()
driver.close()