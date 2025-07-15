from selenium import webdriver
from selenium.webdriver.common.by import By

def test_check_icon():
    driver=webdriver.Chrome()
    driver.get('https://demoqa.com/')

    icon=driver.find_element(By.CSS_SELECTOR, '#app>header>a')
    if icon is None:
        print('Не найден элемент')
    else:
        print('Найден')