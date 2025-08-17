from pages.text_box import TextBox

def test_text_box_submit(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    test_text = "Test User Input"
    text_box_page.name.send_keys(test_text)
    text_box_page.current_address.send_keys(test_text)
    text_box_page.btn_submit.click()
    
    assert text_box_page.name_output.get_text() == f"Name:{test_text}"
    assert text_box_page.current_address_output.get_text() == f"Current Address :{test_text}"
