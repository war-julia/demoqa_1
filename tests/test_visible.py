from pages.elements_page import ElementsPage
import time

def test_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    elements_page.btn_sidebar_first.click()
    time.sleep(3)
    assert elements_page.btn_sidebar_first_textbox.exist()

