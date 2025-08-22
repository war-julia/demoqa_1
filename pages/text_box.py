from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        # Основные элементы формы
        self.full_name_input = WebElement(driver, "#userName")
        self.email_input = WebElement(driver, "#userEmail")
        self.current_address_input = WebElement(driver, "#currentAddress")
        self.permanent_address_input = WebElement(driver, "#permanentAddress")
        self.submit_button = WebElement(driver, "#submit")
        
        # Результат отправки формы
        self.result_name = WebElement(driver, "#name")
        self.result_email = WebElement(driver, "#email")
        self.result_current_address = WebElement(driver, "p#currentAddress")
        self.result_permanent_address = WebElement(driver, "p#permanentAddress")
        
        # Заголовок страницы
        self.page_title = WebElement(driver, ".main-header")
        
        # Навигация
        self.back_to_elements = WebElement(driver, ".btn.btn-light")