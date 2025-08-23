import time
from pages.alerts import Alerts


def test_timer_alert(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    
    assert alert_page.timer_alert_button.visible()
    
    alert_page.timer_alert_button.click()
    time.sleep(6)
    
    assert alert_page.alert()
    alert_page.alert().accept()
