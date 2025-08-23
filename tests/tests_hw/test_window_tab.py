import time
from pages.links import Links


def test_home_link_new_tab(browser):
    links_page = Links(browser)
    links_page.visit()
    
    assert links_page.home_link.visible()
    
    link_text = links_page.home_link.get_text()
    assert link_text == "Home"
    
    href = links_page.home_link.get_attribute('href')
    # Проверяем href с учетом возможного слеша в конце
    assert href.startswith("https://demoqa.com"), f"Неверный href: {href}"
    
    original_window = browser.current_window_handle
    links_page.home_link.click()
    time.sleep(3)
    
    windows = browser.window_handles
    assert len(windows) > 1, "Новая вкладка не открылась"
    
    new_window = [window for window in windows if window != original_window][0]
    browser.switch_to.window(new_window)
    
    # Проверяем URL с учетом возможного слеша в конце
    current_url = browser.current_url
    assert current_url.startswith("https://demoqa.com"), f"Неверный URL в новой вкладке: {current_url}"
    
    browser.close()
    browser.switch_to.window(original_window)
