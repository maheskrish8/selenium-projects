from selenium import webdriver
from selenium.webdriver.edge.options import Options

s=Options()
s.add_argument("--disable-notifications")
s.add_experimental_option("detach",True)
driver= webdriver.Edge(options=s)
driver.get("https://www.justdial.com/")
driver.maximize_window()
driver.implicitly_wait(35)
driver.ti