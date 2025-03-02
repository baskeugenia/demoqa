import time
from pages.alerts_page import AlertsPage


def test_alerts_exist(browser):
    ap = AlertsPage(browser)
    ap.visit()

    time.sleep(2)
    assert not ap.alert()

    ap.alert_btn.click()
    time.sleep(2)

    assert ap.alert()


def test_alerts_text(browser):
    ap = AlertsPage(browser)
    ap.visit()

    ap.alert_btn.click()

    assert ap.alert().text == 'You clicked a button'

    time.sleep(2)

    ap.alert().accept()

    assert not ap.alert()


def test_confirm(browser):
    ap = AlertsPage(browser)
    ap.visit()
    ap.confirm_btn.click()
    time.sleep(3)

    ap.alert().dismiss()

    assert ap.confirm_result.get_text() == 'You selected Cancel'

def test_prompt(browser):
    ap = AlertsPage(browser)
    ap.visit()
    ap.prompt_btn.click()
    time.sleep(3)
    name = 'Eug'
    ap.alert().send_keys(name)
    ap.alert().accept()

    assert ap.prompt_result.get_text() == 'You entered ' + name





