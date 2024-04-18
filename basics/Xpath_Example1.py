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

# single attribute
driver.find_element(By.XPATH,"//input[@data-testid='royal_email']").send_keys("PythonSelenium")
time.sleep(5)


#text() function

cna_tf = driver.find_element(By.XPATH,"//a[text()='Create new account']").text
print(cna_tf)

#contains text():

cna_ctf = driver.find_element(By.XPATH,"//a[contains(text(),'acc')]").text

print(cna_ctf)

#starts-with text():

cna_swtf = driver.find_element(By.XPATH, "//a[starts-with(text(),'Create n')]").text

print(cna_swtf)

time.sleep(5)

#Single attribute

driver.find_element(By.XPATH,"//a[@data-testid='open-registration-form-button']").click()

time.sleep(5)

# text() function

heading = driver.find_element(By.XPATH,"//div[text()='Sign Up']").text

print(heading)

#Multiple attribute

driver.find_element(By.XPATH,"//input[@class='_8esa'][@value='2']").click()
time.sleep(5)