from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage

def test_navigation(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    # Начальная страница
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    
    # Переход на страницу elements
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()
    
    # Обновление страницы
    browser.refresh()
    assert elements_page.equal_url()
    
    # Навигация назад
    browser.back()
    assert demo_qa_page.equal_url()
    
    # Навигация вперед
    browser.forward()
    assert elements_page.equal_url()