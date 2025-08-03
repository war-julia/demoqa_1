from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from components import WebElement

class DemoQa(BasePage):

    def __init__(self,driver):
        self.base_url= 'https://demoga.com/'
        super().__init__(driver,self.base_url)

        self.icon=WebElement(driver, '#app > header> a')

    def exist_icon(self):
        try:
            self.find_element (locator='#app > header> a')
        except NoSuchElementException:
            return False
        return True

    def click_on_the_icon(self):
        self.find_element(locator='#app > header> a').click()

    def click_on_the_btn(self):
        self.find_element(locator='#арр > div > div > div.home-body > div > div:nth-child(1)').click()



