from pages.text_box import TextBox

def test_text_box_submit(browser):
    text_box = TextBox(browser)
    text_box.visit()
    
    # Fill in the form first to ensure proper button state
    text_box.name.send_keys("Test Name")
    text_box.current_address.send_keys("Test Address")
    
    # Check the submit button CSS with correct attribute name and format
    assert text_box.btn_submit.check_css("color", "rgba(255, 255, 255, 1)")
    
    # Verify button is visible
    assert text_box.btn_submit.visible()
