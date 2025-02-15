from pages.demoqa import DemoQa
import time


def test_size(browser):
    demoqa = DemoQa(browser)
    browser.set_window_size(500, 500)
    time.sleep(2)

    print('*'*100, browser.get_window_size())
    browser.set_window_size(1000, 1000)
    time.sleep(2)
    assert demoqa.get_title() == 'DEMOQA'
