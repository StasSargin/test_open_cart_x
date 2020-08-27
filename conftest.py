import pytest
from selenium import webdriver


@pytest.fixture
def browser(request):
    url = 'https://demo.opencart.com/'
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)
    driver.get(url)
    return driver
