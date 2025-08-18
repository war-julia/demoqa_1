from pages.text_box import TextBox

def test_text_box_submit(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()

    name_text = "Ivan Ivanov"
    address_text = "Russia Moscow Polezhaevskaya, 16-8"
    
    # Fill the form
    text_box_page.name.send_keys(name_text)
    text_box_page.current_address.send_keys(address_text)
    text_box_page.btn_submit.click()

    assert text_box_page.name_output.get_text() == f"Name:{name_text}"
    assert text_box_page.current_address_output.get_text() == f"Current Address :{address_text}"