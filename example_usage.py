#!/usr/bin/env python3
"""
Example usage of the DemoQA Test Automation Framework

This script demonstrates how to use the framework to test the DemoQA website.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from pages.text_box import TextBox
from pages.form_page import FormPages
from pages.accordion import Accordion


def setup_driver():
    """Setup Chrome WebDriver with appropriate options"""
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # Set user agent to avoid detection
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    # Execute script to remove webdriver property
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver


def test_main_page_example():
    """Example of testing the main DemoQA page"""
    print("Testing DemoQA main page...")
    driver = setup_driver()
    
    try:
        demo_qa_page = DemoQa(driver)
        demo_qa_page.visit()
        
        # Check if page loaded correctly
        assert demo_qa_page.equal_url()
        print(f"Page URL: {demo_qa_page.get_url()}")
        print(f"Page title: {demo_qa_page.get_title()}")
        
        # Check if elements button exists
        if demo_qa_page.btn_elements.exist():
            print("Elements button found")
            demo_qa_page.btn_elements.click()
        else:
            print("Elements button not found")
        
    finally:
        driver.quit()


def test_elements_page_example():
    """Example of testing the elements page"""
    print("\nTesting elements page...")
    driver = setup_driver()
    
    try:
        elements_page = ElementsPage(driver)
        elements_page.visit()
        
        # Check if page loaded correctly
        assert elements_page.equal_url()
        print(f"Elements page URL: {elements_page.get_url()}")
        
        # Check if sidebar elements exist
        if elements_page.btn_sidebar_first.exist():
            print("Sidebar first button found")
        if elements_page.btn_sidebar_first_textbox.exist():
            print("Textbox button found")
        
    finally:
        driver.quit()


def test_text_box_example():
    """Example of testing the text box page"""
    print("\nTesting text box page...")
    driver = setup_driver()
    
    try:
        text_box_page = TextBox(driver)
        text_box_page.visit()
        
        # Fill in the form
        text_box_page.name.send_keys("John Doe")
        text_box_page.current_address.send_keys("123 Test Street")
        text_box_page.btn_submit.click()
        
        # Check output
        name_output = text_box_page.name_output.get_text()
        address_output = text_box_page.current_address_output.get_text()
        print(f"Name output: {name_output}")
        print(f"Address output: {address_output}")
        
    finally:
        driver.quit()


def test_form_page_example():
    """Example of testing the form page"""
    print("\nTesting form page...")
    driver = setup_driver()
    
    try:
        form_page = FormPages(driver)
        form_page.visit()
        
        # Check placeholders
        first_name_placeholder = form_page.first_name.get_dom_attribute("placeholder")
        last_name_placeholder = form_page.last_name.get_dom_attribute("placeholder")
        email_placeholder = form_page.user_email.get_dom_attribute("placeholder")
        
        print(f"First name placeholder: {first_name_placeholder}")
        print(f"Last name placeholder: {last_name_placeholder}")
        print(f"Email placeholder: {email_placeholder}")
        
    finally:
        driver.quit()


def main():
    """Main function to run all examples"""
    print("DemoQA Test Automation Framework - Examples")
    print("=" * 50)
    
    test_main_page_example()
    test_elements_page_example()
    test_text_box_example()
    test_form_page_example()
    
    print("\n" + "=" * 50)
    print("All examples completed!")


if __name__ == '__main__':
    main() 