from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

o=Options()
o.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=o)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa?src=gain_lose")
driver.maximize_window()
driver.implicitly_wait(30)
#single column
single_column=driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[6]/td[1]").text
print(single_column)
#single_row
row6=driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[6]").text
print(row6)
#entire table
allrows=driver.find_elements(By.XPATH,"//table[@class='dataTable']/tbody/tr")
for i in allrows:
    print(i.text)

