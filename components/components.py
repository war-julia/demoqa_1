from selenium.webdriver.common.by import By

class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        self.find_element().click()

    def find_element(self):
        time.sleep(3)
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)
