from pages.base_page import BasePage
from components.components import WebElement


class TheInternetPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "http://the-internet.herokuapp.com/")
        
        # Ссылка на Add/Remove Elements
        self.add_remove_elements_link = WebElement(driver, "a[href='/add_remove_elements/']")
    
    def click_add_remove_elements(self):
        """Клик по ссылке Add/Remove Elements"""
        self.add_remove_elements_link.click()
