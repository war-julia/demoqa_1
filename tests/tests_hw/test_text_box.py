# from pages.text_box import TextBox
# import time
#
#
# def test_text_box_submit(browser):
#     text_box_page = TextBox(browser)
#     text_box_page.visit()
#     time.sleep(3)
#     name_text = "Ivan Ivanov"
#     address_text = "Russia Moscow Polezhaevskaya, 16-8"
#     text_box_page.name.send_keys(name_text)
#     text_box_page.current_address.send_keys(address_text)
#     text_box_page.btn_submit.scroll_to_element()
#     time.sleep(1)
#     text_box_page.btn_submit.click()
#     time.sleep(2)
#     name_result = text_box_page.name_output.get_text()
#     address_result = text_box_page.current_address_output.get_text()
#
#     assert name_result == f"Name:{name_text}"
#     assert address_result == f"Current Address :{address_text}"