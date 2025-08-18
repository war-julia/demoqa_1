from pages.form_page import FormPages

def test_login_form_validation(browser):
    form_page = FormPages(browser)
    form_page.visit()

    assert form_page.first_name.get_dom_attribute("placeholder") == "First Name"
    assert form_page.last_name.get_dom_attribute("placeholder") == "Last Name"
    assert form_page.user_email.get_dom_attribute("placeholder") == "name@example.com"
    email_pattern = r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
    assert form_page.user_email.get_dom_attribute("pattern") == email_pattern
    
    form_page.btn_submit.click()
    form_element = form_page.driver.find_element("tag name", "form")
    assert "was-validated" in form_element.get_attribute("class")
