from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
driver.get("https://www.fb.com")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Create new account").click()

female_radio = driver.find_element(By.XPATH,"//input[starts-with(@id,'u_')][@value='1']")

e1 = female_radio.is_selected()
print("Female radio button Select =", e1)

female_radio.click()

e2 = female_radio.is_selected()
print("After clicking female radio button Select =", e2)

e3 = female_radio.is_enabled()
print("Female radio button Enable =", e3)

e4 = female_radio.is_displayed()
print("Female radio button Display =", e4)