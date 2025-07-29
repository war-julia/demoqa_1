import pytest
from pages.demoqa import DemoQa


def test_check_icon(browser):
    """Test that the icon exists and is clickable"""
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()

    # Check if icon exists
    assert demo_qa_page.exist_icon()

    # Click on the icon
    demo_qa_page.icon.click()

    # Verify we're still on the same page (icon click should not navigate away)
    assert demo_qa_page.equal_url()
