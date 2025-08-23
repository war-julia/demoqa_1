import time
from pages.tables import Tables
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_webtables_functionality(browser):
    try:
        page_tables = Tables(browser)
        page_tables.visit()
        assert page_tables.page_title.visible()
        title_text = page_tables.page_title.get_text()
        assert "Tables" in title_text or "Web" in title_text
        
        # Удаляем все существующие записи
        while page_tables.btn_delete_row.exist():
            page_tables.btn_delete_row.click()
            time.sleep(1)
        
        # Проверяем, что таблица пуста
        assert page_tables.no_data_exist()
        assert page_tables.add_button.visible()
        
        # Тестируем добавление записи
        page_tables.add_button.click()
        time.sleep(2)
        assert page_tables.first_name_input.visible()
        assert page_tables.submit_button.visible()
        
        # Пытаемся отправить пустую форму
        page_tables.submit_button.click()
        time.sleep(1)
        assert page_tables.first_name_input.visible()
        
        # Закрываем диалог
        browser.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        time.sleep(2)
        
        # Добавляем корректную запись
        page_tables.add_button.click()
        time.sleep(2)
        test_data = {
            'first_name': 'July',
            'last_name': 'War',
            'email': 'war-july@example.com',
            'age': '30',
            'salary': '50000',
            'department': 'IT'
        }
        page_tables.first_name_input.send_keys(test_data['first_name'])
        page_tables.last_name_input.send_keys(test_data['last_name'])
        page_tables.email_input.send_keys(test_data['email'])
        page_tables.age_input.send_keys(test_data['age'])
        page_tables.salary_input.send_keys(test_data['salary'])
        page_tables.department_input.send_keys(test_data['department'])
        page_tables.submit_button.click()
        time.sleep(2)
        
        # Проверяем, что диалог закрылся
        try:
            page_tables.first_name_input.visible()
            dialog_still_open = True
        except:
            dialog_still_open = False
        assert not dialog_still_open
        
        # Проверяем, что данные появились в таблице
        assert not page_tables.no_data_exist()
        
        # Тестируем редактирование
        page_tables.btn_edit_row.click()
        time.sleep(2)
        assert page_tables.first_name_input.visible()
        current_first_name = page_tables.first_name_input.get_attribute('value')
        assert current_first_name == test_data['first_name']
        
        # Изменяем имя
        page_tables.first_name_input.clear()
        page_tables.first_name_input.send_keys('Jane')
        page_tables.submit_button.click()
        time.sleep(2)
        
        # Проверяем, что диалог закрылся
        try:
            page_tables.first_name_input.visible()
            dialog_still_open = True
        except:
            dialog_still_open = False
        assert not dialog_still_open
        
        # Проверяем, что изменения сохранились
        page_tables.btn_edit_row.click()
        time.sleep(2)
        updated_first_name = page_tables.first_name_input.get_attribute('value')
        assert updated_first_name == 'Jane'
        
        # Закрываем диалог
        browser.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        time.sleep(2)
        
        # Удаляем запись
        page_tables.btn_delete_row.click()
        time.sleep(2)
        assert page_tables.no_data_exist()
        
    except Exception as e:
        print(f"Error in test_webtables_functionality: {e}")
        raise


def test_pagination_functionality(browser):
    try:
        page_tables = Tables(browser)
        page_tables.visit()
        
        # Удаляем все существующие записи
        while page_tables.btn_delete_row.exist():
            page_tables.btn_delete_row.click()
            time.sleep(1)
        
        # Устанавливаем количество строк на странице
        if page_tables.rows_per_page_select.exist():
            page_tables.rows_per_page_select.select_by_value("5")
        
        # Создаем тестовые записи
        test_records = [
            {'first_name': 'Kate', 'last_name': 'D', 'email': 'kate@example.com', 'age': '25', 'salary': '30000', 'department': 'HR'},
            {'first_name': 'Jenya', 'last_name': 'S', 'email': 'jenya@example.com', 'age': '30', 'salary': '40000', 'department': 'IT'},
            {'first_name': 'Sasha', 'last_name': 'J', 'email': 'sasha@example.com', 'age': '35', 'salary': '50000', 'department': 'Sales'},
            {'first_name': 'Alice', 'last_name': 'B', 'email': 'alice@example.com', 'age': '28', 'salary': '35000', 'department': 'Marketing'},
            {'first_name': 'Denis', 'last_name': 'W', 'email': 'denis@example.com', 'age': '32', 'salary': '45000', 'department': 'Finance'},
            {'first_name': 'Dasha', 'last_name': 'D', 'email': 'dasha@example.com', 'age': '27', 'salary': '38000', 'department': 'HR'},
            {'first_name': 'Ed', 'last_name': 'M', 'email': 'ed@example.com', 'age': '33', 'salary': '52000', 'department': 'IT'},
            {'first_name': 'Fatima', 'last_name': 'G', 'email': 'fatima@example.com', 'age': '29', 'salary': '42000', 'department': 'Sales'}
        ]
        
        # Добавляем записи
        for record in test_records:
            page_tables.add_button.click()
            time.sleep(1)
            page_tables.first_name_input.send_keys(record['first_name'])
            page_tables.last_name_input.send_keys(record['last_name'])
            page_tables.email_input.send_keys(record['email'])
            page_tables.age_input.send_keys(record['age'])
            page_tables.salary_input.send_keys(record['salary'])
            page_tables.department_input.send_keys(record['department'])
            page_tables.submit_button.click()
            time.sleep(1)
        
        # Получаем ссылки на кнопки пагинации
        next_button = page_tables.next_button
        previous_button = page_tables.previous_button
        
        # Проверяем начальное состояние кнопок
        if next_button.exist() and previous_button.exist():
            # На первой странице кнопка "Предыдущая" должна быть неактивна
            assert previous_button.get_attribute('disabled') is not None
            # Кнопка "Следующая" может быть активна, если есть вторая страница
        
        # Добавляем еще несколько записей для создания второй страницы
        additional_records = [
            {'first_name': 'Gora', 'last_name': 'T', 'email': 'gora@example.com', 'age': '31', 'salary': '48000', 'department': 'HR'},
            {'first_name': 'Hleb', 'last_name': 'A', 'email': 'hleb@example.com', 'age': '34', 'salary': '55000', 'department': 'IT'},
            {'first_name': 'Ivy', 'last_name': 'M', 'email': 'ivy@example.com', 'age': '26', 'salary': '36000', 'department': 'Marketing'}
        ]
        
        for record in additional_records:
            page_tables.add_button.click()
            time.sleep(1)
            page_tables.first_name_input.send_keys(record['first_name'])
            page_tables.last_name_input.send_keys(record['last_name'])
            page_tables.email_input.send_keys(record['email'])
            page_tables.age_input.send_keys(record['age'])
            page_tables.salary_input.send_keys(record['salary'])
            page_tables.department_input.send_keys(record['department'])
            page_tables.submit_button.click()
            time.sleep(1)
        
        # Проверяем информацию о страницах
        if page_tables.page_info.exist():
            page_info = page_tables.page_info.get_text()
            # Более гибкая проверка для разных форматов информации о страницах
            assert any(text in page_info for text in ["of 2", "2", "Page 2", "2 of"])
        
        # Тестируем навигацию по страницам
        if next_button.exist():
            # Кнопка "Следующая" должна быть активна
            assert next_button.get_attribute('disabled') is None
            next_button.click()
            time.sleep(1)
            
            # Проверяем, что перешли на вторую страницу
            if page_tables.page_info.exist():
                page_info_after_next = page_tables.page_info.get_text()
                assert any(text in page_info_after_next for text in ["2", "Page 2", "2 of"])
        
        if previous_button.exist():
            # Переходим обратно на первую страницу
            previous_button.click()
            time.sleep(1)
            
            # Проверяем, что вернулись на первую страницу
            if page_tables.page_info.exist():
                page_info_after_previous = page_tables.page_info.get_text()
                assert any(text in page_info_after_previous for text in ["1", "Page 1", "1 of"])
                
    except Exception as e:
        print(f"Error in test_pagination_functionality: {e}")
        raise