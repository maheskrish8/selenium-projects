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
driver.find_element(By.XPATH,"html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("PythonSelenium")
driver.find_element(By.XPATH,"html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div/div[2]/div/input").send_keys("password123")
f1 = driver.find_element(By.XPATH,"html/body/div/div/div/div/div/div/div/h2").text
print(f1)
time.sleep(10)