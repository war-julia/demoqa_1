# #Создайте директорию tests_hw в папке tests все домашние тесты создавайте в ней
# 1. в классе компонентов создайте метод для получения текста с элементов get_text(self).
#  текст из элемента считывайте так str(self.find_element().text)
# 2. в файле test_check_text.py реализуйте таст кейс:
# a. перейти на страницу 'https://demoqa.com/'
# b. проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’

from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from selenium.webdriver.common.by import By


def test_check_copyright_text(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    # поиск footer
    footer = browser.find_element(By.CSS_SELECTOR, "footer")
    # str(self.find_element().text)
    # проверка copyright text
    copyright_text = "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."

    assert copyright_text in footer.text, "Copyright text not found in footer"


def test_check_text_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()
    
    # center text
    center_element = browser.find_element(By.CSS_SELECTOR, ".col-12.mt-4.col-md-6")
    
    #  проверка center text
    expected_text = "Please select an item from left to start practice."
    assert expected_text in center_element.text, "Center text not found"

