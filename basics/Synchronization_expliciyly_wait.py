#Explicitly wait --> driver can wait for a particular
# time to load specific web element into the webpage

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = Options()
opt.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=opt)
driver.get("http://www.fb.com")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Create new account").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME,"firstname"))).send_keys("Rajesh")

driver.find_element(By.NAME,"lastname").send_keys("K")
driver.find_element(By.NAME,"reg_email__").send_keys('Rajesh@gmail.com')
driver.find_element(By.NAME,"reg_email_confirmation__").send_keys("Rajesh@gmail.com")
driver.find_element(By.NAME,"reg_passwd__").send_keys('admin123')
