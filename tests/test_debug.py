# import time
# from pages.tables import Tables
#
# def test_debug_page_load(browser):
#     """Тест для диагностики загрузки страницы"""
#     page_tables = Tables(browser)
#
#     print(f"Переходим на страницу: {page_tables.base_url}")
#     page_tables.visit()
#
#     print(f"Текущий URL: {page_tables.get_url()}")
#     print(f"Заголовок страницы: {page_tables.get_title()}")
#
#     # Ждем немного для загрузки
#     time.sleep(3)
#
#     # Проверяем, есть ли элементы на странице
#     try:
#         if page_tables.page_title.exist():
#             print("Элемент .main-header найден")
#             print(f"Текст заголовка: {page_tables.page_title.get_text()}")
#         else:
#             print("Элемент .main-header НЕ найден")
#     except Exception as e:
#         print(f"Ошибка при поиске заголовка: {e}")
#
#     # Проверяем другие элементы
#     try:
#         if page_tables.add_button.exist():
#             print("Кнопка Add найдена")
#         else:
#             print("Кнопка Add НЕ найдена")
#     except Exception as e:
#         print(f"Ошибка при поиске кнопки Add: {e}")
#
#     # Делаем скриншот для анализа
#     browser.save_screenshot("debug_screenshot.png")
#     print("Скриншот сохранен как debug_screenshot.png")
