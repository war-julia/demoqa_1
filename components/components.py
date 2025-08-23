from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class WebElement:
    def __init__(self, driver, locator='', locator_type="css"):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def click(self):
        try:
            self.find_element().click()
        except Exception as e:
            print(f"Error in click method: {e}")
            # Пробуем использовать JavaScript клик как fallback
            try:
                self.driver.execute_script("arguments[0].click();", self.find_element())
            except Exception as js_error:
                print(f"JavaScript click also failed: {js_error}")
                raise

    def click_force(self):
        try:
            self.driver.execute_script("arguments[0].click();", self.find_element())
        except Exception as e:
            print(f"Error in click_force method: {e}")
            raise

    def click_with_scroll(self):
        try:
            element = self.find_element()
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(0.5)
            try:
                element.click()
            except:
                # Если обычный клик не работает, используем JavaScript
                self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            print(f"Error in click_with_scroll method: {e}")
            raise

    def wait_for_element(self, timeout=10):
        """Ожидание появления элемента на странице"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((self.get_by_type(), self.locator))
            )
            return True
        except TimeoutException:
            return False
        except Exception as e:
            print(f"Error in wait_for_element method: {e}")
            return False

    def find_element(self):
        try:
            return self.driver.find_element(self.get_by_type(), self.locator)
        except Exception as e:
            print(f"Error in find_element method: {e}")
            raise

    def find_elements(self):
        try:
            return self.driver.find_elements(self.get_by_type(), self.locator)
        except Exception as e:
            print(f"Error in find_elements method: {e}")
            return []

    def exist(self):
        try:
            self.find_element()
            return True
        except (NoSuchElementException, TimeoutException):
            return False
        except Exception as e:
            print(f"Error in exist method: {e}")
            return False

    def get_text(self):
        try:
            return str(self.find_element().text)
        except Exception as e:
            print(f"Error in get_text method: {e}")
            return ""

    def visible(self):
        try:
            return self.find_element().is_displayed()
        except Exception as e:
            print(f"Error in visible method: {e}")
            return False

    def check_count_elements(self, count: int) -> bool:
        try:
            if len(self.find_elements()) == count:
                return True
            return False
        except Exception as e:
            print(f"Error in check_count_elements method: {e}")
            return False

    def send_keys(self, text: str):
        try:
            self.find_element().send_keys(text)
        except Exception as e:
            print(f"Error in send_keys method: {e}")
            # Пробуем использовать JavaScript как fallback
            try:
                self.driver.execute_script("arguments[0].value = arguments[1];", self.find_element(), text)
            except Exception as js_error:
                print(f"JavaScript send_keys also failed: {js_error}")
                raise

    def clear(self):
        try:
            self.find_element().clear()
        except Exception as e:
            print(f"Error in clear method: {e}")
            # Пробуем использовать JavaScript как fallback
            try:
                self.driver.execute_script("arguments[0].value = '';", self.find_element())
            except Exception as js_error:
                print(f"JavaScript clear also failed: {js_error}")
                # Используем старый метод как последний fallback
                try:
                    self.send_keys(Keys.CONTROL + "a")
                    self.send_keys(Keys.DELETE)
                except Exception as old_error:
                    print(f"Old clear method also failed: {old_error}")
                    raise

    def get_dom_attribute(self, name: str):
        try:
            value = self.find_element().get_dom_attribute(name)
            return value
        except Exception as e:
            print(f"Error in get_dom_attribute method: {e}")
            return None
    
    def check_css(self, style, value=''):
        try:
            return self.find_element().value_of_css_property(style) == value
        except Exception as e:
            print(f"Error in check_css method: {e}")
            return False

    def get_attribute(self, name: str):
        """Получение обычного HTML атрибута"""
        try:
            value = self.find_element().get_attribute(name)
            return value
        except Exception as e:
            print(f"Error in get_attribute method: {e}")
            return None

    def scroll_to_element(self):
        try:
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", self.find_element()
            )
        except Exception as e:
            print(f"Error in scroll_to_element method: {e}")
            raise

    def select_by_value(self, value: str):
        """Выбор значения в селекторе по значению"""
        try:
            select = Select(self.find_element())
            select.select_by_value(value)
        except Exception as e:
            print(f"Error in select_by_value method: {e}")
            # Пробуем использовать JavaScript как fallback
            try:
                self.driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));", self.find_element(), value)
            except Exception as js_error:
                print(f"JavaScript select_by_value also failed: {js_error}")
                raise

    def get_by_type(self):
        try:
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
                return By.CSS_SELECTOR  # Возвращаем CSS селектор по умолчанию
        except Exception as e:
            print(f"Error in get_by_type method: {e}")
            return By.CSS_SELECTOR  # Возвращаем CSS селектор по умолчанию