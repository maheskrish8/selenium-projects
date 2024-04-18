from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
o=Options()
o.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=o)
driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.implicitly_wait(30)
job_ele=driver.find_element(By.XPATH,"//a[@title='Search Jobs']")
act=ActionChains(driver)
act.move_to_element(job_ele).perform()