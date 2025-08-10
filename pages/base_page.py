from selenium.webdriver.common.by import By
import time

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        return self.driver.get(self.base_url)

    # def find_element(self.locator):
    #     return self.driver.find_element(By.CSS_SELECTOR, locator)


    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
         if self.get_url() == self.base_url:
             return True
         else:
             return False

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        self.driver.title
