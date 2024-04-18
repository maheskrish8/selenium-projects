from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

o=Options()
o.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=o)
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.switch_to.frame(0)
first_ele=driver.find_element(By.ID,"draggable")
sec_ele=driver.find_element(By.ID,"droppable")
act=ActionChains(driver)
act.drag_and_drop(first_ele,sec_ele).perform()

