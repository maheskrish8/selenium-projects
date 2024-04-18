import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
def test_verifyTitle():
    act_Title=driver.title
    assert act_Title=="Facebook – log in or sign up"


@pytest.mark.usefixtures("setup")
def test_verifyUrl():
    act_Url=driver.current_url
    assert act_Url=="https://www.facebook.com/"

@pytest.mark.usefixtures("setup")
def test_verifylogin():
    act_Logintext=driver.find_element(By.NAME,"login").text
    assert act_Logintext=="Log in"


