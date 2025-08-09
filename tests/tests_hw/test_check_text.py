from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from selenium.webdriver.common.by import By


def test_check_footer(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    # assert demo_qa_page.equal_url()
    # поиск footer
    # footer = browser.find_element(By.CSS_SELECTOR, "footer")
    # проверка copyright text
    # footer = "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."

    # assert footer in footer.text, "Copyright text not found in footer"
    assert demo_qa_page.text_footer.get_text() == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."



def test_check_text_please(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    # assert demo_qa_page.equal_url()
    demo_qa_page.btn_elements.click()
    # assert elements_page.equal_url()
    
    # center text
    # center_element = browser.find_element(By.CSS_SELECTOR, ".col-12.mt-4.col-md-6")
    
    #  проверка center text
    # expected_text = "Please select an item from left to start practice."
    # assert expected_text in center_element.text, "Center text not found"
    assert elements_page.text_please.get_text() == "Please select an item from left to start practice."

def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()
