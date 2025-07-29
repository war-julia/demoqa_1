import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def browser():
    """Fixture to create and manage Chrome WebDriver instance"""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver
    driver.quit()