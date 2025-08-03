import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from pages.main_page import MainPage


def test_simple_footer_text_check(driver):
    """проверка наличия footer text """
    main_page = MainPage(driver)
    main_page.visit()

    # ожидание загрузки страницы
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # ищем текст
    page_text = driver.find_element(By.TAG_NAME, "body").text

    # проверка соответствия
    expected_text_parts = [
        "Все права защищены."
    ]

    # проверка соответствия
    missing_parts = []
    for part in expected_text_parts:
        if part not in page_text:
            missing_parts.append(part)

    assert len(missing_parts) == 0, f"Missing footer text parts: {missing_parts}"


def test_about_page_main_info(driver):
    """перейти на страницу  about и проверить наличие текста 'Основные сведения' в центре"""
    main_page = MainPage(driver)
    main_page.visit()

    #ожидание загрузки
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # переход на страницу
    about_url = "https://ломоносовскаягимназия.рф/about/"
    driver.get(about_url)

    # ожидание загрузки
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # ищем, что текст "Основные сведения" в центре страницы
    # пробуем разные селекторы
    text_selectors = [
        "h1",  # Main heading
        "h2",  # Secondary heading
        "h3",  # Tertiary heading
        ".main-content h1",  # Main content heading
        ".page-title",  # Page title class
        ".content h1",  # Content heading
        ".about-content h1",  # About content heading
        "h1:contains('Основные сведения')",  # Direct text match
        ".page-header h1",  # Page header heading
        ".main-info h1"  # Main info heading
    ]

    text_found = False
    for selector in text_selectors:
        try:
            # ожидание присутствия элемента
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            
            # проверка
            if "Основные сведения" in element.text:
                text_found = True
                break
        except (NoSuchElementException, TimeoutException):
            continue


    if not text_found:
        page_text = driver.find_element(By.TAG_NAME, "body").text
        if "Основные сведения" in page_text:
            text_found = True

    assert text_found, "Text 'Основные сведения' not found on the about page"