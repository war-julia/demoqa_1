from pages.elements_page import ElementsPage

def test_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    # Click the sidebar button first to expand it
    elements_page.btn_sidebar_first.click()
    # Then check if the textbox is visible
    assert elements_page.btn_sidebar_first_textbox.visible()


def test_not_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    # Initially the checkbox should be visible (sidebar is expanded by default)
    assert elements_page.btn_sidebar_first_checkbox.visible()
    # Click to collapse the sidebar
    elements_page.btn_sidebar_first.click()
    # After clicking, the checkbox should be hidden
    assert not elements_page.btn_sidebar_first_checkbox.visible()