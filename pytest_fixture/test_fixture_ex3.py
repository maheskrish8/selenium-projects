import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope='class')
def init_chrome(request):
    c_driver=webdriver.Chrome()
    request.cls.driver=c_driver


    yield
    c_driver.close()

@pytest.mark.usefixtures("init_chrome")
class Testbase:
    pass

class Test_Chrome(Testbase):

    def test_verifyTitle(self):
        self.driver.get("https://www.facebook.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        act_Title = self.driver.title
        assert act_Title == "Facebook – log in or sign up"


    def test_verifyUrl(self):
        act_Url = self.driver.current_url
        assert act_Url == "https://www.facebook.com/"


    def test_verifylogin(self):
        act_Logintext = self.driver.find_element(By.NAME, "login").text
        assert act_Logintext == "Log in"




