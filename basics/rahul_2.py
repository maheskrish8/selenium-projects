from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

o=Options()
o.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=o)
driver.get("https://www.google.com/search?q=rahul+shetty+qa+click+academy&oq=rahul+shetty+qa+click+academy&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTIxODc1ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8")
driver.implicitly_wait(30)
driver.find_element(By.LINK_TEXT,"Practice Page").click()
driver.find_element(By.ID,"autocomplete").send_keys("india")
option1=driver.find_element(By.ID,"dropdown-class-example")



