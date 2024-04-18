from selenium import webdriver

driver=None
def setup(module):
    global driver
    driver=webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(30)


def teardown(module):
    driver.close()


def test_verifyTitle():
    act_title=driver.title
    assert act_title=="Google"

