from pages.base_page import BasePage
from components.components import WebElement
import time


class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        # Основные элементы таблицы
        self.add_button = WebElement(driver, "#addNewRecordButton")
        self.search_box = WebElement(driver, "#searchBox")
        
        # Кнопки управления строками
        self.btn_delete_row = WebElement(driver, "[title='Delete']")
        self.btn_edit_row = WebElement(driver, "[title='Edit']")
        
        # Элементы формы добавления/редактирования
        self.first_name_input = WebElement(driver, "#firstName")
        self.last_name_input = WebElement(driver, "#lastName")
        self.email_input = WebElement(driver, "#userEmail")
        self.age_input = WebElement(driver, "#age")
        self.salary_input = WebElement(driver, "#salary")
        self.department_input = WebElement(driver, "#department")
        self.submit_button = WebElement(driver, "#submit")
        
        # Элементы таблицы
        self.table_rows = WebElement(driver, ".rt-tbody .rt-tr")
        self.table_data = WebElement(driver, ".rt-td")
        
        # Сообщения и статусы
        self.no_data_message = WebElement(driver, ".rt-noData")
        
        # Заголовок страницы
        self.page_title = WebElement(driver, ".main-header")
        
        # Навигация
        self.back_to_elements = WebElement(driver, ".btn.btn-light")
    
    def no_data_exist(self):
        """Проверяет, есть ли данные в таблице"""
        return self.no_data_message.exist()
    
    def get_row_count(self):
        """Возвращает количество строк в таблице"""
        rows = self.table_rows.find_elements()
        return len([row for row in rows if row.text.strip()])
    
    def add_new_record(self, first_name, last_name, email, age, salary, department):
        """Добавляет новую запись в таблицу"""
        self.add_button.click()
        self.first_name_input.send_keys(first_name)
        self.last_name_input.send_keys(last_name)
        self.email_input.send_keys(email)
        self.age_input.send_keys(str(age))
        self.salary_input.send_keys(str(salary))
        self.department_input.send_keys(department)
        self.submit_button.click()
    
    def search_record(self, search_text):
        """Ищет запись в таблице"""
        self.search_box.clear()
        self.search_box.send_keys(search_text)
    
    def delete_all_records(self):
        """Удаляет все записи из таблицы"""
        while self.btn_delete_row.exist():
            self.btn_delete_row.click()
            time.sleep(0.5)
