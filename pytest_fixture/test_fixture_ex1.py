import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_verifyTitle(setup2):
    act_Title=driver.title
    assert act_Title=="Facebook – log in or sign up"



def test_verifyUrl(setup2):
    act_Url=driver.current_url
    assert act_Url=="https://www.facebook.com/"

def test_verifylogin(setup2):
    act_Logintext=driver.find_element(By.NAME,"login").text
    assert act_Logintext=="Log in"


