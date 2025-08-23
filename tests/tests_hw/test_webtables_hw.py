import time
from pages.tables import Tables
from selenium.webdriver.common.keys import Keys


# def test_webtables_functionality(browser):
#     page_tables = Tables(browser)
#     page_tables.visit()
#     assert page_tables.page_title.visible()
#     title_text = page_tables.page_title.get_text()
#     assert "Tables" in title_text or "Web" in title_text
#     while page_tables.btn_delete_row.exist():
#         page_tables.btn_delete_row.click()
#         time.sleep(1)
#     assert page_tables.no_data_exist()
#     assert page_tables.add_button.visible()
#     page_tables.add_button.click()
#     time.sleep(2)
#     assert page_tables.first_name_input.visible()
#     assert page_tables.submit_button.visible()
#     page_tables.submit_button.click()
#     time.sleep(1)
#     assert page_tables.first_name_input.visible()
#     browser.find_element("tag name", "body").send_keys(Keys.ESCAPE)
#     time.sleep(2)
#     page_tables.add_button.click()
#     time.sleep(2)
#     test_data = {
#         'first_name': 'July',
#         'last_name': 'War',
#         'email': 'war-july@example.com',
#         'age': '30',
#         'salary': '50000',
#         'department': 'IT'
#     }
#     page_tables.first_name_input.send_keys(test_data['first_name'])
#     page_tables.last_name_input.send_keys(test_data['last_name'])
#     page_tables.email_input.send_keys(test_data['email'])
#     page_tables.age_input.send_keys(test_data['age'])
#     page_tables.salary_input.send_keys(test_data['salary'])
#     page_tables.department_input.send_keys(test_data['department'])
#     page_tables.submit_button.click()
#     time.sleep(2)
#     try:
#         page_tables.first_name_input.visible()
#         dialog_still_open = True
#     except:
#         dialog_still_open = False
#     assert not dialog_still_open
#     assert page_tables.no_data_exist() == False
#     page_tables.btn_edit_row.click()
#     time.sleep(2)
#     assert page_tables.first_name_input.visible()
#     current_first_name = page_tables.first_name_input.get_attribute('value')
#     assert current_first_name == test_data['first_name']
#     page_tables.first_name_input.clear()
#     page_tables.first_name_input.send_keys('Jane')
#     page_tables.submit_button.click()
#     time.sleep(2)
#     try:
#         page_tables.first_name_input.visible()
#         dialog_still_open = True
#     except:
#         dialog_still_open = False
#     assert not dialog_still_open
#     page_tables.btn_edit_row.click()
#     time.sleep(2)
#     updated_first_name = page_tables.first_name_input.get_attribute('value')
#     assert updated_first_name == 'Jane'
#     browser.find_element("tag name", "body").send_keys(Keys.ESCAPE)
#     time.sleep(2)
#     page_tables.btn_delete_row.click()
#     time.sleep(2)
#     assert page_tables.no_data_exist()

def test_pagination_functionality(browser):
    page_tables = Tables(browser)
    page_tables.visit()
    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click()
        time.sleep(1)
    
    if page_tables.rows_per_page_select.exist():
        page_tables.rows_per_page_select.select_by_value("5")
    
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
    next_button = page_tables.next_button
    previous_button = page_tables.previous_button
    assert next_button.get_attribute('disabled') is not None
    assert previous_button.get_attribute('disabled') is not None
    page_tables.add_button.click()
    time.sleep(1)
    page_tables.first_name_input.send_keys('Gora')
    page_tables.last_name_input.send_keys('T')
    page_tables.email_input.send_keys('gora@example.com')
    page_tables.age_input.send_keys('31')
    page_tables.salary_input.send_keys('48000')
    page_tables.department_input.send_keys('HR')
    page_tables.submit_button.click()
    time.sleep(1)
    page_tables.add_button.click()
    time.sleep(1)
    page_tables.first_name_input.send_keys('Hleb')
    page_tables.last_name_input.send_keys('A')
    page_tables.email_input.send_keys('hleb@example.com')
    page_tables.age_input.send_keys('34')
    page_tables.salary_input.send_keys('55000')
    page_tables.department_input.send_keys('IT')
    page_tables.submit_button.click()
    time.sleep(1)
    page_tables.add_button.click()
    time.sleep(1)
    page_tables.first_name_input.send_keys('Ivy')
    page_tables.last_name_input.send_keys('M')
    page_tables.email_input.send_keys('ivy@example.com')
    page_tables.age_input.send_keys('26')
    page_tables.salary_input.send_keys('36000')
    page_tables.department_input.send_keys('Marketing')
    page_tables.submit_button.click()
    time.sleep(1)
    page_info = page_tables.page_info.get_text()
    assert "of 2" in page_info
    assert next_button.get_attribute('disabled') is None
    next_button.click()
    time.sleep(1)
    
    if page_tables.page_info.exist():
        page_info_after_next = page_tables.page_info.get_text()
        assert "2" in page_info_after_next
    
    previous_button.click()
    time.sleep(1)
    
    if page_tables.page_info.exist():
        page_info_after_previous = page_tables.page_info.get_text()
        assert "1" in page_info_after_previous