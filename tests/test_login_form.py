from pages.form_page import FormPages


def test_login_form(browser):
    form_page = FormPages(browser)
    form_page.visit()
    assert not form_page.modal_dialog.exist()
    form_page.first_name.send_keys("tester")
    form_page.last_name.send_keys("testerovich")
    form_page.user_email.send_keys("test@ttt.tt")
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys("1111111111")
    form_page.hobbies.click_force()
    form_page.current_address.send_keys("karelia")
    form_page.btn_submit.click_force()
    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()

def test_login_form_state_city(browser):
    form_page = FormPages(browser)
    form_page.visit()
    form_page.state.click()
    form_page.state_option.click()
    form_page.city.click()
    form_page.city_option.click()

    assert form_page.state.get_text() != ""
    assert form_page.city.get_text() != ""