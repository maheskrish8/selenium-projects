from selenium import webdriver
from selenium.webdriver.chrome.options import Options

s= Options()
s.add_experimental_option("detach",True)
s.add_argument("--disable-notifications")
driver= webdriver.Chrome(options=s)
driver.get("https://www.justdial.com/")
driver.maximize_window()
driver.implicitly_wait(35)