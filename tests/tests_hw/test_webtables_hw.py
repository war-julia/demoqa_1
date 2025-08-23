import time
from pages.tables import Tables
from selenium.webdriver.common.keys import Keys


def test_webtables_functionality(browser):
    page_tables = Tables(browser)
    page_tables.visit()
    
    assert page_tables.page_title.visible()
    title_text = page_tables.page_title.get_text()
    assert "Tables" in title_text or "Web" in title_text
    
    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click()
        time.sleep(1)
    assert page_tables.no_data_exist()
    
    assert page_tables.add_button.visible()
    
    page_tables.add_button.click()
    time.sleep(2)
    
    assert page_tables.first_name_input.visible()
    assert page_tables.submit_button.visible()
    
    page_tables.submit_button.click()
    time.sleep(1)
    
    assert page_tables.first_name_input.visible()
    
    browser.find_element("tag name", "body").send_keys(Keys.ESCAPE)
    time.sleep(2)
    
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
    
    try:
        page_tables.first_name_input.visible()
        dialog_still_open = True
    except:
        dialog_still_open = False
    
    assert not dialog_still_open
    assert page_tables.no_data_exist() == False
    
    page_tables.btn_edit_row.click()
    time.sleep(2)
    
    assert page_tables.first_name_input.visible()
    
    current_first_name = page_tables.first_name_input.get_attribute('value')
    assert current_first_name == test_data['first_name']
    
    page_tables.first_name_input.clear()
    page_tables.first_name_input.send_keys('Jane')
    
    page_tables.submit_button.click()
    time.sleep(2)
    
    try:
        page_tables.first_name_input.visible()
        dialog_still_open = True
    except:
        dialog_still_open = False
    
    assert not dialog_still_open
    
    page_tables.btn_edit_row.click()
    time.sleep(2)
    
    updated_first_name = page_tables.first_name_input.get_attribute('value')
    assert updated_first_name == 'Jane'
    
    browser.find_element("tag name", "body").send_keys(Keys.ESCAPE)
    time.sleep(2)
    
    page_tables.btn_delete_row.click()
    time.sleep(2)
    assert page_tables.no_data_exist()