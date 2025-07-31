import pytest
from pages.demoqa import SauceDemo


# def test_login_with_valid_credentials(browser):
#     """Test login with valid credentials"""
#     sauce_demo_page = SauceDemo(browser)
#     sauce_demo_page.visit()
#
#     # Login with standard user
#     sauce_demo_page.login('visual_user', 'secret_sauce')
#
#     # Verify successful login by checking URL change
#     assert 'inventory.html' in sauce_demo_page.get_url()


def test_login_with_invalid_credentials(browser):
    """Test login with invalid credentials"""
    sauce_demo_page = SauceDemo(browser)
    sauce_demo_page.visit()
    
    # Login with invalid credentials
    sauce_demo_page.login('invalid_user', 'wrong_password')
    
    # Verify error message appears
    error_message = sauce_demo_page.get_error_message()
    assert 'Epic sadface' in error_message
