from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebElement:
    def __init__(self, driver, locator='', timeout=10):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout

    def click(self):
        self.find_element().click()

    def find_element(self):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.locator))
            )
        except (NoSuchElementException, TimeoutException):
            raise NoSuchElementException(f"Element with locator '{self.locator}' not found")

    def send_keys(self, text):
        """Send keys to the element"""
        self.find_element().send_keys(text)

    def clear(self):
        """Clear the element"""
        self.find_element().clear()

    def get_text(self):
        """Get text from the element"""
        return self.find_element().text

    def is_displayed(self):
        """Check if element is displayed"""
        try:
            return self.find_element().is_displayed()
        except (NoSuchElementException, TimeoutException):
            return False


from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'

    def visit(self):
        self.driver.get(self.base_url)

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)