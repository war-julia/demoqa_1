
# #import time
# from pages.demoqa import DemoQa
#
# def test_check_icon(browser):
#
#     demo_qa_page = DemoQa(browser)
#     demo_qa_page.visit()
#     # time.sleep(3)
#     demo_qa_page.icon.click()
#     # time.sleep(3)
#     assert demo_qa_page.equal_url()
#     assert demo_qa_page.exist_icon()
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_icon_exist():
    driver = webdriver.Chrome()
    driver.get('https://demoga.com/')
    icon = driver.find_element(By.CSS_SELECTOR, '#app > header> a')
    if icon is None:
        print("Элемент не найден")
    else:
        print("Элемент найден")

