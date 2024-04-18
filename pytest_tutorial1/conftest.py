import pytest


@pytest.fixture(scope='module')
def setup():
    print('Open the browser')
    yield
    print('Close the browser')