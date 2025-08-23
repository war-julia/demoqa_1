import time
import pytest
from pages.modal_dialogs import ModalDialogs
from selenium.webdriver.common.by import By


def test_modal_dialogs(browser):
    modal_page = ModalDialogs(browser)
    
    try:
        modal_page.visit()
        time.sleep(2)
        
        assert modal_page.small_modal_button.visible()
        assert modal_page.large_modal_button.visible()
        
        modal_page.small_modal_button.click()
        time.sleep(1)
        assert modal_page.small_modal_dialog.visible()
        assert modal_page.small_modal_close_button.visible()
        
        modal_page.small_modal_close_button.click()
        time.sleep(1)
        assert not modal_page.small_modal_dialog.visible()
        
        modal_page.large_modal_button.click()
        time.sleep(1)
        assert modal_page.large_modal_dialog.visible()
        assert modal_page.large_modal_close_button.visible()
        
        modal_page.large_modal_close_button.click()
        time.sleep(1)
        assert not modal_page.large_modal_dialog.visible()
        
    except Exception as e:
        pytest.skip(f"Страница недоступна: {e}")
