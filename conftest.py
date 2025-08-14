import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser():

    driver = webdriver.Chrome()
    driver.set_window_size(1000, 1000)
    

    yield driver
 
    driver.quit()