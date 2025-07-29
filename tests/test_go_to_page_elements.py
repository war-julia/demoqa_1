import pytest
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_go_to_page_elements(browser):
    """Test navigation to the Elements page"""
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    # Visit the main page
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()

    # Click on Elements button to navigate
    demo_qa_page.btn_elements.click()

    # Verify we're on the Elements page
    assert elements_page.equal_url()

