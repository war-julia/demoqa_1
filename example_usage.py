#!/usr/bin/env python3
"""
Example usage of the Ломоносовская Гимназия Test Automation Framework

This script demonstrates how to use the framework to test the school's website.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.news_page import NewsPage
from pages.education_page import EducationPage
from pages.contacts_page import ContactsPage


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
    """Example of testing the main page"""
    print("Testing main page...")
    driver = setup_driver()
    
    try:
        main_page = MainPage(driver)
        main_page.visit()
        
        # Get school name
        school_name = main_page.get_school_name()
        print(f"School name: {school_name}")
        
        # Get about information
        about_info = main_page.get_about_info()
        print(f"About info length: {len(about_info)} characters")
        
        # Test navigation
        news_success = main_page.navigate_to_news()
        print(f"Navigation to news: {'Success' if news_success else 'Not available'}")
        
        contacts_success = main_page.navigate_to_contacts()
        print(f"Navigation to contacts: {'Success' if contacts_success else 'Not available'}")
        
        education_success = main_page.navigate_to_education()
        print(f"Navigation to education: {'Success' if education_success else 'Not available'}")
        
    finally:
        driver.quit()


def test_news_page_example():
    """Example of testing the news page"""
    print("\nTesting news page...")
    driver = setup_driver()
    
    try:
        news_page = NewsPage(driver)
        news_page.visit()
        
        # Check news availability
        news_available = news_page.check_news_availability()
        print(f"News section available: {news_available}")
        
        # Get news count
        news_count = news_page.get_news_count()
        print(f"Number of news items: {news_count}")
        
        # Get latest news title
        latest_title = news_page.get_latest_news_title()
        print(f"Latest news title: {latest_title}")
        
    finally:
        driver.quit()


def test_education_page_example():
    """Example of testing the education page"""
    print("\nTesting education page...")
    driver = setup_driver()
    
    try:
        education_page = EducationPage(driver)
        education_page.visit()
        
        # Get available programs
        programs_info = education_page.get_available_programs()
        print(f"Programs info length: {len(programs_info)} characters")
        
        # Check program availability
        humanities_available = education_page.check_program_availability("гуманитарный")
        print(f"Humanities profile available: {humanities_available}")
        
        # Get enrollment information
        enrollment_info = education_page.get_enrollment_information()
        print(f"Enrollment info length: {len(enrollment_info)} characters")
        
    finally:
        driver.quit()


def test_contacts_page_example():
    """Example of testing the contacts page"""
    print("\nTesting contacts page...")
    driver = setup_driver()
    
    try:
        contacts_page = ContactsPage(driver)
        contacts_page.visit()
        
        # Get contact details
        contact_details = contacts_page.get_full_contact_details()
        print("Contact details:")
        for key, value in contact_details.items():
            print(f"  {key}: {value}")
        
        # Check map availability
        map_available = contacts_page.check_map_availability()
        print(f"Map available: {map_available}")
        
        # Check contact form availability
        form_available = contacts_page.check_contact_form_availability()
        print(f"Contact form available: {form_available}")
        
    finally:
        driver.quit()


def main():
    """Main function to run all examples"""
    print("=" * 60)
    print("Ломоносовская Гимназия Test Automation Framework - Examples")
    print("=" * 60)
    print("Website: https://ломоносовскаягимназия.рф/")
    print("=" * 60)
    
    try:
        test_main_page_example()
        test_news_page_example()
        test_education_page_example()
        test_contacts_page_example()
        
        print("\n" + "=" * 60)
        print("All examples completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nError during testing: {e}")
        print("This is expected if the website structure doesn't match our selectors.")


if __name__ == '__main__':
    main() 