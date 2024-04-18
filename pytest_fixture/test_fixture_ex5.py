import pytest




@pytest.mark.usefixtures('Allbrowsers')
class Testbase:
    pass

class Test_Edge_browser(Testbase):
    def test_verifyTitle(self):

        act_Title = self.driver.title
        assert act_Title == "Google"

    def test_verifyUrl(self):
        act_Url = self.driver.current_url
        assert act_Url == "https://www.google.com/"


