from pages.form_page import FormPages
from selenium.webdriver.common.by import By
import time


def test_login_form_validation(browser):
    form_page = FormPages(browser)
    form_page.visit()
    time.sleep(3)
    first_name_placeholder = form_page.first_name.get_dom_attribute("placeholder")
    assert first_name_placeholder == "First Name"

    last_name_placeholder = form_page.last_name.get_dom_attribute("placeholder")
    assert last_name_placeholder == "Last Name"

    email_placeholder = form_page.user_email.get_dom_attribute("placeholder")
    assert email_placeholder == "name@example.com"

    email_pattern = form_page.user_email.get_attribute("pattern")
    expected_pattern = r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
    if email_pattern:
        assert email_pattern == expected_pattern
    form_page.btn_submit.scroll_to_element()
    time.sleep(1)
    form_page.btn_submit.click()
    time.sleep(2)
    form_element = browser.find_element(By.TAG_NAME, "form")
    form_class = form_element.get_attribute("class")
    
    assert "was-validated" in form_class