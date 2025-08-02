import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from pages.main_page import MainPage


def test_simple_footer_text_check(driver):
    """Simple test to check that the specified footer text is present on the website"""
    main_page = MainPage(driver)
    main_page.visit()

    # Wait for page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Get the entire page text
    page_text = driver.find_element(By.TAG_NAME, "body").text

    # Check for the specific text parts
    expected_text_parts = [
        "Все права защищены."
    ]

    # Check that all expected text parts are present
    missing_parts = []
    for part in expected_text_parts:
        if part not in page_text:
            missing_parts.append(part)

    assert len(missing_parts) == 0, f"Missing footer text parts: {missing_parts}"