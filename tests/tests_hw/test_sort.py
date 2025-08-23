import time
from pages.tables import Tables


def test_table_sorting(browser):
    tables_page = Tables(browser)
    tables_page.visit()
    
    time.sleep(2)
    
    headers = [
        tables_page.first_name_header,
        tables_page.last_name_header,
        tables_page.age_header,
        tables_page.email_header,
        tables_page.salary_header,
        tables_page.department_header
    ]
    
    for header in headers:
        if header.exist():
            header.click()
            time.sleep(1)
            
            header_class = header.get_attribute('class')
            assert 'sort-asc' in header_class or 'sort-desc' in header_class
            
            header.click()
            time.sleep(1)
            
            header_class = header.get_attribute('class')
            assert 'sort-asc' in header_class or 'sort-desc' in header_class
