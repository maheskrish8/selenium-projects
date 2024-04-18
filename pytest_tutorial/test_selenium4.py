from selenium import webdriver

def setup(module):
    global driver
    driver=webdriver.Chrome()
    driver.get("https://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(30)

    yield
    driver.close()


def test_verifyTitle(setup):
    act_title=driver.title
    assert act_title=="Google"

