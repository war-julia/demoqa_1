# # перейти на страницу 'https://demoqa.com/'
# # проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’
#
# from pages.demoqa import DemoQa
#
# def test_check_text(browser):
#     demo_qa_page = DemoQa(browser)
#     demo_qa_page.visit()
#
#     assert demo_qa_page.equal_url()
#
# try:
#
#     footer_text = driver.find_element(By.TAG_NAME, 'footer').text
#
#     # Проверка текста
#     expected_text = '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
#     assert footer_text == expected_text, f"Ожидалось: '{expected_text}', найдено: '{footer_text}'"
#     print("Текст в подвале соответствует ожидаемому.")
# except Exception as e:
#     print(f"Ошибка: {e}")
# finally:
#     # Закрытие драйвера
#     driver.quit()