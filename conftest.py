import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver
    driver.quit()