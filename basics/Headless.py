import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

opt = Options()
opt.add_argument("--headless")
s = Service(executable_path="D:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service= s, options=opt)
driver.get("http://www.google.com")
driver.maximize_window()
actual_title = driver.title
print(actual_title)
actual_url = driver.current_url
print(actual_url)
time.sleep(5)
driver.close()