from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from components.components import WebElement


class SauceDemo(BasePage):
    """Sauce Demo main page class"""

    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/'
        super().__init__(driver, self.base_url)

        # Page elements
        self.username_field = WebElement(driver, '#user-name')
        self.password_field = WebElement(driver, '#password')
        self.login_button = WebElement(driver, '#login-button')
        self.error_message = WebElement(driver, '.error-message-container')

    def login(self, username, password):
        """Login with provided credentials"""
        self.username_field.clear()
        self.username_field.send_keys(username)
        self.password_field.clear()
        self.password_field.send_keys(password)
        self.login_button.click()

    def get_error_message(self):
        """Get error message text if login fails"""
        try:
            return self.error_message.get_text()
        except NoSuchElementException:
            return ""

