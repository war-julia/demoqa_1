from pages.demoqa import DemoQa

def test_size(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    
    # Get initial window size
    initial_size = browser.get_window_size()
    
    # Change window size to 1000x300
    browser.set_window_size(1000, 300)
    
    # Verify the size change
    new_size = browser.get_window_size()
    assert new_size['width'] == 1000, f"Expected width 1000, got {new_size['width']}"
    assert new_size['height'] == 300, f"Expected height 300, got {new_size['height']}"
    
    # Change window size back to 1000x1000
    browser.set_window_size(1000, 1000)
    
    # Verify the final size
    final_size = browser.get_window_size()
    assert final_size['width'] == 1000, f"Expected width 1000, got {final_size['width']}"
    assert final_size['height'] == 1000, f"Expected height 1000, got {final_size['height']}"
    
    # Verify that the page is still accessible after size changes
    assert demo_qa_page.icon.exist(), "Page icon should be visible after size changes"
