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


