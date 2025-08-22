# from pages.text_box import TextBox
#
# def test_text_box_submit(browser):
#     text_box = TextBox(browser)
#     text_box.visit()
#
#     # Fill in the form first to ensure proper button state
#     text_box.full_name_input.send_keys("Test Name")
#     text_box.current_address_input.send_keys("Test Address")
#
#     # Check the submit button CSS with correct attribute name and format
#     assert text_box.submit_button.check_css("color", "rgba(255, 255, 255, 1)")
#     assert text_box.submit_button.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
#     assert text_box.submit_button.check_css('borderColor', 'rgba(0, 123, 255)')
#     # Verify button is visible
#     assert text_box.submit_button.visible()



