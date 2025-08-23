import time
from pages.links import Links


def test_home_link_new_tab(browser):
    links_page = Links(browser)
    links_page.visit()
    
    assert links_page.home_link.visible()
    
    link_text = links_page.home_link.get_text()
    assert link_text == "Home"
    
    href = links_page.home_link.get_attribute('href')
    assert href == "https://demoqa.com"
    
    original_window = browser.current_window_handle
    links_page.home_link.click()
    time.sleep(2)
    
    windows = browser.window_handles
    assert len(windows) > 1, "Новая вкладка не открылась"
    
    new_window = [window for window in windows if window != original_window][0]
    browser.switch_to.window(new_window)
    
    assert browser.current_url == "https://demoqa.com"
    
    browser.close()
    browser.switch_to.window(original_window)
