import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = Service(executable_path="D:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Create new account").click()
month_dd = driver.find_element(By.ID,"month")
sel = Select(month_dd)
time.sleep(5)
sel.select_by_visible_text("Aug")
time.sleep(5)
sel.select_by_value("12")
time.sleep(5)
sel.select_by_index(3)
time.sleep(10)