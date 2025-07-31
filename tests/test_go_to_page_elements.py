import pytest
from selenium.webdriver.common.by import By
from pages.demoqa import SauceDemo
from pages.elements_page import InventoryPage


# def test_add_item_to_cart(browser):
#     """Test adding item to cart functionality"""
#     sauce_demo_page = SauceDemo(browser)
#     inventory_page = InventoryPage(browser)
#
#     # Login first
#     sauce_demo_page.visit()
#     sauce_demo_page.login('standard_user', 'secret_sauce')
#
#     # Verify we're on inventory page
#     assert 'inventory.html' in sauce_demo_page.get_url()
#
#     # Add first item to cart
#     inventory_page.add_item_to_cart(0)
#
#     # Verify item was added (button text should change to "Remove")
#     buttons = browser.find_elements(By.CSS_SELECTOR, '.btn_inventory')
#     assert buttons[0].text == "Remove"


def test_logout_functionality(browser):
    """Test logout functionality"""
    sauce_demo_page = SauceDemo(browser)
    inventory_page = InventoryPage(browser)
    
    # Login first
    sauce_demo_page.visit()
    sauce_demo_page.login('visual_user', 'secret_sauce')
    
    # Logout
    inventory_page.logout()
    
    # Verify we're back to login page
    assert sauce_demo_page.equal_url()

