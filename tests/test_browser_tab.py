import time
from pages.browser_tab_page import BrowserTabPage


def test_browser_tab(browser):
    btp = BrowserTabPage(browser)
    btp.visit()

    assert len(browser.window_handles) == 1

    btp.new_tab.click()
    time.sleep(2)

    assert len(browser.window_handles) == 2

    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)