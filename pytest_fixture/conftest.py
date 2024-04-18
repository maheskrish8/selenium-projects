import pytest
from selenium import webdriver


@pytest.fixture(scope='module')
def setup():
    global driver
    driver=webdriver.Chrome()
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    driver.implicitly_wait(30)



    yield
    driver.close()

@pytest.fixture(scope='module')
def setup1():
    global driver
    driver=webdriver.Edge()
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    driver.implicitly_wait(30)


    yield
    driver.close()

@pytest.fixture(scope='module')
def setup2():
    global driver
    driver=webdriver.Firefox()
    driver.get("https://www.facebook.com")
    driver.maximize_window()
    driver.implicitly_wait(30)


    yield
    driver.close()


@pytest.fixture(scope='class')
def init_Edge(request):
    edge_driver = webdriver.Edge()
    request.cls.driver = edge_driver
    edge_driver.get("https://www.google.com/")
    edge_driver.maximize_window()
    edge_driver.implicitly_wait(30)

    yield
    edge_driver.close()


@pytest.fixture(scope='class')
def init_Chrome(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    chrome_driver.get("https://www.google.com/")
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(30)

    yield
    chrome_driver.close()


@pytest.fixture(scope='class')
def init_Firefox(request):
    firefox_driver = webdriver.Firefox()
    request.cls.driver = firefox_driver
    firefox_driver.get("https://www.google.com/")
    firefox_driver.maximize_window()
    firefox_driver.implicitly_wait(30)

    yield
    firefox_driver.close()


@pytest.fixture(scope='class')
def init_Chrome_orangeHRM(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    chrome_driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(30)

    yield
    chrome_driver.close()


@pytest.fixture (scope='class',params=['Edge','Chrome','Firefox'])
def Allbrowsers(request):
    global web_driver
    if request.param=="Chrome":
        web_driver=webdriver.Chrome()

    if request.param=="Firefox":
        web_driver=webdriver.Firefox()

    if request.param=="Edge":
        web_driver=webdriver.Edge()

    request.cls.driver=web_driver
    web_driver.get("https://www.google.com/")
    web_driver.maximize_window()
    web_driver.implicitly_wait(30)
    web_driver.find_element()


    yield
    web_driver.close()


