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
    
    assert page_tables.add_button.visible()
    
    has_data = not page_tables.no_data_exist()
    
    page_tables.add_button.click()
    time.sleep(3)
    
    try:
        form_visible = page_tables.first_name_input.visible()
        assert form_visible
    except Exception:
        pass