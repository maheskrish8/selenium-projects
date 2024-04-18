from selenium import webdriver
from selenium.webdriver.common.by import By

from data_driven_framework import XL_Reader

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(30)
path="C:\\Users\\care\\Desktop\\ddf.xlsx"
rows=XL_Reader.total_Rows(path,"Sheet3")
for r in range(2,rows+1):
    username=XL_Reader.read_Data(path,"Sheet3",r,1)
    pwd=XL_Reader.read_Data(path,"Sheet3",r,2)
    driver.find_element(By.NAME,"username").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(pwd)
    driver.find_element(By.XPATH,"//button[normalize-space(text()='Login')]").click()
    act=driver.title
    if act=="OrangeHRM":
        XL_Reader.write_Data(path,"Sheet3",r,3,"pass")
        driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()

    else :
        XL_Reader.write_Data(path,"Sheet3",r,3,"fail")
        driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()


