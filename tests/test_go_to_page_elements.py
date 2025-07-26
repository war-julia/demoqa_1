
# import time
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_go_to_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
                                    # time.sleep(3)
                                    # time.sleep(3)
    assert demo_qa_page.equal_url()
                                    # assert demo_qa_page.exist_icon()
    demo_qa_page.click_on_the_btn()
    assert elements_page.equal_url()


