import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("init_Chrome_orangeHRM")
class Testbase:
    pass


class Test_Chrome_browser(Testbase):
    @pytest.mark.skip
    def test_verifyTitle(self):
        act_Title = self.driver.title
        assert act_Title == "OrangeHRM"
    @pytest.mark.skip
    def test_verifyUrl(self):
        act_Url = self.driver.current_url
        assert act_Url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    @pytest.mark.xfail
    def test_verifyloginHeadig(self):
       act_text= self.driver.find_element(By.XPATH,"//h5[text()='Login']").text
       assert act_text=="Log in"

    @pytest.mark.skip
    def test_verifylogin(self):
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.NAME,"password").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[normalize-space(text()='Login')]").click()
        assert self.driver.title=="OrangeHRM"
        self.driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
        self.driver.find_element(By.LINK_TEXT,"Logout").click()


    @pytest.mark.parametrize("un","pwd",[("Admin","Admin","Admin"),("admin123","admin123","admin123")])
    def test_verifylogin1(self,un,pwd):
        self.driver.find_element(By.NAME, "username").send_keys(un)
        self.driver.find_element(By.NAME, "password").send_keys(pwd)
        self.driver.find_element(By.XPATH, "//button[normalize-space(text()='Login')]").click()
        assert self.driver.title == "OrangeHRM"
        self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
