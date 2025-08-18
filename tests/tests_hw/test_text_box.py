from pages.text_box import TextBox

def test_text_box_submit(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()
    
    text_box_page.name.send_keys("Ivan Ivanov")
    text_box_page.current_address.send_keys("Russia Moscow Polezhaevskaya, 16-8")
    text_box_page.btn_submit.click()

    assert text_box_page.name_output.get_text() == "Ivan Ivanov"
    assert text_box_page.current_address_output.get_text() == "Russia Moscow Polezhaevskaya, 16-8"