from pages.base_page import BasePage
from components.components import WebElement


class AddRemoveElementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "http://the-internet.herokuapp.com/add_remove_elements/")
        
        # Элементы страницы
        self.add_element_btn = WebElement(driver, "button[onclick='addElement()']")
        self.delete_btns = WebElement(driver, ".added-manually")
        self.add_remove_link = WebElement(driver, "a[href='/add_remove_elements/']")
    
    def click_add_element(self):
      
        self.add_element_btn.click()
    
    def click_delete_btn(self, index=0):
        """Клик по кнопке Delete по индексу"""
        delete_btns = self.driver.find_elements("css selector", ".added-manually")
        if index < len(delete_btns):
            delete_btns[index].click()
    
    def get_delete_buttons_count(self):
        """Получить количество кнопок Delete"""
        return len(self.driver.find_elements("css selector", ".added-manually"))
    
    def add_multiple_elements(self, count):
        """Добавить несколько элементов"""
        for _ in range(count):
            self.click_add_element()
    
    def delete_all_elements(self):
        """Удалить все элементы"""
        delete_btns = self.driver.find_elements("css selector", ".added-manually")
        for btn in delete_btns:
            btn.click()
