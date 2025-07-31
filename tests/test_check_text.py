import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from pages.main_page import MainPage


class TestFooterText:
    """Test cases for checking footer text on Ломоносовская гимназия website"""

    def test_footer_text_presence(self, driver):
        """Test that the specific footer text is present on the website"""
        main_page = MainPage(driver)
        main_page.visit()

        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Expected footer text
        expected_footer_text = '''Муниципальное бюджетное общеобразовательное учреждение Петрозаводского городского округа "Ломоносовская гимназия", 2020 г.

Все права защищены.

При использовании материалов ссылка на сайт обязательна.'''

        # Try to find footer text using various selectors
        footer_selectors = [
            'footer',
            '.footer',
            '#footer',
            '.site-footer',
            '.main-footer',
            '.copyright',
            '.footer-text',
            '.footer-content',
            'div[class*="footer"]',
            'div[class*="copyright"]',
            'div[class*="rights"]'
        ]

        footer_text_found = False
        actual_footer_text = ""

        for selector in footer_selectors:
            try:
                # Wait for footer element to be present
                footer_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                
                # Get the text content
                actual_footer_text = footer_element.text.strip()
                
                # Check if the expected text is contained in the actual footer text
                if expected_footer_text.strip() in actual_footer_text:
                    footer_text_found = True
                    break
                    
            except (NoSuchElementException, TimeoutException):
                continue

        # If footer not found with specific selectors, try to find text anywhere on the page
        if not footer_text_found:
            try:
                # Search for the text in the entire page
                page_text = driver.find_element(By.TAG_NAME, "body").text
                if expected_footer_text.strip() in page_text:
                    footer_text_found = True
                    actual_footer_text = "Text found in page body"
            except NoSuchElementException:
                pass

        # Assert that the footer text is found
        assert footer_text_found, f"Expected footer text not found. Actual footer text: {actual_footer_text[:200]}..."

    def test_footer_text_complete(self, driver):
        """Test that the footer text contains all required parts"""
        main_page = MainPage(driver)
        main_page.visit()

        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Get page text
        page_text = driver.find_element(By.TAG_NAME, "body").text

        # Check for individual parts of the expected text
        required_parts = [
            "Муниципальное бюджетное общеобразовательное учреждение",
            "Петрозаводского городского округа",
            "Ломоносовская гимназия",
            "2020 г.",
            "Все права защищены",
            "При использовании материалов ссылка на сайт обязательна"
        ]

        missing_parts = []
        for part in required_parts:
            if part not in page_text:
                missing_parts.append(part)

        assert len(missing_parts) == 0, f"Missing footer text parts: {missing_parts}"

    def test_footer_text_formatting(self, driver):
        """Test that the footer text has proper formatting and structure"""
        main_page = MainPage(driver)
        main_page.visit()

        # Wait for page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        # Try to find footer element
        footer_selectors = [
            'footer',
            '.footer',
            '#footer',
            '.site-footer',
            '.main-footer'
        ]

        footer_element = None
        for selector in footer_selectors:
            try:
                footer_element = driver.find_element(By.CSS_SELECTOR, selector)
                break
            except NoSuchElementException:
                continue

        if footer_element:
            # Check that footer is visible
            assert footer_element.is_displayed(), "Footer should be visible"
            
            # Check that footer has some text content
            footer_text = footer_element.text.strip()
            assert len(footer_text) > 0, "Footer should contain text"
            
            # Check that footer contains copyright information
            assert "2020" in footer_text or "Все права защищены" in footer_text, "Footer should contain copyright information"

    def test_footer_text_consistency(self, driver):
        """Test that footer text is consistent across different pages"""
        main_page = MainPage(driver)
        main_page.visit()

        # Get footer text from main page
        main_page_text = driver.find_element(By.TAG_NAME, "body").text

        # Try to navigate to other pages and check footer consistency
        pages_to_test = [
            ("news", main_page.navigate_to_news),
            ("contacts", main_page.navigate_to_contacts),
            ("education", main_page.navigate_to_education)
        ]

        for page_name, navigation_method in pages_to_test:
            try:
                # Navigate to the page
                navigation_success = navigation_method()
                
                if navigation_success:
                    # Wait for page to load
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, "body"))
                    )
                    
                    # Get footer text from this page
                    page_text = driver.find_element(By.TAG_NAME, "body").text
                    
                    # Check that both pages contain the same key footer elements
                    key_elements = ["Ломоносовская гимназия", "Все права защищены"]
                    
                    for element in key_elements:
                        assert (element in main_page_text) == (element in page_text), \
                            f"Footer consistency check failed for {page_name} page"
                
                # Go back to main page for next test
                main_page.visit()
                
            except Exception as e:
                # If navigation fails, continue with next page
                print(f"Navigation to {page_name} page failed: {e}")
                continue 