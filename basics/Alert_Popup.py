import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Ser = Service(executable_path="D:\\SeleniumDrivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=Ser)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()
#driver.find_element(By.NAME,"proceed").click()
driver.find_element(By.XPATH,"//input[@title='Sign in']").click()
time.sleep(5)
alt = driver.switch_to.alert
alert_text = alt.text
print(alert_text)
alt.accept()
time.sleep(5)
