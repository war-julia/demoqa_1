from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from components.components import WebElement


class DemoQa(BasePage):
    """DemoQA main page class"""

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        # Page elements
        self.icon = WebElement(driver, '.header__logo')
        self.btn_elements = WebElement(driver, ".card:nth-child(1)")

    def exist_icon(self):
        """Check if the icon exists on the page"""
        try:
            self.icon.find_element()
            return True
        except NoSuchElementException:
            return False

