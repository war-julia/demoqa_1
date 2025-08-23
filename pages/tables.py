from pages.base_page import BasePage
from components.components import WebElement
import time


class Tables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        # Основные элементы таблицы
        self.add_button = WebElement(driver, "#addNewRecordButton, button[title='Add'], .add-button")
        self.search_box = WebElement(driver, "#searchBox, input[placeholder*='Search'], .search-input")
        
        # Кнопки управления строками
        self.btn_delete_row = WebElement(driver, "[title='Delete'], [aria-label='Delete'], .delete-button")
        self.btn_edit_row = WebElement(driver, "[title='Edit'], [aria-label='Edit'], .edit-button")
        
        # Элементы формы добавления/редактирования
        self.first_name_input = WebElement(driver, "#firstName, input[name='firstName'], input[placeholder*='First']")
        self.last_name_input = WebElement(driver, "#lastName, input[name='lastName'], input[placeholder*='Last']")
        self.email_input = WebElement(driver, "#userEmail, input[name='userEmail'], input[type='email']")
        self.age_input = WebElement(driver, "#age, input[name='age'], input[type='number']")
        self.salary_input = WebElement(driver, "#salary, input[name='salary'], input[placeholder*='Salary']")
        self.department_input = WebElement(driver, "#department, input[name='department'], input[placeholder*='Department']")
        self.submit_button = WebElement(driver, "#submit, button[type='submit'], .submit-button")
        
        # Элементы таблицы
        self.table_rows = WebElement(driver, ".rt-tbody .rt-tr, tbody tr, .table-row")
        self.table_data = WebElement(driver, ".rt-td, td, .table-cell")
        
        # Сообщения и статусы
        self.no_data_message = WebElement(driver, ".rt-noData, .no-data, .empty-message, tbody tr td[colspan]")
        
        # Заголовок страницы - исправленный селектор
        self.page_title = WebElement(driver, "h1, .page-title, .main-header")
        
        # Навигация
        self.back_to_elements = WebElement(driver, ".btn.btn-light, .back-button, .nav-back")
        
        # Элементы пагинации - улучшенные селекторы
        self.rows_per_page_select = WebElement(driver, "select")
        self.next_button = WebElement(driver, "button[aria-label='Next page'], button[title='Next page'], .pagination-next")
        self.previous_button = WebElement(driver, "button[aria-label='Previous page'], button[title='Previous page'], .pagination-prev")
        self.page_info = WebElement(driver, ".pagination-info, .pagination-detail")
    
    def no_data_exist(self):
        """Проверяет, есть ли данные в таблице"""
        try:
            # Проверяем наличие сообщения "No data"
            if self.no_data_message.exist():
                return True
            
            # Проверяем количество строк с данными
            rows = self.table_rows.find_elements()
            # Фильтруем только строки с реальными данными
            valid_rows = []
            for row in rows:
                try:
                    row_text = row.text.strip()
                    # Проверяем, что строка содержит данные (не пустая и не содержит "No data")
                    if row_text and not any(no_data_text in row_text.lower() for no_data_text in ["no data", "empty", "нет данных"]):
                        # Проверяем, что строка содержит достаточно данных
                        if len(row_text) > 10 and not row_text.startswith('No data'):
                            valid_rows.append(row)
                except:
                    continue
            
            return len(valid_rows) == 0
        except Exception as e:
            print(f"Error in no_data_exist: {e}")
            return True
    
    def get_row_count(self):
        """Возвращает количество строк в таблице"""
        try:
            rows = self.table_rows.find_elements()
            # Фильтруем только строки с данными (исключаем пустые и сообщения об отсутствии данных)
            valid_rows = []
            for row in rows:
                try:
                    row_text = row.text.strip()
                    # Проверяем, что строка содержит данные
                    if row_text and not any(no_data_text in row_text.lower() for no_data_text in ["no data", "empty", "нет данных"]):
                        if len(row_text) > 10:
                            valid_rows.append(row)
                except:
                    continue
            return len(valid_rows)
        except Exception as e:
            print(f"Error in get_row_count: {e}")
            return 0
    
    def add_new_record(self, first_name, last_name, email, age, salary, department):
        """Добавляет новую запись в таблицу"""
        try:
            self.add_button.click()
            time.sleep(1)
            
            # Очищаем поля перед вводом
            self.first_name_input.clear()
            self.last_name_input.clear()
            self.email_input.clear()
            self.age_input.clear()
            self.salary_input.clear()
            self.department_input.clear()
            
            # Вводим данные
            self.first_name_input.send_keys(first_name)
            self.last_name_input.send_keys(last_name)
            self.email_input.send_keys(email)
            self.age_input.send_keys(str(age))
            self.salary_input.send_keys(str(salary))
            self.department_input.send_keys(department)
            
            # Отправляем форму
            self.submit_button.click()
            time.sleep(1)
        except Exception as e:
            print(f"Error in add_new_record: {e}")
            raise
    
    def search_record(self, search_text):
        """Ищет запись в таблице"""
        try:
            self.search_box.clear()
            self.search_box.send_keys(search_text)
            time.sleep(0.5)
        except Exception as e:
            print(f"Error in search_record: {e}")
            raise
    
    def delete_all_records(self):
        """Удаляет все записи из таблицы"""
        try:
            while self.btn_delete_row.exist():
                self.btn_delete_row.click()
                time.sleep(0.5)
        except Exception as e:
            print(f"Error in delete_all_records: {e}")
            raise
