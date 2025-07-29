from pages.base_page import BasePage
from components.components import WebElement


class InventoryPage(BasePage):
    """Sauce Demo inventory page class"""

    def __init__(self, driver):
        self.base_url = 'https://www.saucedemo.com/inventory.html'
        super().__init__(driver, self.base_url)

        # Page elements
        self.inventory_container = WebElement(driver, '.inventory_container')
        self.add_to_cart_buttons = WebElement(driver, '.btn_inventory')
        self.cart_icon = WebElement(driver, '.shopping_cart_link')
        self.menu_button = WebElement(driver, '#react-burger-menu-btn')
        self.logout_link = WebElement(driver, '#logout_sidebar_link')

    def add_item_to_cart(self, item_index=0):
        """Add item to cart by index"""
        buttons = self.driver.find_elements(By.CSS_SELECTOR, '.btn_inventory')
        if item_index < len(buttons):
            buttons[item_index].click()

    def open_cart(self):
        """Open shopping cart"""
        self.cart_icon.click()

    def logout(self):
        """Logout from the application"""
        self.menu_button.click()
        self.logout_link.click()



