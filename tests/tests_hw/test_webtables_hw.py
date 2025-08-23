import time
from pages.tables import Tables
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_webtables_functionality(browser):
    page_tables = Tables(browser)
    page_tables.visit()
    
    assert page_tables.page_title.visible()
    title_text = page_tables.page_title.get_text()
    assert "Tables" in title_text or "Web" in title_text
    
    delete_count = 0
    while page_tables.btn_delete_row.exist() and delete_count < 10:
        page_tables.btn_delete_row.click()
        time.sleep(0.5)
        delete_count += 1
    
    assert page_tables.no_data_exist()
    assert page_tables.add_button.visible()
    
    page_tables.add_button.click()
    time.sleep(1)
    assert page_tables.first_name_input.visible()
    assert page_tables.submit_button.visible()
    
    page_tables.submit_button.click()
    time.sleep(1)
    assert page_tables.first_name_input.visible()
    
    browser.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
    time.sleep(1)
    
    page_tables.add_button.click()
    time.sleep(1)
    
    test_data = {
        'first_name': 'July',
        'last_name': 'War',
        'email': 'war-july@example.com',
        'age': '30',
        'salary': '50000',
        'department': 'IT'
    }
    
    page_tables.first_name_input.clear()
    page_tables.first_name_input.send_keys(test_data['first_name'])
    page_tables.last_name_input.clear()
    page_tables.last_name_input.send_keys(test_data['last_name'])
    page_tables.email_input.clear()
    page_tables.email_input.send_keys(test_data['email'])
    page_tables.age_input.clear()
    page_tables.age_input.send_keys(test_data['age'])
    page_tables.salary_input.clear()
    page_tables.salary_input.send_keys(test_data['salary'])
    page_tables.department_input.clear()
    page_tables.department_input.send_keys(test_data['department'])
    
    page_tables.submit_button.click()
    time.sleep(3)
    time.sleep(2)
    
    try:
        page_tables.first_name_input.visible()
        dialog_still_open = True
    except:
        dialog_still_open = False
    
    if dialog_still_open:
        browser.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        time.sleep(1)
    
    has_data = not page_tables.no_data_exist()
    assert has_data, "Запись не добавилась в таблицу"
    
    page_tables.btn_edit_row.click()
    time.sleep(1)
    assert page_tables.first_name_input.visible()
    
    current_first_name = page_tables.first_name_input.get_attribute('value')
    assert current_first_name == test_data['first_name']
    
    page_tables.first_name_input.clear()
    page_tables.first_name_input.send_keys('Jane')
    page_tables.submit_button.click()
    time.sleep(2)
    
    try:
        page_tables.first_name_input.visible()
        dialog_open = True
    except:
        dialog_open = False
    assert not dialog_open
    
    page_tables.btn_edit_row.click()
    time.sleep(1)
    updated_first_name = page_tables.first_name_input.get_attribute('value')
    assert updated_first_name == 'Jane'
    
    browser.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
    time.sleep(1)
    
    page_tables.btn_delete_row.click()
    time.sleep(1)
    
    assert page_tables.no_data_exist()