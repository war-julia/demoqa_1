from pages.base_page import BasePage
from components.components import WebElement


class ElementsPage(BasePage):

    def __init__(self,driver):
        self.base_url= 'https://demoqa.com/elements'
        super().__init__(driver,self.base_url)

        self.text_please = WebElement(driver, ".col-12.mt-4.col-md-6")
        self.text_elements = WebElement(driver, "div")



