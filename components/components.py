from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class WebElement:
    def __init__(self, driver, locator='', locator_type="css"):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def click(self):
        self.find_element().click()

    def click_force(self):
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def click_with_scroll(self):
        element = self.find_element()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
        try:
            element.click()
        except:
            # Если обычный клик не работает, используем JavaScript
            self.driver.execute_script("arguments[0].click();", element)

    def wait_for_element(self, timeout=10):
        """Ожидание появления элемента на странице"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((self.get_by_type(), self.locator))
            )
            return True
        except TimeoutException:
            return False

    def find_element(self):
        return self.driver.find_element(self.get_by_type(), self.locator)

    def find_elements(self):
        return self.driver.find_elements(self.get_by_type(), self.locator)

    def exist(self):
        try:
            self.find_element()
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def get_text(self):
        return str(self.find_element().text)

    def visible(self):
        return self.find_element().is_displayed()

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False

    def send_keys(self, text: str):
        self.find_element().send_keys(text)

    def clear(self):
        self.send_keys(Keys.CONTROL + "a")
        self.send_keys(Keys.DELETE)

    def get_dom_attribute(self, name: str):
        value = self.find_element().get_dom_attribute(name)
        return value

    def get_attribute(self, name: str):
        """Получение обычного HTML атрибута"""
        value = self.find_element().get_attribute(name)
        return value

    def scroll_to_element(self):
        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);", self.find_element()
        )

    def get_by_type(self):
        if self.locator_type == "id":
            return By.ID
        elif self.locator_type == "name":
            return By.NAME
        elif self.locator_type == "xpath":
            return By.XPATH
        elif self.locator_type == "css":
            return By.CSS_SELECTOR
        elif self.locator_type == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + self.locator_type + " not correct")
        return False
