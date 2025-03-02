import time
from pages.alerts_page import AlertsPage


def test_check_alert(browser):
    ap = AlertsPage(browser)
    ap.visit()

    ap.timer_alert_btn.click()
    time.sleep(6)
    print(ap.alert().text)

    assert ap.alert().text == 'This alert appeared after 5 seconds'


