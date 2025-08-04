#!/usr/bin/env python3
"""
Test script to identify issues in the project
"""

def test_imports():
    """Test all imports"""
    print("Testing imports...")
    
    try:
        from components.components import WebElement
        print("✓ WebElement import successful")
    except Exception as e:
        print(f"✗ WebElement import failed: {e}")
    
    try:
        from pages.base_page import BasePage
        print("✓ BasePage import successful")
    except Exception as e:
        print(f"✗ BasePage import failed: {e}")
    
    try:
        from pages.demoqa import DemoQa
        print("✓ DemoQa import successful")
    except Exception as e:
        print(f"✗ DemoQa import failed: {e}")

def test_webdriver():
    """Test WebDriver functionality"""
    print("\nTesting WebDriver...")
    
    try:
        from selenium import webdriver
        driver = webdriver.Chrome()
        print("✓ Chrome driver created successfully")
        driver.quit()
    except Exception as e:
        print(f"✗ Chrome driver failed: {e}")

def test_code_issues():
    """Test for specific code issues"""
    print("\nTesting code issues...")
    
    # Check if WebElement has exist method
    try:
        from components.components import WebElement
        from selenium import webdriver
        driver = webdriver.Chrome()
        element = WebElement(driver, '#test')
        
        if hasattr(element, 'exist'):
            print("✓ WebElement has exist method")
        else:
            print("✗ WebElement missing exist method")
        
        driver.quit()
    except Exception as e:
        print(f"✗ WebElement test failed: {e}")

if __name__ == "__main__":
    print("=" * 50)
    print("PROJECT ISSUES CHECK")
    print("=" * 50)
    
    test_imports()
    test_webdriver()
    test_code_issues()
    
    print("\n" + "=" * 50)
    print("CHECK COMPLETED")
    print("=" * 50) 