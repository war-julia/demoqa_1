

from pages.demoqa import Demoqa
def test_check_icon(browser):




    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.exist_icon()