from selenium.webdriver.common.by import By


class BasePage:
    """Base page class that contains common methods for all pages"""

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        """Navigate to the base URL"""
        return self.driver.get(self.base_url)

    def get_url(self):
        """Get current page URL"""
        return self.driver.current_url

    def equal_url(self):
        """Check if current URL matches base URL"""
        return self.get_url() == self.base_url