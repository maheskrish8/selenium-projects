from selenium import webdriver


def test_fb():
    driver=webdriver.Chrome()
    driver.get("https://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    act_title=driver.title
    assert act_title=="Facebook – log in or sign up"
    driver.close()



def test_google():
    driver = webdriver.Firefox()
    driver.get("https://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    act_title = driver.title
    assert act_title == "Google"
    driver.close()

def test_instagram():
    driver = webdriver.Edge()
    driver.get("https://www.instagram.com/")
    driver.maximize_window()
    driver.implicitly_wait(30)
    act_title = driver.title
    assert act_title == "Instagram"
    driver.close()


def test_whatsapp():
    driver = webdriver.Chrome()
    driver.get("https://www.whatsapp.com/")
    driver.maximize_window()
    driver.implicitly_wait(30)
    act_title = driver.title
    assert act_title == "whatsapp"
    driver.close()
