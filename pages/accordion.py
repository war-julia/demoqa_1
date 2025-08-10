from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):

    def __init__(self,driver):
        self.base_url= 'https://demoqa.com/accordian'
        super().__init__(driver,self.base_url)

        self.btn_sidebar_second_testbox = WebElement(driver, "#section1Content > p")
        self.btn_accordion = WebElement(driver, "#section1Heading")

        self.btn_accordion_content21 = WebElement(driver, "#section2Content > p:nth-child(1)")
        self.btn_accordion_content22 = WebElement(driver, "#section2Content > p:nth-child(2)")
        self.btn_accordion_content3 = WebElement(driver, "#section3Content > p")

