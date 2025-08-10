# from pages.accordion import Accordion
# import time
#
# def test_visible_accordion(browser):
#     accordion_page = Accordion(browser)
#
#     accordion_page.visit()
#     accordion_page.btn_accordion.click()
#     time.sleep(2)
#     assert accordion_page.btn_sidebar_second_textbox.visible()
#
# def test_not_visible_accordion(browser):
#     accordion_page = Accordion(browser)
#
#     accordion_page.visit()
#     assert accordion_page.btn_sidebar_second_textbox.visible()
#     accordion_page.btn_accordion.click()
#     time.sleep(2)
#     assert not accordion_page.btn_sidebar_second_textbox.visible()
#
# def test_visible_accordion_default(browser):
#     accordion_page = Accordion(browser)
#
#     accordion_page.visit()
#     assert accordion_page.btn_accordion_content21.visible()
#     assert accordion_page.btn_accordion_content22.visible()
#     assert accordion_page.btn_accordion_content3.visible()
#     accordion_page.btn_accordion.click()
#     time.sleep(2)
#     assert not accordion_page.btn_accordion_content21.visible()
#     assert not accordion_page.btn_accordion_content22.visible()
#     assert not accordion_page.btn_accordion_content3.visible()