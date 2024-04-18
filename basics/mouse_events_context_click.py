from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
o=Options()
o.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=o)
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
driver.implicitly_wait(30)
ele=driver.find_element(By.XPATH,"//span[text()='right click me']")
act=ActionChains(driver)
act.context_click(ele).perform()
