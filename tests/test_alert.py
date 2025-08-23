import time

from pages.alerts import Alerts:

def test_allert(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    assert not alert_page.alert()
    alert_page.alertButton.click()
    time.sleep(2)
    assert alert_page.alert()

def test_alert_text(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    alert_page.alertButton.click()
    assert alert_page.alert().text == "You clicked a button"
    alert_page.alert().accept()
    assert not alert_page.alert()

def test_confirm(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    alert_page.confirmButton.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.confirmResult.get_text() == "You celected Cancel"

def test_prompt(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    alert_page.promptButton.click()
    time.sleep(2)
    alert_page.alert().accept()
    assert alert_page.promptResult.get_text() == "You entered Artem"
