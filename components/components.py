from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WebElement:
    def __init__(self, driver, locator='', timeout=10):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def click(self):
        """Click on the element with explicit wait"""
        element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator)))
        element.click()

    def find_element(self):
        """Find element with explicit wait"""
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator)))
    
    def exist(self):
        """Check if element exists on the page"""
        try:
            self.find_element()
            return True
        except (NoSuchElementException, TimeoutException):
            return False


    def get_text(self):
        try:
            str(self.find_element().text)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

