#implicitly_wait, explicitly wait
#implicitly wait --> driver can wait for a particular
# time to load all the web elements in to the page
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.find_element(By.NAME,"firstname").send_keys("Rajesh")
driver.find_element(By.NAME,"lastname").send_keys("K")
driver.find_element(By.NAME,"reg_email__").send_keys('Rajesh@gmail.com')
driver.find_element(By.NAME,"reg_email_confirmation__").send_keys("Rajesh@gmail.com")
driver.find_element(By.NAME,"reg_passwd__").send_keys('admin123')
