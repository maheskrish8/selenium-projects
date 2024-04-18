from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

o=Options()
o.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=o)
driver.get("https://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Create new account").click()
driver.find_element(By.NAME,"firstname").send_keys("krish")
act=ActionChains(driver)
act.send_keys(Keys.TAB).send_keys("veni").send_keys(Keys.TAB).send_keys("mahes098@gmail.com").send_keys(Keys.TAB).send_keys("yjdo989").perform()

