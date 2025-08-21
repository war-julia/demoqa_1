# import time
# from selenium.webdriver.common.by import By
#
# def test_btn_add(driver):
#     # Открыть главную страницу
#     driver.get("http://the-internet.herokuapp.com/")
#
#     # Убедиться, что на странице есть ссылка "Add/Remove Elements" и перейти по ней
#     link = driver.find_element(By.LINK_TEXT, "Add/Remove Elements")
#     link.click()
#
#     # Проверить, что открылся правильный URL
#     assert "http://the-internet.herokuapp.com/add_remove_elements/" in driver.current_url
#
#     # Найти кнопку "Add Element" по атрибуту onclick и тексту
#     add_btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
#     assert add_btn.text == "Add Element"
#
#     # Кликнуть 4 раза
#     for _ in range(4):
#         add_btn.click()
#
#     # Проверить, что появились 4 кнопки "Delete"
#     delete_buttons = driver.find_elements(By.XPATH, '//button[text()="Delete"]')
#     assert len(delete_buttons) == 4
#
#     # Кликнуть на каждую кнопку "Delete"
#     # Берём список заново в цикле, так как DOM меняется после каждого клика
#     for _ in range(4):
#         btn = driver.find_element(By.XPATH, '//button[text()="Delete"]')
#         btn.click()
#         # небольшой короткий пауз для стабильности (опционально)
#         time.sleep(0.1)
#
#     # Убедиться, что кнопки "Delete" пропали
#     remaining = driver.find_elements(By.XPATH, '//button[text()="Delete"]')
#     assert len(remaining) == 0
