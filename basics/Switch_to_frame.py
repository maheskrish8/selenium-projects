from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

t = Options()
t.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=t)
driver.get("https://www.rediff.com")
driver.maximize_window()
driver.implicitly_wait(30)
actual_text1 = driver.find_element(By.CLASS_NAME,"mailicon").text
print(actual_text1)

#driver.switch_to.frame("moneyiframe") # by id or name 3 ways
#driver.switch_to.frame(0) # by index

f1 = driver.find_element(By.XPATH,"//iframe[@title='Rediff Money Widget']")
driver.switch_to.frame(f1)

text2 = driver.find_element(By.XPATH,"//span[text()='BSE']").text
print(text2)

driver.switch_to.default_content() # 1 way

text3 = driver.find_element(By.LINK_TEXT,"Money").text
print(text3)
