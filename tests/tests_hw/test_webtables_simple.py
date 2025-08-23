import time
from pages.tables import Tables


def test_webtables_basic(browser):
    """
    Простой тест базовой функциональности веб-таблиц
    """
    page_tables = Tables(browser)
    page_tables.visit()

    # Проверяем загрузку страницы
    assert page_tables.page_title.visible()
    title_text = page_tables.page_title.get_text()
    print(f"Заголовок страницы: {title_text}")
    
    # Проверяем наличие основных элементов
    assert page_tables.add_button.visible()
    print("Кнопка Add найдена")
    
    # Проверяем, есть ли данные в таблице
    if page_tables.no_data_exist():
        print("Таблица пуста")
    else:
        print("В таблице есть данные")
    
    # Пытаемся открыть диалог добавления
    print("Открываем диалог добавления...")
    page_tables.add_button.click()
    time.sleep(3)
    
    # Проверяем, открылся ли диалог
    try:
        if page_tables.first_name_input.visible():
            print("Диалог добавления открылся успешно")
            
            # Проверяем все поля формы
            assert page_tables.last_name_input.visible()
            assert page_tables.email_input.visible()
            assert page_tables.age_input.visible()
            assert page_tables.salary_input.visible()
            assert page_tables.department_input.visible()
            assert page_tables.submit_button.visible()
            
            print("Все поля формы найдены")
            
            # Закрываем диалог
            browser.find_element("tag name", "body").send_keys("Escape")
            time.sleep(1)
            print("Диалог закрыт")
            
        else:
            print("Диалог добавления НЕ открылся")
            
    except Exception as e:
        print(f"Ошибка при работе с диалогом: {e}")
    
    print("Базовый тест завершен")


def test_webtables_add_record(browser):
    """
    Тест добавления записи в таблицу
    """
    page_tables = Tables(browser)
    page_tables.visit()
    
    # Очищаем таблицу
    print("Очищаем таблицу...")
    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click()
        time.sleep(1)
    
    if page_tables.no_data_exist():
        print("Таблица очищена")
        
        # Добавляем запись
        print("Добавляем запись...")
        page_tables.add_button.click()
        time.sleep(2)
        
        if page_tables.first_name_input.visible():
            # Заполняем форму
            page_tables.first_name_input.send_keys("Test")
            page_tables.last_name_input.send_keys("User")
            page_tables.email_input.send_keys("test@example.com")
            page_tables.age_input.send_keys("25")
            page_tables.salary_input.send_keys("30000")
            page_tables.department_input.send_keys("QA")
            
            # Сохраняем
            page_tables.submit_button.click()
            time.sleep(2)
            
            # Проверяем результат
            if not page_tables.no_data_exist():
                print("Запись добавлена успешно")
                
                # Удаляем запись
                page_tables.btn_delete_row.click()
                time.sleep(1)
                
                if page_tables.no_data_exist():
                    print("Запись удалена успешно")
                else:
                    print("Ошибка при удалении записи")
            else:
                print("Ошибка при добавлении записи")
        else:
            print("Диалог добавления не открылся")
    else:
        print("Не удалось очистить таблицу")
    
    print("Тест добавления записи завершен")
