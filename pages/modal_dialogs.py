from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        # Element for all submenu buttons (5 buttons total)
        self.btns_submenu = WebElement(driver, ".btn")
        
        # Element for the icon to navigate to main page
        self.icon = WebElement(driver, "header > a > img")
