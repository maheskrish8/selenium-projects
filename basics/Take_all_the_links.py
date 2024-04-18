from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

s = Options()
s.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=s)
driver.get("http://www.rediff.com")
driver.maximize_window()
driver.implicitly_wait(30)
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))

'''for i in links:
    print(i.text)'''

for i in links:
    print(i.text, "--->", i.get_attribute("href"))