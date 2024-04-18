import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
opt=Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.rediff.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Create Account").click()
driver.find_element(By.XPATH,"//input[starts-with(@name,'name')]").send_keys("mahes")

