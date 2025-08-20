from pages.form_page import FormPages
from selenium.webdriver.common.by import By
import time


def test_login_form_validation(browser):
    form_page = FormPages(browser)
    form_page.visit()
    
    time.sleep(3)
    
    first_name_placeholder = form_page.first_name.get_attribute("placeholder")
    assert first_name_placeholder == "First Name", f"Ошибка! '{first_name_placeholder}'"
    
    last_name_placeholder = form_page.last_name.get_attribute("placeholder")
    assert last_name_placeholder == "Last Name", f"Ошибка!'{last_name_placeholder}'"
    
    email_placeholder = form_page.user_email.get_attribute("placeholder")
    assert email_placeholder == "name@example.com", f"Ошибка!'{email_placeholder}'"
    
    email_pattern = form_page.user_email.get_attribute("pattern")
    
    if email_pattern:
        assert "@" in email_pattern, "должно содержать символ @"
        assert "\\." in email_pattern or "." in email_pattern, "должно содержать точку"
    
    form_page.btn_submit.scroll_to_element()
    form_page.btn_submit.click()
    
    time.sleep(2)  # Ждем обработки формы
    
    form_element = browser.find_element(By.TAG_NAME, "form")
    form_class = form_element.get_attribute("class")
    
    assert "was-validated" in form_class, f"Ошибка! Класс формы: '{form_class}'"