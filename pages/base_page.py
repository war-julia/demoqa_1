from selenium.webdriver.common.by import By
import logging
import time

class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        try:
            return self.driver.get(self.base_url)
        except Exception as e:
            logging.error(f"Error visiting {self.base_url}: {e}")
            raise

    def find_element(self, locator):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, locator)
        except Exception as e:
            logging.error(f"Error finding element {locator}: {e}")
            raise

    def get_url(self):
        try:
            return self.driver.current_url
        except Exception as e:
            logging.error(f"Error getting current URL: {e}")
            return ""

    def equal_url(self):
        try:
            if self.get_url() == self.base_url:
                return True
            else:
                return False
        except Exception as e:
            logging.error(f"Error comparing URLs: {e}")
            return False

    def back(self):
        try:
            self.driver.back()
        except Exception as e:
            logging.error(f"Error going back: {e}")
            raise

    def forward(self):
        try:
            self.driver.forward()
        except Exception as e:
            logging.error(f"Error going forward: {e}")
            raise

    def refresh(self):
        try:
            self.driver.refresh()
        except Exception as e:
            logging.error(f"Error refreshing page: {e}")
            raise

    def get_title(self):
        try:
            return self.driver.title
        except Exception as e:
            logging.error(f"Error getting title: {e}")
            return ""

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False